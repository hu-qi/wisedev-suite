#!/usr/bin/env python3
"""Render a DESIGN.md document from a theme JSON file."""
from __future__ import annotations

import json
from pathlib import Path
import sys


DEFAULT_FIT = "enterprise-facing dashboards, lists, detail pages, forms, and workflow timelines"


def parse_args(argv: list[str]) -> tuple[Path, Path | None]:
    if not argv:
        print("usage: render_design_md.py <theme.json> [output.md]")
        raise SystemExit(1)
    source = Path(argv[0])
    target = Path(argv[1]) if len(argv) > 1 else None
    return source, target


def load_theme(path: Path) -> dict:
    if not path.exists():
        print(f"[ERROR] theme file not found: {path}")
        raise SystemExit(1)
    return json.loads(path.read_text(encoding="utf-8"))


def infer_overview(theme: dict) -> str:
    name = theme.get("themeName", theme.get("themeId", "Theme"))
    fit_for = ", ".join(theme.get("fitFor", [])) or DEFAULT_FIT
    philosophy = theme.get("philosophy", "A structured design system for AI-assisted product delivery.")
    return (
        f"{name} is a design system created for {fit_for}. "
        f"{philosophy} The system should support dashboards, lists, detail pages, forms, "
        f"and workflow timelines without losing consistency or readability."
    )


def render_colors(theme: dict) -> str:
    color = theme["color"]
    lines = [
        f"- **Primary** ({color['primary']}): Main actions, active states, links, key highlights",
        f"- **Primary Hover** ({color['primary']}): Hover state for primary interactive elements",
        f"- **Secondary** ({color['textSecondary']}): Supporting actions, metadata accents, secondary emphasis",
        f"- **Accent** ({color['accent']}): Reserved for key emphasis areas, hero moments, or branded highlights",
        f"- **Background** ({color['bgCanvas']}): Page background or app canvas",
        f"- **Surface** ({color['bgSurface']}): Cards, panels, modals, and raised surfaces",
        f"- **Text Primary** ({color['textPrimary']}): Headings, body text, key labels",
        f"- **Text Secondary** ({color['textSecondary']}): Descriptions, helper text, metadata, timestamps",
        f"- **Border** ({color['border']}): Dividers, card borders, input borders, neutral separators",
        f"- **Success** ({color['success']}): Positive states, published or completed indicators",
        f"- **Warning** ({color['warning']}): Pending, caution, reminder, timeout, or review states",
        f"- **Error** ({color['danger']}): Validation errors, destructive actions, rejected states",
        f"- **Info** ({color.get('textMuted', color['textSecondary'])}): Informational badges, neutral notices, supporting signals",
    ]
    return "\n".join(lines)


def render_typography(theme: dict) -> str:
    typo = theme.get("typography", {})
    font = typo.get("fontFamily", '"Source Han Sans SC", "PingFang SC", sans-serif')
    return "\n".join([
        f"- **Display Font**: {font}",
        f"- **Body Font**: {font}",
        "- **Code Font**: JetBrains Mono or another compact monospace for code-like data if needed",
        "",
        "Typography should feel deliberate, calm, and readable. Display text should establish tone and hierarchy, "
        "while body text should preserve information density for business scenarios. The relationship between "
        "display and body styles should reinforce the selected theme rather than compete with the data.",
        "",
        "Type scale: "
        f"Display {typo.get('heroTitle', '[size]')}, "
        f"Headline {typo.get('pageTitle', '[size]')}, "
        f"Section heading {typo.get('sectionTitle', '[size]')}, "
        f"Body {typo.get('body', '[size]')}, "
        f"Caption {typo.get('caption', '[size]')}.",
    ])


def render_spacing(theme: dict) -> str:
    density = theme.get("density", {})
    return "\n".join([
        "- Base unit: 4px",
        f"- Scale: 4px, 8px, 12px, 16px, {density.get('gridGap', '20px')}, {density.get('sectionGap', '24px')}",
        "- Component padding: small 8x12, medium 10x16, large 12x24",
        f"- Section spacing: {density.get('sectionGap', '24px')}",
        f"- Container max width: {density.get('pageMaxWidth', '1440px')}",
        f"- Grid gap: {density.get('gridGap', '20px')}",
    ])


def render_radius(theme: dict) -> str:
    radius = theme.get("radius", {})
    return "\n".join([
        f"- {radius.get('control', '10px')}: Buttons, inputs, compact controls",
        f"- {radius.get('card', '12px')}: Cards, list containers, lightweight panels",
        f"- {radius.get('panel', '14px')}: Hero blocks, summary containers, larger sections",
        "- 9999px: Pills, chips, badges, status dots",
    ])


