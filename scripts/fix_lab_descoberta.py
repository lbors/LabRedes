#!/usr/bin/env python3
"""Replace occurrences of 'Lab%20Descoberta' with 'Descoberta' in docs markdown files."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
docs = root / 'docs'
count = 0
for md in docs.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    if 'Lab%20Descoberta' in text:
        new_text = text.replace('Lab%20Descoberta', 'Descoberta')
        bak = md.with_suffix(md.suffix + '.bak2')
        bak.write_text(text, encoding='utf-8')
        md.write_text(new_text, encoding='utf-8')
        count += 1
print(f'Modified {count} files')

