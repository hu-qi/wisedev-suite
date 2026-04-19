<template>
  <PageHeader title="会议通知列表" subtitle="展示会议安排、确认情况与会议内容概览。" />
  <div class="section">
    <div class="table-wrap">
      <table class="table">
        <thead><tr><th>编号</th><th>标题</th><th>开始时间</th><th>确认情况</th><th>操作</th></tr></thead>
        <tbody>
          <tr v-for="item in rows" :key="item.id">
            <td>{{ item.id }}</td>
            <td>
              <div class="table-title">{{ item.title }}</div>
              <div class="table-desc">{{ item.content }}</div>
            </td>
            <td>{{ item.startAt }}</td>
            <td>{{ item.confirmStatus }}</td>
            <td><RouterLink class="link-button" :to="`/meetings/${item.id}`">查看详情</RouterLink></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { repository } from '@/services/api/repository'
import PageHeader from '@/components/common/PageHeader.vue'
const rows = repository.listMeetings()
</script>
