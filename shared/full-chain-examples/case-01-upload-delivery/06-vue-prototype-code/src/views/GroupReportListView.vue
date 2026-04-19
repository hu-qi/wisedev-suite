<template>
  <PageHeader title="周报上报列表" subtitle="展示巡组上报状态、版本链和被退回后的补正情况。">
    <RouterLink to="/group-reports/new" class="button">新建周报</RouterLink>
  </PageHeader>

  <div class="filter-panel">
    <div class="toolbar">
      <input class="toolbar-grow" v-model="keyword" placeholder="按标题、编号或巡组名称搜索" />
      <select v-model="status">
        <option value="">全部状态</option>
        <option value="SUBMITTED">已提交</option>
        <option value="RETURNED">已退回</option>
        <option value="RESUBMITTED">已重提</option>
      </select>
    </div>
  </div>

  <div class="notice-panel warning" v-if="filtered.some((item) => item.status === 'RETURNED')">
    <div class="notice-title">存在被退回的报表</div>
    <div class="notice-desc">建议进入详情页演示退回意见、版本链和再次提交流程。</div>
  </div>

  <div class="section">
    <div class="table-wrap">
      <table class="table">
        <thead>
          <tr><th>编号</th><th>标题</th><th>巡组</th><th>周期</th><th>状态</th><th>更新时间</th><th>版本数</th><th>操作</th></tr>
        </thead>
        <tbody>
          <tr v-for="item in filtered" :key="item.id">
            <td>{{ item.id }}</td>
            <td>
              <div class="table-title">{{ item.title }}</div>
              <div class="table-desc">{{ item.content }}</div>
            </td>
            <td>{{ item.groupName }}</td>
            <td>{{ item.period }}</td>
            <td><StatusBadge :label="item.status" /></td>
            <td>{{ item.updatedAt }}</td>
            <td>{{ item.versions.length }}</td>
            <td><RouterLink class="link-button" :to="`/group-reports/${item.id}`">查看详情</RouterLink></td>
          </tr>
          <tr v-if="filtered.length === 0">
            <td colspan="8"><EmptyState icon="🗂" title="暂无符合条件的周报" description="可切换场景后再次查看。" /></td>
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
const rows = repository.listReports()

const filtered = computed(() => rows.filter((item) => {
  const matchKeyword = !keyword.value || item.title.includes(keyword.value) || item.id.includes(keyword.value) || item.groupName.includes(keyword.value)
  const matchStatus = !status.value || item.status === status.value
  return matchKeyword && matchStatus
}))
</script>
