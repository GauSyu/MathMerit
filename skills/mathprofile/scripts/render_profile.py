#!/usr/bin/env python3
"""Render supplied ordinal contribution grades as an SVG; no assessment or network."""
import argparse
import json
import math
from pathlib import Path
import unicodedata
import xml.etree.ElementTree as ET

AXES = json.loads((Path(__file__).resolve().parents[1] / 'references/grades.json').read_text())
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)


def element(parent, tag, attrs=None, text=None):
    node = ET.SubElement(parent, f'{{{NS}}}{tag}', {k: str(v) for k, v in (attrs or {}).items()})
    node.text = text
    return node


def wrap(text, width):
    """Conservative character-width wrapping, including unbroken titles and CJK."""
    def units(char):
        if unicodedata.east_asian_width(char) in ('W', 'F') or char in 'WM@%':
            return 2
        if char in " ilI.,:;'|!\t":
            return .7
        return 1.6 if char.isupper() else 1.3

    lines, line, size = [], '', 0
    for char in text:
        cost = units(char)
        if char == '\n':
            lines.append(line.rstrip())
            line, size = '', 0
            continue
        if line and size + cost > width:
            split = line.rfind(' ')
            if split > len(line) // 3:
                lines.append(line[:split].rstrip())
                line = line[split + 1:]
                size = sum(units(c) for c in line)
            else:
                lines.append(line.rstrip())
                line, size = '', 0
        line += char
        size += cost
    if line or not lines:
        lines.append(line.rstrip())
    return lines


def text_block(parent, text, x, y, width=40, size=20, step=26, **attrs):
    lines = wrap(text, width)
    node = element(parent, 'text', {'x': x, 'y': y, 'font-size': size, 'text-anchor': 'middle', 'fill': '#243748', **attrs})
    for i, line in enumerate(lines):
        element(node, 'tspan', {'x': x, 'y': y + i * step}, line)
    return y + len(lines) * step


def validate(data):
    if not isinstance(data, dict) or set(data) - {'title', 'language', 'grades', 'context'}:
        raise ValueError('Expected title, language, grades, and optional context.')
    title = data.get('title')
    if not isinstance(title, str) or not title.strip():
        raise ValueError('Supply a nonempty work title.')
    if any(not (c in '\t\n\r' or 0x20 <= ord(c) <= 0xD7FF or
                0xE000 <= ord(c) <= 0xFFFD or 0x10000 <= ord(c) <= 0x10FFFF)
           for c in title):
        raise ValueError('Title contains characters not permitted in XML 1.0.')
    language = data.get('language')
    if language not in ('zh', 'en', 'bilingual'):
        raise ValueError('language must be zh, en, or bilingual.')
    context = data.get('context', 'contribution')
    if context not in ('contribution', 'ai-reading-selection'):
        raise ValueError('context must be contribution or ai-reading-selection.')
    grades = data.get('grades')
    if not isinstance(grades, dict) or set(grades) != set(AXES):
        raise ValueError('Supply exactly one grade for each of: ' + ', '.join(AXES))
    positions = {}
    for axis, spec in AXES.items():
        value = grades[axis]
        matches = [i for i, grade in enumerate(spec['grades']) if isinstance(value, str) and value in grade.values()]
        if len(matches) != 1:
            choices = '; '.join(f'{g["zh"]} / {g["en"]}' for g in spec['grades'])
            raise ValueError(f'Invalid {axis} grade {value!r}. Use one of: {choices}')
        positions[axis] = matches[0]
    return title.strip(), language, context, positions


