<template>
  <div v-if="item">
    <PageHeader :title="item.title" :subtitle="item.id">
      <StatusBadge :label="item.status" />
      <button class="button ghost" v-for="action in item.actions" :key="action">{{ action }}</button>
    </PageHeader>

    <div class="hero-banner">
      <div class="hero-panel">
        <div class="hero-title">指令执行总览</div>
        <div class="hero-desc">围绕发布时间、签收进度、密级控制和阶段反馈统一展示当前调度指令的推进情况。</div>
        <div class="hero-metrics">
          <span class="hero-chip">密级 {{ item.securityLevel }}</span>
          <span class="hero-chip">目标巡组 {{ item.targetGroupCount }} 个</span>
          <span class="hero-chip">截止 {{ item.dueAt }}</span>
        </div>
      </div>
      <div class="hero-panel">
        <div class="section-head">
          <div>
            <h2>签收进度</h2>
            <div class="section-subtitle">用于模拟首页看板与详情页之间的下钻关系。</div>
          </div>
          <span class="meta-pill">{{ progressText }}</span>
        </div>
        <div class="progress-track"><div class="progress-value" :style="{ width: `${progress}%` }" /></div>
        <div class="muted" style="margin-top:10px;">{{ progressHint }}</div>
      </div>
    </div>

    <div class="split">
      <div>
        <div class="section">
          <div class="section-head">
            <div>
              <h2>基础信息</h2>
              <div class="section-subtitle">正文、状态与关键约束</div>
            </div>
          </div>
          <div class="kv">
            <div>指令编号</div><div>{{ item.id }}</div>
            <div>密级</div><div>{{ item.securityLevel }}</div>
            <div>截止时间</div><div>{{ item.dueAt }}</div>
            <div>当前状态</div><div><StatusBadge :label="item.status" /></div>
            <div>正文内容</div><div>{{ item.content }}</div>
          </div>
        </div>

        <div class="section">
          <div class="section-head">
            <div>
              <h2>流转时间轴</h2>
              <div class="section-subtitle">演示发布、签收、反馈、预警等关键节点。</div>
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
      <div>
        <InfoStrip label="责任焦点" :value="focusArea" extra="可用于演示巡办催办与巡组反馈。" />
        <InfoStrip label="演示建议" :value="demoHint" extra="适合作为从首页风险事项进入的第一条详情页。" />
        <div class="notice-panel info">
          <div class="notice-title">附件与审计说明</div>
          <div class="notice-desc">当前高保真原型用说明块替代真实附件预览，可在下一轮继续补成可点击附件面板与审计抽屉。</div>
        </div>
        <div class="section">
          <div class="section-head"><h2>最近动作提示</h2></div>
          <div class="inline-meta" style="margin-bottom:10px;">
            <span class="meta-pill">可扩展审批意见</span>
            <span class="meta-pill">可扩展附件签收</span>
            <span class="meta-pill">可扩展催办说明</span>
          </div>
          <div class="muted">当前版本优先保证流程讲解完整，后续可在此区域扩成附件预览、签收明细和审计侧边栏。</div>
        </div>
      </div>
    </div>
  </div>
  <EmptyState v-else icon="📭" title="未找到对应调度指令" description="请从调度指令列表重新进入，或检查当前演示场景是否切换。" />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { repository } from '@/services/api/repository'
import StatusBadge from '@/components/common/StatusBadge.vue'
import PageHeader from '@/components/common/PageHeader.vue'
import InfoStrip from '@/components/common/InfoStrip.vue'
import EmptyState from '@/components/common/EmptyState.vue'

const route = useRoute()
const item = computed(() => repository.getDispatchOrder(String(route.params.id)))
const progress = computed(() => {
  if (!item.value) return 0
  if (item.value.status === 'COMPLETED') return 100
  if (item.value.status === 'OVERDUE') return 52
  return 76
})
const progressText = computed(() => `${progress.value}%`)
const progressHint = computed(() => item.value?.status === 'OVERDUE' ? '当前仍有巡组未完成签收，建议演示催办提醒。' : '多数巡组已签收并进入办理阶段，可继续演示阶段反馈。')
const focusArea = computed(() => item.value?.status === 'OVERDUE' ? '重点关注逾期组与催办策略' : '重点关注阶段反馈与后续闭环')
const demoHint = computed(() => item.value?.status === 'OVERDUE' ? '可串联首页风险事项、调度详情和审计摘要。' : '可串联调度详情与周报上报的衔接。')
</script>
