#!/usr/bin/env python3
"""根据业务标签和资源名生成 OpenAPI 骨架。"""
from __future__ import annotations
import sys
import yaml


def main() -> int:
    title = sys.argv[1] if len(sys.argv) > 1 else 'Generated API'
    resource = sys.argv[2] if len(sys.argv) > 2 else 'resources'
    tag = sys.argv[3] if len(sys.argv) > 3 else resource.rstrip('s')
    skeleton = {
        'openapi': '3.0.3',
        'info': {'title': title, 'version': '0.1.0', 'description': f'{title} contract'},
        'servers': [{'url': '/api'}],
        'tags': [{'name': tag, 'description': f'{tag} domain'}],
        'paths': {
            f'/{resource}': {
                'get': {
                    'tags': [tag],
                    'summary': f'查询{resource}列表',
                    'responses': {'200': {'description': 'success'}},
                }
            }
        },
        'components': {'schemas': {}, 'responses': {}, 'parameters': {}, 'securitySchemes': {}},
    }
    print(yaml.safe_dump(skeleton, allow_unicode=True, sort_keys=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
