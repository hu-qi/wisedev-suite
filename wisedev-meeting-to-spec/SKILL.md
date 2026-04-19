---
name: wisedev-meeting-to-spec
description: analyze meeting notes, transcript text, and mixed chinese discussion materials and convert them into structured requirement inputs. use when the user provides a transcript, a meeting summary, or scattered discussion text and wants requirement clarification, feature extraction, role and scenario analysis, unresolved question tracking, or a draft requirement brief.
---

# 目标
在 `using-wisedev` 已确认这是明确单阶段任务，或 `wisedev-orchestrator` 已完成阶段判断后，再由本 Skill 处理当前阶段。

首次执行本阶段任务时，优先参考 `references/example-library.md`；若输入与“上传下达模块”高度相似，再对照 `../shared/full-chain-examples/case-01-upload-delivery/01-meeting-to-spec.md` 的本阶段样例。


把噪声较高的会议讨论材料转成可进入需求阶段的结构化产物。

# 输入类型

- 录音转写文本
- 会议纪要
- 讨论群消息摘录
- 多份材料混合输入

# 处理流程

1. 提取显性事实：背景、目标、角色、场景、功能点、约束、时间要求。
2. 归并重复表述，把同义需求合并成统一条目。
3. 区分：
   - 已明确达成一致的结论
   - 倾向性方案
   - 个人观点或未决问题
4. 识别缺口：权限、状态、异常、边界条件、口径冲突、审批流程缺失等。
5. 输出“需求梳理稿”，供后续写需求规格说明书使用。

# 输出要求

必须至少输出：
- 一页式摘要
- 角色与关系图（文字版）
- 业务场景清单
- 功能点清单
- 风险与歧义项
- 待确认问题列表
- 需求简报初稿

# 质量要求

- 不要把讨论中的口头表达原样堆砌到结果里。
- 对没有被会议明确确认的内容，统一标记为“工作假设”。
- 当材料内容不完整时，要优先补齐结构，而不是强行补细节。

# 高质量样例优先

优先参考 `references/example-library.md` 和 `references/examples/` 下的案例，尤其是“上传下达模块”“周报填报”这类政企业务协同场景。样例用于稳定输出骨架，不用于限制具体内容。

# 可用资源

- `references/transcript-patterns.md`
- `references/ambiguity-handling.md`
- `templates/meeting-summary.md`
- `templates/requirement-brief.md`
- `templates/decision-log.md`
- `templates/feature-extraction.md`
- `templates/open-questions.md`