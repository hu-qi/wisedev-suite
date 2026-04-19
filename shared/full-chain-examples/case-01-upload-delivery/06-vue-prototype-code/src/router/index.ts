import { createRouter, createWebHistory } from 'vue-router'
import ConsoleLayout from '@/layouts/ConsoleLayout.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: ConsoleLayout,
      children: [
        { path: '', redirect: '/dashboard' },
        { path: 'dashboard', component: () => import('@/views/DashboardView.vue') },
        { path: 'dispatch-orders', component: () => import('@/views/DispatchOrderListView.vue') },
        { path: 'dispatch-orders/:id', component: () => import('@/views/DispatchOrderDetailView.vue') },
        { path: 'group-reports', component: () => import('@/views/GroupReportListView.vue') },
        { path: 'group-reports/new', component: () => import('@/views/GroupReportCreateView.vue') },
        { path: 'group-reports/:id', component: () => import('@/views/GroupReportDetailView.vue') },
        { path: 'assist-requests', component: () => import('@/views/AssistRequestListView.vue') },
        { path: 'assist-requests/:id', component: () => import('@/views/AssistRequestDetailView.vue') },
        { path: 'meetings', component: () => import('@/views/MeetingListView.vue') },
        { path: 'meetings/:id', component: () => import('@/views/MeetingDetailView.vue') },
        { path: 'audit-logs', component: () => import('@/views/AuditLogView.vue') },
      ],
    },
  ],
})

export default router
