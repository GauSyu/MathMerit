import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/render_profile.py'
spec = importlib.util.spec_from_file_location('render_profile', SCRIPT)
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
NS = {'s': renderer.NS}


def example(indices=(0, 0, 0, 0, 0), language='en'):
    return {'title': 'Example work', 'language': language,
            'grades': {axis: data['grades'][index]['en'] for (axis, data), index in zip(renderer.AXES.items(), indices)}}


class RenderingTests(unittest.TestCase):
    def test_all_lowest_is_origin_and_neutral(self):
        svg = renderer.render(example())
        root = ET.fromstring(svg)
        points = root.find(".//s:polygon[@id='profile-contour']", NS).get('points').split()
        self.assertEqual(points, ['700.000,450.000'] * 5)
        self.assertNotIn('AI', svg)
        self.assertNotIn('MathMerit', svg)

    def test_mixed_grades_preserve_axis_order_and_positions(self):
        root = ET.fromstring(renderer.render(example((3, 2, 1, 0, 3))))
        expected = {'significance': (700, 190), 'knowledge': (864.850, 396.437),
                    'understanding': (750.941, 520.115), 'methods': (700, 450),
                    'exposition': (452.725, 369.656)}
        for axis, (x, y) in expected.items():
            circle = root.find(f".//s:circle[@id='{axis}-marker']", NS)
            self.assertAlmostEqual(float(circle.get('cx')), x, places=3)
            self.assertAlmostEqual(float(circle.get('cy')), y, places=3)
        contour = root.find(".//s:polygon[@id='profile-contour']", NS).get('points').split()
        self.assertEqual(len(contour), 5)

    def test_single_nonzero_is_line_without_fabricated_area(self):
        root = ET.fromstring(renderer.render(example((1, 0, 0, 0, 0))))
        points = root.find(".//s:polygon[@id='profile-contour']", NS).get('points').split()
        self.assertEqual(points[1:], ['700.000,450.000'] * 4)
        self.assertEqual(points[0], '700.000,363.333')

    def test_all_names_resolve_in_either_language(self):
        for lang in ('zh', 'en'):
            for index in range(4):
                data = example(language='bilingual')
                data['grades'] = {axis: spec['grades'][index][lang] for axis, spec in renderer.AXES.items()}
                self.assertEqual(list(renderer.validate(data)[3].values()), [index] * 5)
                root = ET.fromstring(renderer.render(data))
                for axis in renderer.AXES:
                    node = root.find(f".//s:text[@id='{axis}-grade']", NS)
                    label = ''.join(node.itertext()).replace(' ', '')
                    for name in renderer.AXES[axis]['grades'][index].values():
                        self.assertIn(name.replace(' ', ''), label)

    def test_missing_numeric_wrong_axis_and_unknown_grades_rejected(self):
        for value in (None, 0, True, '3', 'A Step Forward', 'unknown'):
            data = example()
            data['grades']['significance'] = value
            with self.assertRaises(ValueError): renderer.render(data)
        data = example()
        del data['grades']['methods']
        with self.assertRaises(ValueError): renderer.render(data)

    def test_explicit_ai_context_and_xml_escaping(self):
        data = example(language='zh')
        data['context'] = 'ai-reading-selection'
        data['title'] = 'A < B & C > D'
        root = ET.fromstring(renderer.render(data))
        title = root.find('s:title', NS).text
        self.assertIn('AI 阅读筛选推测图', title)
        self.assertIn(data['title'], title)
        self.assertEqual(len(root.findall('.//s:script', NS)), 0)

    def test_long_title_grows_canvas(self):
        short = ET.fromstring(renderer.render(example()))
        data = example()
        data['title'] = 'W' * 180 + '中文题目' * 20
        long = ET.fromstring(renderer.render(data))
        self.assertGreater(float(long.get('height')), float(short.get('height')))
        for text in long.findall('.//s:text', NS):
            for span in text:
                self.assertLess(float(span.get('y')), float(long.get('height')))

    def test_cli_validation_and_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, output = Path(tmp) / 'input.json', Path(tmp) / 'output.svg'
            source.write_text(json.dumps(example()))
            run = lambda: subprocess.run([sys.executable, '-B', str(SCRIPT), str(source), str(output)], capture_output=True)
            self.assertEqual(run().returncode, 0)
            original = output.read_bytes()
            self.assertEqual(run().returncode, 2)
            self.assertEqual(output.read_bytes(), original)
            output.unlink()
            data = example(); del data['grades']['knowledge']
            source.write_text(json.dumps(data))
            self.assertEqual(run().returncode, 2)
            self.assertFalse(output.exists())
            source.write_text('{"title":"first","title":"conflict"}')
            self.assertEqual(run().returncode, 2)
            self.assertFalse(output.exists())

    def test_illegal_xml_title_never_creates_or_truncates_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, output = Path(tmp) / 'input.json', Path(tmp) / 'output.svg'
            for code in (0, 8, 0xD800, 0xDFFF, 0xFFFE, 0xFFFF):
                data = example(); data['title'] = 'A' + chr(code) + 'B'
                source.write_text(json.dumps(data))
                command = [sys.executable, '-B', str(SCRIPT), str(source), str(output)]
                self.assertEqual(subprocess.run(command, capture_output=True).returncode, 2)
                self.assertFalse(output.exists())
                output.write_text('existing diagram')
                self.assertEqual(subprocess.run(command + ['--overwrite'], capture_output=True).returncode, 2)
                self.assertEqual(output.read_text(), 'existing diagram')
                output.unlink()


if __name__ == '__main__':
    unittest.main()
