<template>
  <PageHeader title="新建周报/问题报表" subtitle="演示表单填写、校验提示、保存草稿与提交操作的页面骨架。">
    <button class="button secondary" @click="applyTemplate">套用模板</button>
    <button class="button">模拟提交</button>
  </PageHeader>

  <div class="tabs">
    <button class="tab-button" :class="{ active: activeTab === 'basic' }" @click="activeTab = 'basic'">基础信息</button>
    <button class="tab-button" :class="{ active: activeTab === 'detail' }" @click="activeTab = 'detail'">问题与附件</button>
    <button class="tab-button" :class="{ active: activeTab === 'review' }" @click="activeTab = 'review'">提交预览</button>
  </div>

  <div class="section" v-if="activeTab === 'basic'">
    <div class="form-grid">
      <div>
        <label class="form-label">报表类型</label>
        <select class="form-control" v-model="form.type">
          <option value="周报">周报</option>
          <option value="问题报表">问题报表</option>
        </select>
      </div>
      <div>
        <label class="form-label">周期</label>
        <input class="form-control" v-model="form.period" />
      </div>
      <div class="form-row-full">
        <label class="form-label">标题</label>
        <input class="form-control" v-model="form.title" placeholder="请输入报表标题" />
      </div>
      <div class="form-row-full">
        <label class="form-label">正文摘要</label>
        <textarea class="form-textarea" rows="8" v-model="form.content" placeholder="请输入本周工作推进、发现问题和处理建议"></textarea>
      </div>
    </div>
    <div class="validation-note" v-if="!form.title || form.content.length < 12">请至少填写标题，并保证正文摘要不少于 12 个字，便于演示表单校验。</div>
  </div>

  <div class="section" v-else-if="activeTab === 'detail'">
    <div class="dual-column">
      <div>
        <label class="form-label">问题分类</label>
        <select class="form-control" v-model="form.category">
          <option value="流程">流程</option>
          <option value="财务">财务</option>
          <option value="干部管理">干部管理</option>
        </select>
        <div class="form-hint">用于模拟退回时要求补充问题分类。</div>
      </div>
      <div>
        <label class="form-label">附件目录</label>
        <input class="form-control" v-model="form.attachmentIndex" placeholder="如：附件 1~5" />
        <div class="form-hint">当前版本不上传真实文件，使用目录字段模拟。</div>
      </div>
    </div>
  </div>

  <div class="section" v-else>
    <div class="kv">
      <div>报表类型</div><div>{{ form.type }}</div>
      <div>周期</div><div>{{ form.period }}</div>
      <div>标题</div><div>{{ form.title || '（未填写）' }}</div>
      <div>问题分类</div><div>{{ form.category }}</div>
      <div>附件目录</div><div>{{ form.attachmentIndex || '（未填写）' }}</div>
      <div>正文摘要</div><div>{{ form.content || '（未填写）' }}</div>
    </div>
  </div>

  <div class="actions" style="margin-top:16px;">
    <button class="button light">保存草稿</button>
    <button class="button secondary">预览校验</button>
    <button class="button">提交巡办</button>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import PageHeader from '@/components/common/PageHeader.vue'

const activeTab = ref<'basic' | 'detail' | 'review'>('basic')
const form = reactive({
  type: '周报',
  period: '2026-W16',
  title: '',
  content: '',
  category: '流程',
  attachmentIndex: '',
})

const applyTemplate = () => {
  form.title = '第三巡视组第 16 周周报（模板）'
  form.content = '本周围绕专项资金和采购流程开展谈话核查，形成问题线索 2 项，建议继续补充附件与分类说明。'
  form.attachmentIndex = '附件 1~3'
}
</script>
