<template>
  <PageHeader title="调度指令列表" subtitle="展示指令状态、密级、目标巡组数、截止时间与后续操作入口。">
    <span class="meta-pill">当前共 {{ filtered.length }} 条</span>
  </PageHeader>

  <div class="filter-panel">
    <div class="toolbar">
      <input class="toolbar-grow" v-model="keyword" placeholder="按编号或标题搜索调度指令" />
      <select v-model="status">
        <option value="">全部状态</option>
        <option value="OVERDUE">逾期</option>
        <option value="IN_PROGRESS">办理中</option>
        <option value="COMPLETED">已办结</option>
      </select>
      <select v-model="securityLevel">
        <option value="">全部密级</option>
        <option value="绝密">绝密</option>
        <option value="机密">机密</option>
      </select>
    </div>
  </div>

  <div class="notice-panel warning" v-if="filtered.some((item) => item.status === 'OVERDUE')">
    <div class="notice-title">当前存在逾期事项</div>
    <div class="notice-desc">建议优先查看逾期事项详情页，演示催办、提醒和升级预警动作。</div>
  </div>

  <div class="section">
    <div class="table-wrap">
      <table class="table">
        <thead>
          <tr>
            <th>编号</th>
            <th>标题</th>
            <th>密级</th>
            <th>目标巡组</th>
            <th>截止时间</th>
            <th>状态</th>
            <th>最近更新时间</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in filtered" :key="item.id">
            <td>{{ item.id }}</td>
            <td>
              <div class="table-title">{{ item.title }}</div>
              <div class="table-desc">{{ item.content }}</div>
            </td>
            <td><span class="meta-pill">{{ item.securityLevel }}</span></td>
            <td>{{ item.targetGroupCount }} 个</td>
            <td>{{ item.dueAt }}</td>
            <td><StatusBadge :label="item.status" /></td>
            <td>{{ item.updatedAt }}</td>
            <td class="table-ops">
              <RouterLink class="link-button" :to="`/dispatch-orders/${item.id}`">查看详情</RouterLink>
            </td>
          </tr>
          <tr v-if="filtered.length === 0">
            <td colspan="8">
              <EmptyState icon="🔎" title="暂无符合条件的调度指令" description="请清空筛选条件，或切换演示场景后重试。" />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { repository } from '@/services/api/repository'
import StatusBadge from '@/components/common/StatusBadge.vue'
import PageHeader from '@/components/common/PageHeader.vue'
import EmptyState from '@/components/common/EmptyState.vue'

const keyword = ref('')
const status = ref('')
const securityLevel = ref('')
const rows = repository.listDispatchOrders()

const filtered = computed(() => rows.filter((item) => {
  const matchKeyword = !keyword.value || item.title.includes(keyword.value) || item.id.includes(keyword.value)
  const matchStatus = !status.value || item.status === status.value
  const matchSecurity = !securityLevel.value || item.securityLevel === securityLevel.value
  return matchKeyword && matchStatus && matchSecurity
}))
</script>
