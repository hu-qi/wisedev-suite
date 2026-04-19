#!/usr/bin/env python3
"""检查原型目录关键文件是否齐全。"""
from __future__ import annotations
from pathlib import Path
import sys

REQUIRED = [
    'package.json',
    'vite.config.ts',
    'src/App.vue',
    'src/main.ts',
    'src/router/index.ts',
    'src/mock',
]


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    missing = [item for item in REQUIRED if not (target / item).exists()]
    if missing:
        print('[ERROR] missing required items:')
        for item in missing:
            print(' -', item)
        return 1
    print('[OK] prototype structure looks complete')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
