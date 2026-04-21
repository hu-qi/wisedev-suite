#!/usr/bin/env python3
"""从 OpenAPI tags/path 生成 route 与 mock 模块草稿。"""
from __future__ import annotations
import json
from pathlib import Path
import sys
import yaml


DEFAULT_THEME_ID = 'stable_enterprise'
ACTION_SEGMENTS = {'receive', 'feedback', 'confirm', 'resubmit', 'forward', 'submit', 'approve', 'reject'}
TAG_LABELS = {
    'dispatchOrders': '调度指令',
    'dispatchMaterials': '下发材料',
    'meetings': '会议通知',
    'groupReports': '组报表',
    'assistRequests': '协助申请',
    'dashboards': '综合看板',
    'auditLogs': '审计日志',
}
ACTION_LABELS = {
    'receive': '签收',
    'feedback': '反馈',
    'confirm': '确认',
    'resubmit': '重新提交',
    'forward': '转办',
    'submit': '提交',
    'approve': '审批',
    'reject': '驳回',
}


def to_module_name(tag: str) -> str:
    chars: list[str] = []
    for index, char in enumerate(tag):
        if char.isupper() and index > 0:
            chars.append('-')
        chars.append(char.lower())
    return ''.join(chars)


def to_view_name(path: str) -> str:
    segments = [segment for segment in path.strip('/').split('/') if segment]
    parts: list[str] = []
    for segment in segments:
        cleaned = segment.strip('{}')
        normalized = cleaned.replace('-', ' ').replace('_', ' ')
        parts.append(''.join(word.capitalize() for word in normalized.split()))
    if not parts:
        return 'DashboardView.vue'
    return ''.join(parts) + 'View.vue'


def guess_template_type(path: str) -> str:
    segments = [segment for segment in path.strip('/').split('/') if segment]
    if not segments:
        return 'dashboard'
    if segments[0] in {'dashboard', 'dashboards'}:
        return 'dashboard'
    if segments[-1].strip('{}') in ACTION_SEGMENTS:
        return 'workflow'
    if any(segment.startswith('{') and segment.endswith('}') for segment in segments):
        return 'detail'
    return 'list'


def build_view_entries(paths: list[str], tag: str) -> list[dict]:
    if not paths:
        fallback_name = f'{tag[:1].upper()}{tag[1:]}View.vue'
        return [{
            'path': '',
            'view': fallback_name,
            'templateType': 'list',
            'pageTitle': f'{TAG_LABELS.get(tag, tag)}列表',
            'pageSummary': f'{TAG_LABELS.get(tag, tag)}模块列表页草稿。',
        }]
    entries: list[dict] = []
    module_label = TAG_LABELS.get(tag, tag)
    for path in paths:
        template_type = guess_template_type(path)
        segments = [segment for segment in path.strip('/').split('/') if segment]
        last_segment = segments[-1].strip('{}') if segments else ''
        if template_type == 'dashboard':
            page_title = module_label
            page_summary = f'{module_label}页面草稿，对应路由 {path}。'
        elif template_type == 'detail':
            page_title = f'{module_label}详情'
            page_summary = f'{module_label}详情页草稿，对应路由 {path}。'
        elif template_type == 'workflow':
            action_label = ACTION_LABELS.get(last_segment, last_segment or '处理')
            page_title = f'{module_label}{action_label}'
            page_summary = f'{module_label}{action_label}页草稿，对应路由 {path}。'
        else:
            page_title = f'{module_label}列表'
            page_summary = f'{module_label}列表页草稿，对应路由 {path}。'
        entries.append({
            'path': path,
            'view': to_view_name(path),
            'templateType': template_type,
            'pageTitle': page_title,
            'pageSummary': page_summary,
        })
    return entries


