# Data Command

## Overview
Data Command is a design system created for dispatch-center, supervision-dashboard. Make the dashboard feel operational and action-oriented without turning it into a noisy command center. The system should support dashboards, lists, detail pages, forms, and workflow timelines without losing consistency or readability.

## Colors
- **Primary** (#0F5CDD): Main actions, active states, links, key highlights
- **Primary Hover** (#0F5CDD): Hover state for primary interactive elements
- **Secondary** (#334155): Supporting actions, metadata accents, secondary emphasis
- **Accent** (#0F766E): Reserved for key emphasis areas, hero moments, or branded highlights
- **Background** (#F2F5F9): Page background or app canvas
- **Surface** (#FFFFFF): Cards, panels, modals, and raised surfaces
- **Text Primary** (#0F172A): Headings, body text, key labels
- **Text Secondary** (#334155): Descriptions, helper text, metadata, timestamps
- **Border** (#CBD5E1): Dividers, card borders, input borders, neutral separators
- **Success** (#0F9F6E): Positive states, published or completed indicators
- **Warning** (#C2410C): Pending, caution, reminder, timeout, or review states
- **Error** (#C81E1E): Validation errors, destructive actions, rejected states
- **Info** (#64748B): Informational badges, neutral notices, supporting signals

## Typography
- **Display Font**: "DIN Alternate", "Source Han Sans SC", "PingFang SC", sans-serif
- **Body Font**: "DIN Alternate", "Source Han Sans SC", "PingFang SC", sans-serif
- **Code Font**: JetBrains Mono or another compact monospace for code-like data if needed

Typography should feel deliberate, calm, and readable. Display text should establish tone and hierarchy, while body text should preserve information density for business scenarios. The relationship between display and body styles should reinforce the selected theme rather than compete with the data.

Type scale: Display 32px/1.2/700, Headline 24px/1.3/700, Section heading 18px/1.35/700, Body 14px/1.6/400, Caption 12px/1.45/500.

## Spacing
- Base unit: 4px
- Scale: 4px, 8px, 12px, 16px, 18px, 20px
- Component padding: small 8x12, medium 10x16, large 12x24
- Section spacing: 20px
- Container max width: 1480px
- Grid gap: 18px

## Border Radius
- 8px: Buttons, inputs, compact controls
- 10px: Cards, list containers, lightweight panels
- 12px: Hero blocks, summary containers, larger sections
- 9999px: Pills, chips, badges, status dots

## Elevation
Elevation should remain controlled and purposeful. Panels use 0 12px 26px rgba(15, 23, 42, 0.08) while cards use 0 6px 16px rgba(15, 23, 42, 0.06). Hover and focus states should create feedback without turning the interface into a decorative system. Avoid sci-fi neon, dense full-width tables with no breathing room, decorative charts without operational meaning.

## Components
- **Buttons**: Use the primary color for the main call to action, keep secondary actions quieter, and preserve clear interaction hierarchy.
- **Cards**: Panels and cards should feel consistent with the theme's density and elevation system, using 10px radius as the standard card shape.
- **Inputs**: Keep borders subtle, focus states explicit, and placeholder text recessive. Error states should be semantic and immediately scannable.
- **Chips / Tags / Status Badges**: Use compact rounded badges for metadata and semantic states. Status color should support scanning rather than decoration.
- **Navigation**: Navigation should foreground orientation and active state while staying visually quieter than the content itself.
- **Search / Filters**: Search and filters should support fast list scanning and should not dominate the page unless discovery is the primary task.
- **Tables / Lists**: Lists should maintain clear row rhythm, restrained dividers, and highly legible state markers.
- **Hero Sections**: Hero should look like a mission status board with metric emphasis.
- **KPI Cards**: Cards may use stronger colored top bars or side accents.
- **Detail Panels**: Keep status, SLA and next action visible above the fold.
- **Forms**: Use section dividers and completion hints to reduce friction.
- **Workflow / Timeline**: Highlight bottlenecks and delayed nodes with status color.

## Layout Guidance
- **Dashboard**: Keep the summary and critical metrics above the fold, then move into risks, queues, and supporting analysis.
- **List Pages**: Prioritize scanability, status recognition, and action hierarchy before ornamental layout variation.
- **Detail Pages**: Start with object identity, state, and next action, then move into supporting sections and history.
- **Form Pages**: Group related fields, keep action buttons stable, and make validation language concrete rather than generic.
- **Workflow Pages**: Show progression, blockers, and timestamps with enough contrast that the current step is unmistakable.

## Animations
Motion should exist to reinforce hierarchy and interaction feedback. Use subtle hover lift, focus emphasis, and state transitions where they improve clarity. Keep motion restrained in dense business contexts and avoid sci-fi neon, dense full-width tables with no breathing room, decorative charts without operational meaning.

## Do's and Don'ts
- Do use #0F5CDD for primary interactive emphasis.
- Do keep spacing and component density aligned with the chosen theme.
- Do maintain consistent radius and elevation across related surfaces.
- Do make semantic states immediately scannable in lists, detail views, and timelines.
- Do preserve business readability even when pursuing a distinctive visual tone.
- Don't use #0F5CDD as decorative filler outside meaningful interactive or emphasis contexts.
- Don't mix multiple unrelated visual moods on the same screen.
- Don't let hero areas overpower the actual business content.
- Don't create new ad hoc component styles when an existing pattern already fits.
- Don't introduce sci-fi neon, dense full-width tables with no breathing room, decorative charts without operational meaning.
