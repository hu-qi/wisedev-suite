<template>
  <div v-if="item">
    <PageHeader :title="item.title" :subtitle="item.id">
      <StatusBadge :label="item.status" />
      <button class="button ghost">查看附件目录</button>
      <button class="button secondary" v-if="item.returnComment">模拟重提</button>
    </PageHeader>

    <div class="hero-banner">
      <div class="hero-panel">
        <div class="hero-title">报表主信息</div>
        <div class="hero-desc">用于展示巡组本周工作推进、发现问题与问题报表补正状态。</div>
        <div class="hero-metrics">
          <span class="hero-chip">巡组 {{ item.groupName }}</span>
          <span class="hero-chip">周期 {{ item.period }}</span>
          <span class="hero-chip">版本 {{ item.versions.length }} 个</span>
        </div>
      </div>
      <div class="hero-panel">
        <div class="section-head"><h2>退回与补正提示</h2></div>
        <div v-if="item.returnComment" class="notice-panel warning" style="margin:0;">
          <div class="notice-title">当前存在退回意见</div>
          <div class="notice-desc">{{ item.returnComment }}</div>
        </div>
        <div v-else class="notice-panel info" style="margin:0;">
          <div class="notice-title">当前无退回意见</div>
          <div class="notice-desc">适合演示已正常上报并归档的标准路径。</div>
        </div>
      </div>
    </div>

    <div class="split">
      <div class="section">
        <div class="section-head">
          <div>
            <h2>当前版本内容</h2>
            <div class="section-subtitle">高保真原型中用摘要文本替代富文本正文与附件区。</div>
          </div>
        </div>
        <div class="kv">
          <div>报表编号</div><div>{{ item.id }}</div>
          <div>巡组名称</div><div>{{ item.groupName }}</div>
          <div>状态</div><div><StatusBadge :label="item.status" /></div>
          <div>更新时间</div><div>{{ item.updatedAt }}</div>
          <div>正文摘要</div><div>{{ item.content }}</div>
        </div>
      </div>

      <div class="section">
        <div class="section-head">
          <div>
            <h2>版本链</h2>
            <div class="section-subtitle">演示首次提交、退回补正、再次提交的历史轨迹。</div>
          </div>
        </div>
        <ul class="timeline">
          <li v-for="ver in item.versions" :key="ver.version + ver.at">
            <div class="timeline-title">{{ ver.version }}</div>
            <div class="timeline-meta">{{ ver.at }}｜{{ ver.operator }}</div>
            <div>{{ ver.note }}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <EmptyState v-else icon="📝" title="未找到对应报表" description="请从周报上报列表重新进入。" />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { repository } from '@/services/api/repository'
import PageHeader from '@/components/common/PageHeader.vue'
import StatusBadge from '@/components/common/StatusBadge.vue'
import EmptyState from '@/components/common/EmptyState.vue'

const route = useRoute()
const item = computed(() => repository.getReport(String(route.params.id)))
</script>