def build_module_scaffold(tags: list[str], paths: list[str]) -> list[dict]:
    path_map: dict[str, list[str]] = {}
    for path in paths:
        root = path.strip('/').split('/')[0] if path.strip('/') else 'dashboard'
        path_map.setdefault(root, []).append(path)

    scaffolds: list[dict] = []
    for tag in tags:
        module_name = to_module_name(tag)
        matched_paths = [
            path for root, root_paths in path_map.items()
            if root.replace('-', '').lower() in module_name.replace('-', '')
            for path in root_paths
        ]
        view_entries = build_view_entries(matched_paths, tag)
        scaffolds.append({
            'module': module_name,
            'sourceTag': tag,
            'suggestedPaths': [
                f'src/modules/{module_name}/views',
                f'src/modules/{module_name}/components',
                f'src/modules/{module_name}/store',
                f'src/modules/{module_name}/mock',
                f'src/modules/{module_name}/types',
            ],
            'views': [entry['view'] for entry in view_entries],
            'viewEntries': view_entries,
            'mockHandler': f'{tag}.ts',
        })
    return scaffolds


def build_route_records(scaffold: list[dict]) -> list[dict]:
    records: list[dict] = []
    for module in scaffold:
        for view_entry in module.get('viewEntries', []):
            raw_path = view_entry.get('path') or f"/{module['module']}"
            path = raw_path.replace('{', ':').replace('}', '')
            route_name = raw_path.strip('/').replace('/', '-').replace('{', '').replace('}', '') or 'dashboard'
            records.append({
                'path': path,
                'name': route_name,
                'module': module['module'],
                'view': view_entry['view'],
                'templateType': view_entry['templateType'],
                'pageTitle': view_entry.get('pageTitle', ''),
                'sourcePath': raw_path,
            })
    return records


def parse_args(argv: list[str]) -> tuple[Path, str | None, Path | None]:
    source_arg: str | None = None
    theme_arg: str | None = None
    write_target: Path | None = None
    index = 0
    while index < len(argv):
        item = argv[index]
        if item == '--write':
            if index + 1 >= len(argv):
                print('[ERROR] --write requires a target directory')
                raise SystemExit(1)
            write_target = Path(argv[index + 1])
            index += 2
            continue
        if source_arg is None:
            source_arg = item
        elif theme_arg is None:
            theme_arg = item
        else:
            print(f'[ERROR] unexpected argument: {item}')
            raise SystemExit(1)
        index += 1
    return Path(source_arg or 'openapi.yaml'), theme_arg, write_target


def load_theme_meta(theme_path: str | None) -> dict:
    if not theme_path:
        return {
            'recommendedThemeId': DEFAULT_THEME_ID,
            'themeSource': 'default',
            'themeFiles': ['src/theme/tokens.ts', 'src/theme/theme.css'],
            'note': 'If wisedev-prototype-design has already produced a theme package, replace the defaults with the selected theme.',
        }
    source = Path(theme_path)
    if not source.exists():
        print(f'[ERROR] theme file not found: {source}')
        raise SystemExit(1)
    data = json.loads(source.read_text(encoding='utf-8'))
    return {
        'recommendedThemeId': data.get('themeId', DEFAULT_THEME_ID),
        'themeSource': str(source),
        'themeFiles': ['src/theme/tokens.ts', 'src/theme/theme.css'],
        'themeName': data.get('themeName', ''),
        'note': 'Apply this theme package when initializing the Vue prototype scaffold.',
    }


def write_file_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding='utf-8')


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def build_view_content(view_entry: dict, module_name: str, theme_id: str) -> str:
    view_name = view_entry['view']
    title = view_entry.get('pageTitle') or view_name.removesuffix('.vue').replace('View', '')
    template_type = view_entry['templateType']
    path_hint = view_entry.get('path') or f'/{module_name}'
    summary = view_entry.get('pageSummary') or f"{module_name} 模块页面草稿，当前按 {theme_id} 主题生成。"

    if template_type == 'dashboard':
        body = """    <div class="hero-panel">Hero / 摘要区</div>
    <div class="panel-grid panel-grid--cards">统计卡片区</div>
    <div class="panel-grid">进度分布区</div>
    <div class="panel-grid">待办与预警区</div>"""
        summary = view_entry.get('pageSummary') or f"{module_name} 模块看板草稿，对应路由 {path_hint}，当前按 {theme_id} 主题生成。"
    elif template_type == 'detail':
        body = """    <div class="hero-panel">对象摘要 / 状态区</div>
    <div class="detail-grid">
      <div class="panel-card">基础信息</div>
      <div class="panel-card">过程信息</div>
      <div class="panel-card detail-grid__full">操作记录</div>
    </div>"""
        summary = view_entry.get('pageSummary') or f"{module_name} 模块详情页草稿，对应路由 {path_hint}。"
    elif template_type == 'workflow':
        body = """    <div class="panel-card">流程节点</div>
    <div class="panel-card">状态时间线</div>
    <div class="panel-card">附件与消息</div>"""
        summary = view_entry.get('pageSummary') or f"{module_name} 模块流程动作页草稿，对应路由 {path_hint}。"
    else:
        body = """    <div class="panel-card">筛选区</div>
    <div class="panel-card">表格 / 卡片列表</div>"""
        summary = view_entry.get('pageSummary') or f"{module_name} 模块列表页草稿，对应路由 {path_hint}。"

    return f"""<template>
  <section class="page-section">
    <header class="page-header">
      <h1 class="page-title">{title}</h1>
      <p class="page-summary">{summary}</p>
    </header>
{body}
  </section>
</template>
"""


