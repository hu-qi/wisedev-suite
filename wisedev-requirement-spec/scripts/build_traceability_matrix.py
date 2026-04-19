#!/usr/bin/env python3
"""根据需求编号列表生成追踪矩阵骨架。"""
from __future__ import annotations
import sys


def main() -> int:
    ids = sys.argv[1:] or ['FR-001', 'FR-002']
    print('| 需求编号 | 场景 | 设计模块 | API 标签 | 页面模块 |')
    print('| --- | --- | --- | --- | --- |')
    for item in ids:
        print(f'| {item} |  |  |  |  |')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
