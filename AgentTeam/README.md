# AgentTeam for WiseDev Suite

本目录用于存放 WiseDev Suite 面向“长期协作、多角色产品交付团队”的 AgentTeam 设计资料、角色规范、配置草案和共享模板。

## 目录说明
- `ROLE_SPEC.md`：长期协作团队角色说明书
- `team-config.example.yaml`：AgentTeam 配置草案
- `leader-persona.md`：团队 Leader 人设草案
- `reviewer-persona.md`：团队 Reviewer 人设草案
- `shared-workspace-layout.md`：共享工件目录规范
- `shared/templates/`：团队协作模板目录

## 设计目标
本目录不替代现有 `wisedev-*` skills，而是为它们提供一个更高层的 Team 运行时组织方式。

目标包括：
1. 将阶段化单技能编排升级为长期协作团队
2. 用角色分工替代单总控串行路由
3. 用共享工件保证跨角色事实一致
4. 用 reviewer 与 leader 验收保证阶段推进可控

## 推荐落地顺序
1. 先固定角色与共享工件规范
2. 再固定 team 配置
3. 再将模板纳入日常协作
4. 最后接入真正的 AgentTeam runtime

## 当前状态
当前目录中的内容主要是设计与模板草案，适合作为：
- Team 方案设计输入
- 配置试验基础
- 团队运行规范沉淀点