def render(data):
    title, language, context, positions = validate(data)
    langs = ('zh', 'en') if language == 'bilingual' else (language,)
    titles = {'contribution': {'zh': '数学贡献五维图', 'en': 'Mathematical contribution profile'},
              'ai-reading-selection': {'zh': 'AI 阅读筛选推测图', 'en': 'AI reading-selection profile'}}
    heading = ' / '.join(titles[context][lang] for lang in langs)
    root = ET.Element(f'{{{NS}}}svg', {'width': '1400', 'role': 'img', 'aria-labelledby': 'chart-title chart-description'})
    element(root, 'title', {'id': 'chart-title'}, heading + ': ' + title)
    descriptions = {'zh': '按所提供的五项等级绘制。最低档在原点，其余三档依次向外；图形面积不表示总体价值。',
                    'en': 'Drawn from the five supplied grades. Lowest grades share the origin; three higher grades lie on successive rings. Area does not represent overall value.'}
    element(root, 'desc', {'id': 'chart-description'}, ' '.join(descriptions[lang] for lang in langs))
    element(root, 'style', text="text { font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Noto Sans CJK SC', sans-serif; }")
    background = element(root, 'rect', {'width': 1400, 'fill': '#ffffff'})
    bottom = text_block(root, heading, 700, 40, width=88, size=26, step=34, id='profile-title', **{'font-weight': '600'})
    bottom = text_block(root, title, 700, bottom + 8, width=90, size=24, step=32)
    chart = element(root, 'g', {'transform': f'translate(0 {bottom})'})
    cx, cy, radius = 700, 450, 260
    directions = [(math.sin(2 * math.pi * i / 5), -math.cos(2 * math.pi * i / 5)) for i in range(5)]

    def point(index, r):
        dx, dy = directions[index]
        return cx + r * dx, cy + r * dy

    def coordinates(points):
        return ' '.join(f'{x:.3f},{y:.3f}' for x, y in points)

    grid = element(chart, 'g', {'id': 'grid', 'fill': 'none', 'stroke': '#cbd5e1', 'stroke-width': '1.2'})
    for step in (1, 2, 3):
        r = radius * step / 3
        element(grid, 'polygon', {'data-radius': r, 'points': coordinates([point(i, r) for i in range(5)])})
    for i in range(5):
        x, y = point(i, radius)
        element(grid, 'line', {'x1': cx, 'y1': cy, 'x2': x, 'y2': y})
    markers = [point(i, radius * positions[axis] / 3) for i, axis in enumerate(AXES)]
    element(chart, 'polygon', {'id': 'profile-contour', 'points': coordinates(markers), 'fill': '#176373', 'fill-opacity': '.2', 'stroke': '#176373', 'stroke-width': '2.5', 'stroke-linejoin': 'round'})
    for (axis, index), (x, y) in zip(positions.items(), markers):
        element(chart, 'circle', {'id': axis + '-marker', 'data-grade-index': index, 'cx': f'{x:.3f}', 'cy': f'{y:.3f}', 'r': 8, 'fill': '#176373', 'stroke': '#ffffff', 'stroke-width': 2})
    label_positions = [(700, 90), (1120, 317), (990, 757), (410, 757), (280, 317)]
    for (axis, spec), (x, y) in zip(AXES.items(), label_positions):
        y = text_block(chart, ' / '.join(spec[lang] for lang in langs), x, y, width=34, size=22, step=26, **{'font-weight': '600'})
        text_block(chart, '\n'.join(spec['grades'][positions[axis]][lang] for lang in langs), x, y + 10, width=32, size=18, step=24, id=axis + '-grade', fill='#176373')
    legends = {'zh': '最低档位于原点，其余三档依次向外。等级只表示次序，间距和面积不表示贡献大小。',
               'en': 'Lowest grades share the origin; three higher grades lie on successive rings. Positions show order, not equal differences or overall value.'}
    y = bottom + 900
    for lang in langs:
        y = text_block(root, legends[lang], 700, y, width=115, size=18, step=24) + 6
    y += 20
    for axis, spec in AXES.items():
        for lang in langs:
            line = spec[lang] + ': ' + ' → '.join(grade[lang] for grade in spec['grades'])
            y = text_block(root, line, 100, y, width=110, size=18, step=25, **{'text-anchor': 'start'})
        y += 14
    height = y + 30
    root.set('height', str(height))
    root.set('viewBox', f'0 0 1400 {height}')
    background.set('height', str(height))
    return ET.tostring(root, encoding='unicode', xml_declaration=True)


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    try:
        if args.input.resolve() == args.output.resolve():
            raise ValueError('Input and output must be different files.')
        if args.output.suffix.lower() != '.svg':
            raise ValueError('Output must have an .svg extension.')
        data = json.loads(args.input.read_text(encoding='utf-8'), object_pairs_hook=no_duplicate_keys)
        svg = render(data)
        with args.output.open('w' if args.overwrite else 'x', encoding='utf-8') as stream:
            stream.write(svg + '\n')
    except (ValueError, OSError) as exc:
        parser.exit(2, f'Error: {exc}\n')
    print(args.output)


if __name__ == '__main__':
    main()
