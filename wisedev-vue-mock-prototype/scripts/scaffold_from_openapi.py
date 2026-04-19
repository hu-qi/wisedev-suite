#!/usr/bin/env python3
"""从 OpenAPI tags/path 生成 route 与 mock 模块草稿。"""
from __future__ import annotations
from pathlib import Path
import sys
import yaml


def main() -> int:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('openapi.yaml')
    if not source.exists():
        print('[ERROR] openapi file not found')
        return 1
    data = yaml.safe_load(source.read_text(encoding='utf-8'))
    tags = [t.get('name') for t in data.get('tags', []) if isinstance(t, dict) and t.get('name')]
    paths = list(data.get('paths', {}).keys())
    result = {
        'modules': tags,
        'routes': [{'path': p, 'name': p.strip('/').replace('/', '-')} for p in paths],
        'mockHandlers': [f'{t}.ts' for t in tags],
    }
    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
