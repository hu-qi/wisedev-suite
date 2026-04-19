#!/usr/bin/env python3
"""根据 OpenAPI paths 生成简易 mock 示例索引。"""
from __future__ import annotations
import sys
from pathlib import Path
import yaml

METHODS = ['get', 'post', 'put', 'patch', 'delete']

def main() -> int:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('openapi.yaml')
    if not source.exists():
        print(f'[ERROR] file not found: {source}')
        return 1
    data = yaml.safe_load(source.read_text(encoding='utf-8'))
    paths = data.get('paths', {})
    result = {'mock_profiles': []}
    for path_name, path_item in paths.items():
        for method in METHODS:
            if method in path_item:
                result['mock_profiles'].append({
                    'operation': f'{method.upper()} {path_name}',
                    'profiles': ['happy_path', 'pending_review', 'partial_completion'],
                })
    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
