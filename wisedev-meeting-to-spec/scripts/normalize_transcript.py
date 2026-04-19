#!/usr/bin/env python3
"""把带说话人与时间戳的转写，归一化为便于分析的段落文本。"""
from __future__ import annotations
import re
import sys
from pathlib import Path

TIMESTAMP = re.compile(r'^\s*[\d:：]{4,}\s*$')
SPEAKER = re.compile(r'^\s*发言人\d+\s*$')

def main() -> int:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    text = source.read_text(encoding='utf-8') if source else sys.stdin.read()
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or TIMESTAMP.match(line) or SPEAKER.match(line):
            continue
        lines.append(line)
    print('\n'.join(lines))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
