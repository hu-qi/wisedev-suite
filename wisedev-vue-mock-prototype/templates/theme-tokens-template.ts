export type PrototypeTheme = {
  themeId: string
  color: {
    bgCanvas: string
    bgSurface: string
    bgMuted: string
    textPrimary: string
    textSecondary: string
    border: string
    primary: string
    accent: string
    success: string
    warning: string
    danger: string
  }
  radius: {
    panel: string
    card: string
    control: string
  }
  shadow: {
    panel: string
    card: string
  }
  density: {
    pageMaxWidth: string
    gridGap: string
    sectionGap: string
    sidebarWidth: string
  }
}

export const defaultTheme: PrototypeTheme = {
  themeId: 'stable_enterprise',
  color: {
    bgCanvas: '#f6f8fb',
    bgSurface: '#ffffff',
    bgMuted: '#eef3f8',
    textPrimary: '#1e293b',
    textSecondary: '#475569',
    border: '#d9e2ec',
    primary: '#175cd3',
    accent: '#0f766e',
    success: '#15803d',
    warning: '#b45309',
    danger: '#b42318',
  },
  radius: {
    panel: '14px',
    card: '12px',
    control: '10px',
  },
  shadow: {
    panel: '0 10px 24px rgba(15, 23, 42, 0.06)',
    card: '0 6px 18px rgba(15, 23, 42, 0.05)',
  },
  density: {
    pageMaxWidth: '1440px',
    gridGap: '20px',
    sectionGap: '24px',
    sidebarWidth: '220px',
  },
}
