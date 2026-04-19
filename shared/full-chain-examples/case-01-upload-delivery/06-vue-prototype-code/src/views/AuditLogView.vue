<template>
  <PageHeader title="审计摘要" subtitle="汇总关键模块动作，支持从业务演示切回全链路追溯。">
    <span class="meta-pill">{{ rows.length }} 条关键动作</span>
  </PageHeader>
  <div class="section">
    <div class="table-wrap">
      <table class="table">
        <thead><tr><th>时间</th><th>模块</th><th>动作</th><th>操作人</th><th>摘要</th></tr></thead>
        <tbody>
          <tr v-for="item in rows" :key="item.id">
            <td>{{ item.at }}</td>
            <td>{{ item.module }}</td>
            <td><span class="meta-pill">{{ item.action }}</span></td>
            <td>{{ item.actor }}</td>
            <td>{{ item.summary }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { repository } from '@/services/api/repository'
import PageHeader from '@/components/common/PageHeader.vue'
const rows = repository.listAuditLogs()
</script>
