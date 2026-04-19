<template>
  <div v-if="item">
    <PageHeader :title="item.title" :subtitle="item.id">
      <StatusBadge :label="item.status" />
      <button class="button ghost">催办协同部门</button>
    </PageHeader>
    <div class="split">
      <div class="section">
        <div class="section-head">
          <div>
            <h2>申请内容</h2>
            <div class="section-subtitle">用于演示巡组向巡办提请横向协同的申请信息。</div>
          </div>
        </div>
        <div class="kv">
          <div>申请人</div><div>{{ item.requester }}</div>
          <div>协同部门</div><div>{{ item.targetDepartment }}</div>
          <div>状态</div><div><StatusBadge :label="item.status" /></div>
          <div>说明</div><div>{{ item.content }}</div>
        </div>
      </div>
      <div class="section">
        <div class="section-head">
          <div>
            <h2>流转时间轴</h2>
            <div class="section-subtitle">用于演示巡办转办和部门接收的过程。</div>
          </div>
        </div>
        <ul class="timeline">
          <li v-for="row in item.timeline" :key="row.at + row.action">
            <div class="timeline-title">{{ row.action }}</div>
            <div class="timeline-meta">{{ row.at }}｜{{ row.actor }}</div>
            <div>{{ row.note }}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <EmptyState v-else icon="🤝" title="未找到对应协助申请" description="请从协助申请列表重新进入。" />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { repository } from '@/services/api/repository'
import StatusBadge from '@/components/common/StatusBadge.vue'
import PageHeader from '@/components/common/PageHeader.vue'
import EmptyState from '@/components/common/EmptyState.vue'
const route = useRoute()
const item = computed(() => repository.getAssist(String(route.params.id)))
</script>