def build_store_content(module_name: str) -> str:
    store_name = module_name.replace('-', '')
    return f"""import {{ defineStore }} from 'pinia'

export const use{store_name[:1].upper() + store_name[1:]}Store = defineStore('{module_name}', {{
  state: () => ({{
    loading: false,
    items: [] as Array<Record<string, unknown>>,
  }}),
}})
"""


def build_mock_content(source_tag: str) -> str:
    return f"""export const {source_tag}Handlers = {{
  list: () => ({{
    code: 'SUCCESS',
    message: 'ok',
    data: {{
      items: [],
      page: {{ pageNo: 1, pageSize: 20, total: 0 }},
    }},
  }}),
}}
"""


def build_router_content(route_records: list[dict]) -> str:
    lines = [
        "import { createRouter, createWebHistory } from 'vue-router'",
        "",
        "export const router = createRouter({",
        "  history: createWebHistory(),",
        "  routes: [",
    ]
    for record in route_records:
        lines.extend([
            "    {",
            f"      path: '{record['path']}',",
            f"      name: '{record['name']}',",
            f"      component: () => import('@/modules/{record['module']}/views/{record['view']}'),",
            "    },",
        ])
    lines.extend([
        "  ],",
        "})",
        "",
    ])
    return "\n".join(lines)


def write_module_scaffold(target: Path, scaffold: list[dict], route_records: list[dict], theme_id: str) -> None:
    for module in scaffold:
        module_root = target / 'src' / 'modules' / module['module']
        for rel_path in ['views', 'components', 'store', 'mock', 'types']:
            (module_root / rel_path).mkdir(parents=True, exist_ok=True)
        for view_entry in module.get('viewEntries', []):
            write_file_if_missing(
                module_root / 'views' / view_entry['view'],
                build_view_content(view_entry, module['module'], theme_id),
            )
        write_file_if_missing(
            module_root / 'store' / 'index.ts',
            build_store_content(module['module']),
        )
        write_file_if_missing(
            module_root / 'mock' / module['mockHandler'],
            build_mock_content(module['sourceTag']),
        )
        write_file_if_missing(
            module_root / 'types' / 'index.ts',
            f"export type {module['sourceTag'][:1].upper() + module['sourceTag'][1:]}Record = Record<string, unknown>\n",
        )
    write_file(
        target / 'src' / 'router' / 'index.ts',
        build_router_content(route_records),
    )


def main() -> int:
    source, theme_path, write_target = parse_args(sys.argv[1:])
    if not source.exists():
        print('[ERROR] openapi file not found')
        return 1
    data = yaml.safe_load(source.read_text(encoding='utf-8'))
    tags = [t.get('name') for t in data.get('tags', []) if isinstance(t, dict) and t.get('name')]
    paths = list(data.get('paths', {}).keys())
    theme_meta = load_theme_meta(theme_path)
    module_scaffold = build_module_scaffold(tags, paths)
    route_records = build_route_records(module_scaffold)
    result = {
        'modules': tags,
        'routes': route_records,
        'mockHandlers': [f'{t}.ts' for t in tags],
        'theme': theme_meta,
        'moduleScaffold': module_scaffold,
    }
    if write_target is not None:
        write_module_scaffold(write_target, module_scaffold, route_records, theme_meta['recommendedThemeId'])
        result['writtenTo'] = str(write_target)
    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
