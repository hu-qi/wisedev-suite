<template>
  <div v-if="item">
    <PageHeader :title="item.title" :subtitle="item.id">
      <span class="meta-pill">{{ item.confirmStatus }}</span>
    </PageHeader>
    <div class="section">
      <div class="kv">
        <div>开始时间</div><div>{{ item.startAt }}</div>
        <div>确认情况</div><div>{{ item.confirmStatus }}</div>
        <div>会议主题</div><div>{{ item.content }}</div>
      </div>
    </div>
  </div>
  <EmptyState v-else icon="📅" title="未找到对应会议通知" description="请从会议通知列表重新进入。" />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { repository } from '@/services/api/repository'
import PageHeader from '@/components/common/PageHeader.vue'
import EmptyState from '@/components/common/EmptyState.vue'
const route = useRoute()
const item = computed(() => repository.getMeeting(String(route.params.id)))
</script>
