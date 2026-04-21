#!/usr/bin/env python3
"""初始化 Vue 原型骨架目录。"""
from __future__ import annotations
import json
from pathlib import Path
import sys

DEFAULT_DIRS = [
    'src/router', 'src/stores', 'src/layouts', 'src/components', 'src/modules',
    'src/mock/handlers', 'src/mock/datasets', 'src/mock/scenarios', 'src/theme', 'src/types'
]

DEFAULT_THEME = {
    'themeId': 'stable_enterprise',
    'themeName': 'Stable Enterprise',
    'color': {
        'bgCanvas': '#F6F8FB',
        'bgSurface': '#FFFFFF',
        'bgMuted': '#EEF3F8',
        'textPrimary': '#1E293B',
        'textSecondary': '#475569',
        'textMuted': '#64748B',
        'border': '#D9E2EC',
        'primary': '#175CD3',
        'accent': '#0F766E',
        'success': '#15803D',
        'warning': '#B45309',
        'danger': '#B42318',
    },
    'radius': {
        'panel': '14px',
        'card': '12px',
        'control': '10px',
    },
    'shadow': {
        'panel': '0 10px 24px rgba(15, 23, 42, 0.06)',
        'card': '0 6px 18px rgba(15, 23, 42, 0.05)',
    },
    'density': {
        'pageMaxWidth': '1440px',
        'gridGap': '20px',
        'sectionGap': '24px',
        'sidebarWidth': '220px',
    },
    'typography': {
        'fontFamily': '"Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif',
    },
}

STATIC_FILES = {
    'src/App.vue': """<template>
  <div class="app-shell" data-theme="stable_enterprise">
    <RouterView />
  </div>
</template>
""",
    'src/main.ts': """import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import { router } from './router'
import './theme/theme.css'

createApp(App).use(createPinia()).use(router).mount('#app')
""",
    'src/router/index.ts': """import { createRouter, createWebHistory } from 'vue-router'

export const router = createRouter({
  history: createWebHistory(),
  routes: [],
})
""",
    'src/theme/tokens.ts': """export const defaultTheme = {
  themeId: 'stable_enterprise',
  color: {
    bgCanvas: '#f6f8fb',
    bgSurface: '#ffffff',
    textPrimary: '#1e293b',
    textSecondary: '#475569',
    border: '#d9e2ec',
    primary: '#175cd3',
  },
}
""",
    'src/theme/theme.css': """:root {
  --color-bg-canvas: #f6f8fb;
  --color-bg-surface: #ffffff;
  --color-text-primary: #1e293b;
  --color-text-secondary: #475569;
  --color-border: #d9e2ec;
  --color-primary: #175cd3;
  --layout-sidebar-width: 220px;
}

body {
  margin: 0;
  background: var(--color-bg-canvas);
  color: var(--color-text-primary);
  font-family: "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
}
""",
    'package.json': '// TODO\n',
    'vite.config.ts': '// TODO\n',
}


def load_theme(theme_path: str | None) -> dict:
    if not theme_path:
        return DEFAULT_THEME
    source = Path(theme_path)
    if not source.exists():
        raise FileNotFoundError(f'theme file not found: {source}')
    data = json.loads(source.read_text(encoding='utf-8'))
    merged = json.loads(json.dumps(DEFAULT_THEME))
    for section in ['color', 'radius', 'shadow', 'density', 'typography']:
        merged.setdefault(section, {})
        merged[section].update(data.get(section, {}))
    for key in ['themeId', 'themeName', 'philosophy', 'fitFor', 'components', 'banned']:
        if key in data:
            merged[key] = data[key]
    return merged


def build_tokens_ts(theme: dict) -> str:
    return (
        "export const defaultTheme = "
        + json.dumps(theme, ensure_ascii=False, indent=2)
        + " as const\n"
    )


def build_theme_css(theme: dict) -> str:
    color = theme['color']
    radius = theme['radius']
    shadow = theme['shadow']
    density = theme['density']
    font_family = theme.get('typography', {}).get(
        'fontFamily',
        '"Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif',
    )
    return f""":root {{
  --color-bg-canvas: {color['bgCanvas']};
  --color-bg-surface: {color['bgSurface']};
  --color-bg-muted: {color.get('bgMuted', color['bgSurface'])};
  --color-text-primary: {color['textPrimary']};
  --color-text-secondary: {color['textSecondary']};
  --color-text-muted: {color.get('textMuted', color['textSecondary'])};
  --color-border: {color['border']};
  --color-primary: {color['primary']};
  --color-accent: {color.get('accent', color['primary'])};
  --color-success: {color.get('success', color['primary'])};
  --color-warning: {color.get('warning', color['primary'])};
  --color-danger: {color.get('danger', color['primary'])};

  --radius-panel: {radius['panel']};
  --radius-card: {radius['card']};
  --radius-control: {radius['control']};

  --shadow-panel: {shadow['panel']};
  --shadow-card: {shadow['card']};

  --layout-max-width: {density['pageMaxWidth']};
  --layout-grid-gap: {density['gridGap']};
  --layout-section-gap: {density['sectionGap']};
  --layout-sidebar-width: {density.get('sidebarWidth', '220px')};
}}

body {{
  margin: 0;
  background: var(--color-bg-canvas);
  color: var(--color-text-primary);
  font-family: {font_family};
}}
"""


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('prototype-app')
    theme_path = sys.argv[2] if len(sys.argv) > 2 else None
    theme = load_theme(theme_path)
    for item in DEFAULT_DIRS:
        (target / item).mkdir(parents=True, exist_ok=True)
    files = dict(STATIC_FILES)
    files['src/App.vue'] = files['src/App.vue'].replace('stable_enterprise', theme['themeId'])
    files['src/theme/tokens.ts'] = build_tokens_ts(theme)
    files['src/theme/theme.css'] = build_theme_css(theme)
    for rel, content in files.items():
        file_path = target / rel
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if not file_path.exists():
            file_path.write_text(content, encoding='utf-8')
    print(f'[OK] initialized vue prototype scaffold at {target} with theme {theme["themeId"]}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
