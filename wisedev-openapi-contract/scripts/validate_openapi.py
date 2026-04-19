#!/usr/bin/env python3
"""对 openapi.yaml 做最小结构校验。"""
from __future__ import annotations
import sys
from pathlib import Path
import yaml

REQUIRED_TOP_LEVEL = ['openapi', 'info', 'paths', 'components']

def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('openapi.yaml')
    if not target.exists():
        print(f'[ERROR] file not found: {target}')
        return 1
    try:
        data = yaml.safe_load(target.read_text(encoding='utf-8'))
    except Exception as exc:
        print(f'[ERROR] yaml parse failed: {exc}')
        return 1
    missing = [key for key in REQUIRED_TOP_LEVEL if key not in data]
    if missing:
        print('[ERROR] missing top-level keys:', ', '.join(missing))
        return 1
    info = data.get('info', {})
    for key in ['title', 'version', 'description']:
        if key not in info:
            print(f'[ERROR] info.{key} is required')
            return 1
    if not isinstance(data.get('paths'), dict) or not data['paths']:
        print('[ERROR] paths must be a non-empty object')
        return 1
    print('[OK] minimal OpenAPI structure looks valid')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
