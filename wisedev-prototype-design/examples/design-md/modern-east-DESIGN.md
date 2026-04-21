# Modern East

## Overview
Modern East is a design system created for proposal-showcase, high-level-demo. Blend calm whitespace and precise structure to create a refined, contemporary Chinese enterprise tone. The system should support dashboards, lists, detail pages, forms, and workflow timelines without losing consistency or readability.

## Colors
- **Primary** (#8E2F2F): Main actions, active states, links, key highlights
- **Primary Hover** (#8E2F2F): Hover state for primary interactive elements
- **Secondary** (#5B5650): Supporting actions, metadata accents, secondary emphasis
- **Accent** (#355C66): Reserved for key emphasis areas, hero moments, or branded highlights
- **Background** (#F7F5F1): Page background or app canvas
- **Surface** (#FFFCF7): Cards, panels, modals, and raised surfaces
- **Text Primary** (#2B2A28): Headings, body text, key labels
- **Text Secondary** (#5B5650): Descriptions, helper text, metadata, timestamps
- **Border** (#DDD5CA): Dividers, card borders, input borders, neutral separators
- **Success** (#4D7C57): Positive states, published or completed indicators
- **Warning** (#B7791F): Pending, caution, reminder, timeout, or review states
- **Error** (#A63A3A): Validation errors, destructive actions, rejected states
- **Info** (#7A746C): Informational badges, neutral notices, supporting signals

## Typography
- **Display Font**: "Noto Serif SC", "Source Han Serif SC", "PingFang SC", serif
- **Body Font**: "Noto Serif SC", "Source Han Serif SC", "PingFang SC", serif
- **Code Font**: JetBrains Mono or another compact monospace for code-like data if needed

Typography should feel deliberate, calm, and readable. Display text should establish tone and hierarchy, while body text should preserve information density for business scenarios. The relationship between display and body styles should reinforce the selected theme rather than compete with the data.

Type scale: Display 32px/1.28/600, Headline 24px/1.38/600, Section heading 18px/1.45/600, Body 14px/1.75/400, Caption 12px/1.6/400.

## Spacing
- Base unit: 4px
- Scale: 4px, 8px, 12px, 16px, 24px, 28px
- Component padding: small 8x12, medium 10x16, large 12x24
- Section spacing: 28px
- Container max width: 1400px
- Grid gap: 24px

## Border Radius
- 10px: Buttons, inputs, compact controls
- 14px: Cards, list containers, lightweight panels
- 16px: Hero blocks, summary containers, larger sections
- 9999px: Pills, chips, badges, status dots

## Elevation
Elevation should remain controlled and purposeful. Panels use 0 10px 30px rgba(63, 47, 35, 0.08) while cards use 0 6px 18px rgba(63, 47, 35, 0.05). Hover and focus states should create feedback without turning the interface into a decorative system. Avoid heavy black backgrounds, cartoonish illustration style, over-decoration that weakens business seriousness.

## Components
- **Buttons**: Use the primary color for the main call to action, keep secondary actions quieter, and preserve clear interaction hierarchy.
- **Cards**: Panels and cards should feel consistent with the theme's density and elevation system, using 14px radius as the standard card shape.
- **Inputs**: Keep borders subtle, focus states explicit, and placeholder text recessive. Error states should be semantic and immediately scannable.
- **Chips / Tags / Status Badges**: Use compact rounded badges for metadata and semantic states. Status color should support scanning rather than decoration.
- **Navigation**: Navigation should foreground orientation and active state while staying visually quieter than the content itself.
- **Search / Filters**: Search and filters should support fast list scanning and should not dominate the page unless discovery is the primary task.
- **Tables / Lists**: Lists should maintain clear row rhythm, restrained dividers, and highly legible state markers.
- **Hero Sections**: Use more whitespace and a concise poetic summary, but keep business metrics visible.
- **KPI Cards**: Cards should feel refined, with muted backgrounds and controlled accent color.
- **Detail Panels**: Pair summary facts with contextual notes rather than dense paragraphs.
- **Forms**: Reduce field crowding and use calm helper text.
- **Workflow / Timeline**: Prefer subtle linework and label hierarchy over heavy badges.

## Layout Guidance
- **Dashboard**: Keep the summary and critical metrics above the fold, then move into risks, queues, and supporting analysis.
- **List Pages**: Prioritize scanability, status recognition, and action hierarchy before ornamental layout variation.
- **Detail Pages**: Start with object identity, state, and next action, then move into supporting sections and history.
- **Form Pages**: Group related fields, keep action buttons stable, and make validation language concrete rather than generic.
- **Workflow Pages**: Show progression, blockers, and timestamps with enough contrast that the current step is unmistakable.

## Animations
Motion should exist to reinforce hierarchy and interaction feedback. Use subtle hover lift, focus emphasis, and state transitions where they improve clarity. Keep motion restrained in dense business contexts and avoid heavy black backgrounds, cartoonish illustration style, over-decoration that weakens business seriousness.

## Do's and Don'ts
- Do use #8E2F2F for primary interactive emphasis.
- Do keep spacing and component density aligned with the chosen theme.
- Do maintain consistent radius and elevation across related surfaces.
- Do make semantic states immediately scannable in lists, detail views, and timelines.
- Do preserve business readability even when pursuing a distinctive visual tone.
- Don't use #8E2F2F as decorative filler outside meaningful interactive or emphasis contexts.
- Don't mix multiple unrelated visual moods on the same screen.
- Don't let hero areas overpower the actual business content.
- Don't create new ad hoc component styles when an existing pattern already fits.
- Don't introduce heavy black backgrounds, cartoonish illustration style, over-decoration that weakens business seriousness.
