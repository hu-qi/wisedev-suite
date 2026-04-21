# Enterprise Calm

## Overview
Enterprise Calm is a design system created for leadership-review, government-enterprise-demo. Present business facts with restraint, hierarchy and a stable visual cadence that supports trust. The system should support dashboards, lists, detail pages, forms, and workflow timelines without losing consistency or readability.

## Colors
- **Primary** (#175CD3): Main actions, active states, links, key highlights
- **Primary Hover** (#175CD3): Hover state for primary interactive elements
- **Secondary** (#475569): Supporting actions, metadata accents, secondary emphasis
- **Accent** (#0F766E): Reserved for key emphasis areas, hero moments, or branded highlights
- **Background** (#F6F8FB): Page background or app canvas
- **Surface** (#FFFFFF): Cards, panels, modals, and raised surfaces
- **Text Primary** (#1E293B): Headings, body text, key labels
- **Text Secondary** (#475569): Descriptions, helper text, metadata, timestamps
- **Border** (#D9E2EC): Dividers, card borders, input borders, neutral separators
- **Success** (#15803D): Positive states, published or completed indicators
- **Warning** (#B45309): Pending, caution, reminder, timeout, or review states
- **Error** (#B42318): Validation errors, destructive actions, rejected states
- **Info** (#64748B): Informational badges, neutral notices, supporting signals

## Typography
- **Display Font**: "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif
- **Body Font**: "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif
- **Code Font**: JetBrains Mono or another compact monospace for code-like data if needed

Typography should feel deliberate, calm, and readable. Display text should establish tone and hierarchy, while body text should preserve information density for business scenarios. The relationship between display and body styles should reinforce the selected theme rather than compete with the data.

Type scale: Display 30px/1.25/700, Headline 24px/1.35/700, Section heading 18px/1.4/600, Body 14px/1.65/400, Caption 12px/1.5/400.

## Spacing
- Base unit: 4px
- Scale: 4px, 8px, 12px, 16px, 20px, 24px
- Component padding: small 8x12, medium 10x16, large 12x24
- Section spacing: 24px
- Container max width: 1440px
- Grid gap: 20px

## Border Radius
- 10px: Buttons, inputs, compact controls
- 12px: Cards, list containers, lightweight panels
- 14px: Hero blocks, summary containers, larger sections
- 9999px: Pills, chips, badges, status dots

## Elevation
Elevation should remain controlled and purposeful. Panels use 0 10px 24px rgba(15, 23, 42, 0.06) while cards use 0 6px 18px rgba(15, 23, 42, 0.05). Hover and focus states should create feedback without turning the interface into a decorative system. Avoid full dark mode, glow effects, oversized gradients.

## Components
- **Buttons**: Use the primary color for the main call to action, keep secondary actions quieter, and preserve clear interaction hierarchy.
- **Cards**: Panels and cards should feel consistent with the theme's density and elevation system, using 12px radius as the standard card shape.
- **Inputs**: Keep borders subtle, focus states explicit, and placeholder text recessive. Error states should be semantic and immediately scannable.
- **Chips / Tags / Status Badges**: Use compact rounded badges for metadata and semantic states. Status color should support scanning rather than decoration.
- **Navigation**: Navigation should foreground orientation and active state while staying visually quieter than the content itself.
- **Search / Filters**: Search and filters should support fast list scanning and should not dominate the page unless discovery is the primary task.
- **Tables / Lists**: Lists should maintain clear row rhythm, restrained dividers, and highly legible state markers.
- **Hero Sections**: Wide and calm; summary copy should stay within two short paragraphs.
- **KPI Cards**: Four-card grid with compact trend indicators.
- **Detail Panels**: Top summary card followed by timeline and notes columns.
- **Forms**: Two-column sections with explicit helper text.
- **Workflow / Timeline**: Neutral axis with one strong current-state marker.

## Layout Guidance
- **Dashboard**: Keep the summary and critical metrics above the fold, then move into risks, queues, and supporting analysis.
- **List Pages**: Prioritize scanability, status recognition, and action hierarchy before ornamental layout variation.
- **Detail Pages**: Start with object identity, state, and next action, then move into supporting sections and history.
- **Form Pages**: Group related fields, keep action buttons stable, and make validation language concrete rather than generic.
- **Workflow Pages**: Show progression, blockers, and timestamps with enough contrast that the current step is unmistakable.

## Animations
Motion should exist to reinforce hierarchy and interaction feedback. Use subtle hover lift, focus emphasis, and state transitions where they improve clarity. Keep motion restrained in dense business contexts and avoid full dark mode, glow effects, oversized gradients.

## Do's and Don'ts
- Do use #175CD3 for primary interactive emphasis.
- Do keep spacing and component density aligned with the chosen theme.
- Do maintain consistent radius and elevation across related surfaces.
- Do make semantic states immediately scannable in lists, detail views, and timelines.
- Do preserve business readability even when pursuing a distinctive visual tone.
- Don't use #175CD3 as decorative filler outside meaningful interactive or emphasis contexts.
- Don't mix multiple unrelated visual moods on the same screen.
- Don't let hero areas overpower the actual business content.
- Don't create new ad hoc component styles when an existing pattern already fits.
- Don't introduce full dark mode, glow effects, oversized gradients.