def render_elevation(theme: dict) -> str:
    shadow = theme.get("shadow", {})
    banned = ", ".join(theme.get("banned", [])) or "visual noise and decorative excess"
    return (
        "Elevation should remain controlled and purposeful. Panels use "
        f"{shadow.get('panel', '[panel shadow]')} while cards use {shadow.get('card', '[card shadow]')}. "
        "Hover and focus states should create feedback without turning the interface into a decorative system. "
        f"Avoid {banned}."
    )


def render_components(theme: dict) -> str:
    comp = theme.get("components", {})
    return "\n".join([
        f"- **Buttons**: Use the primary color for the main call to action, keep secondary actions quieter, and preserve clear interaction hierarchy.",
        f"- **Cards**: Panels and cards should feel consistent with the theme's density and elevation system, using {theme.get('radius', {}).get('card', '12px')} radius as the standard card shape.",
        "- **Inputs**: Keep borders subtle, focus states explicit, and placeholder text recessive. Error states should be semantic and immediately scannable.",
        "- **Chips / Tags / Status Badges**: Use compact rounded badges for metadata and semantic states. Status color should support scanning rather than decoration.",
        "- **Navigation**: Navigation should foreground orientation and active state while staying visually quieter than the content itself.",
        "- **Search / Filters**: Search and filters should support fast list scanning and should not dominate the page unless discovery is the primary task.",
        "- **Tables / Lists**: Lists should maintain clear row rhythm, restrained dividers, and highly legible state markers.",
        f"- **Hero Sections**: {comp.get('hero', 'Use a summary-first hero that balances context, metrics, and action.')}",
        f"- **KPI Cards**: {comp.get('kpiCard', 'Use value-first KPI cards with concise labels and restrained emphasis.')}",
        f"- **Detail Panels**: {comp.get('detail', 'Detail panels should bring identity, status, and next action above the fold.')}",
        f"- **Forms**: {comp.get('form', 'Forms should group fields clearly and keep helper text and validation explicit.')}",
        f"- **Workflow / Timeline**: {comp.get('timeline', 'Timelines should make the current state and exceptions obvious at a glance.')}",
    ])


def render_layout_guidance() -> str:
    return "\n".join([
        "- **Dashboard**: Keep the summary and critical metrics above the fold, then move into risks, queues, and supporting analysis.",
        "- **List Pages**: Prioritize scanability, status recognition, and action hierarchy before ornamental layout variation.",
        "- **Detail Pages**: Start with object identity, state, and next action, then move into supporting sections and history.",
        "- **Form Pages**: Group related fields, keep action buttons stable, and make validation language concrete rather than generic.",
        "- **Workflow Pages**: Show progression, blockers, and timestamps with enough contrast that the current step is unmistakable.",
    ])


def render_animations(theme: dict) -> str:
    banned = ", ".join(theme.get("banned", [])) or "excessive decorative motion"
    return (
        "Motion should exist to reinforce hierarchy and interaction feedback. Use subtle hover lift, focus emphasis, "
        "and state transitions where they improve clarity. Keep motion restrained in dense business contexts and avoid "
        f"{banned}."
    )


def render_dos_and_donts(theme: dict) -> str:
    color = theme["color"]
    banned = theme.get("banned", [])
    dos = [
        f"Do use {color['primary']} for primary interactive emphasis.",
        "Do keep spacing and component density aligned with the chosen theme.",
        "Do maintain consistent radius and elevation across related surfaces.",
        "Do make semantic states immediately scannable in lists, detail views, and timelines.",
        "Do preserve business readability even when pursuing a distinctive visual tone.",
    ]
    donts = [
        f"Don't use {color['primary']} as decorative filler outside meaningful interactive or emphasis contexts.",
        "Don't mix multiple unrelated visual moods on the same screen.",
        "Don't let hero areas overpower the actual business content.",
        "Don't create new ad hoc component styles when an existing pattern already fits.",
        f"Don't introduce {', '.join(banned) if banned else 'visual effects that weaken clarity'}.",
    ]
    return "\n".join([*(f"- {item}" for item in dos), *(f"- {item}" for item in donts)])


def render_design_md(theme: dict) -> str:
    name = theme.get("themeName", theme.get("themeId", "Theme"))
    sections = [
        f"# {name}",
        "",
        "## Overview",
        infer_overview(theme),
        "",
        "## Colors",
        render_colors(theme),
        "",
        "## Typography",
        render_typography(theme),
        "",
        "## Spacing",
        render_spacing(theme),
        "",
        "## Border Radius",
        render_radius(theme),
        "",
        "## Elevation",
        render_elevation(theme),
        "",
        "## Components",
        render_components(theme),
        "",
        "## Layout Guidance",
        render_layout_guidance(),
        "",
        "## Animations",
        render_animations(theme),
        "",
        "## Do's and Don'ts",
        render_dos_and_donts(theme),
        "",
    ]
    return "\n".join(sections)


def main() -> int:
    source, target = parse_args(sys.argv[1:])
    theme = load_theme(source)
    content = render_design_md(theme)
    if target is None:
        print(content)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        print(f"[OK] wrote DESIGN.md to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
