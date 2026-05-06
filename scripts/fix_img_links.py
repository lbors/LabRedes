#!/usr/bin/env python3
"""Fix img links in docs markdown files by replacing any leading ../.../img/... with /img/ (site-root absolute path).
This script makes backups of modified files (file.bak).
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
docs = root / 'docs'
pattern = re.compile(r"\(\.{2,}/(?:\.{2,}/)*img/")

modified = []
for md in docs.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    new_text, n = pattern.subn('(/img/', text)
    if n:
        bak = md.with_suffix(md.suffix + '.bak')
        bak.write_text(text, encoding='utf-8')
        md.write_text(new_text, encoding='utf-8')
        modified.append((str(md), n))

if modified:
    print('Modified files:')
    for f, c in modified:
        print(f, c)
else:
    print('No changes made.')

