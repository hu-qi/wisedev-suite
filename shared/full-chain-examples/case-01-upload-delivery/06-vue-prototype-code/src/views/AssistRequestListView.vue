<template>
  <PageHeader title="协助申请列表" subtitle="展示跨部门协同申请的状态、流转部门与办结情况。">
    <span class="meta-pill">未结事项 {{ openCount }}</span>
  </PageHeader>

  <div class="section">
    <div class="table-wrap">
      <table class="table">
        <thead><tr><th>编号</th><th>标题</th><th>申请人</th><th>协同部门</th><th>状态</th><th>更新时间</th><th>操作</th></tr></thead>
        <tbody>
          <tr v-for="item in rows" :key="item.id">
            <td>{{ item.id }}</td>
            <td>
              <div class="table-title">{{ item.title }}</div>
              <div class="table-desc">{{ item.content }}</div>
            </td>
            <td>{{ item.requester }}</td>
            <td>{{ item.targetDepartment }}</td>
            <td><StatusBadge :label="item.status" /></td>
            <td>{{ item.updatedAt }}</td>
            <td><RouterLink class="link-button" :to="`/assist-requests/${item.id}`">查看详情</RouterLink></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { repository } from '@/services/api/repository'
import StatusBadge from '@/components/common/StatusBadge.vue'
import PageHeader from '@/components/common/PageHeader.vue'

const rows = repository.listAssists()
const openCount = computed(() => rows.filter((item) => item.status !== 'COMPLETED').length)
</script>
