#!/usr/bin/env python3
"""初始化 Vue 原型骨架目录。"""
from __future__ import annotations
from pathlib import Path
import sys

DEFAULT_DIRS = [
    'src/router', 'src/stores', 'src/layouts', 'src/components', 'src/modules',
    'src/mock/handlers', 'src/mock/datasets', 'src/mock/scenarios', 'src/types'
]


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('prototype-app')
    for item in DEFAULT_DIRS:
        (target / item).mkdir(parents=True, exist_ok=True)
    for rel in ['src/App.vue', 'src/main.ts', 'src/router/index.ts', 'package.json', 'vite.config.ts']:
        file_path = target / rel
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if not file_path.exists():
            file_path.write_text('// TODO\n', encoding='utf-8')
    print(f'[OK] initialized vue prototype scaffold at {target}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
