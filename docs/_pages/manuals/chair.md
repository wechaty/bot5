---
title: "Chair Manual"
permalink: /manuals/chair/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/bot5-banner.png
#   actions:
#     - label: "Download"
#       url: "https://github.com/mmistakes/minimal-mistakes/"
  caption: "Photo credit: [slow-growing pilot](https://chatbotsmagazine.com/why-a-slow-growing-pilot-is-vital-for-chatbot-success-cce7875f93b3)"
excerpt: "For all BOT5 Chairs to Follow"
toc: true
toc_sticky: true
toc_label: "Chair Manual"
toc_icon: "tasks"  # corresponding Font Awesome icon name (without fa prefix)
---

## Vice Chair

### Vice Chairperson Duty List

1. 辅助主席开展工作，在下次活动时顺延成为轮值主席
2. 在主席无法行使职能的时候，代替主席，肩负主席职责，开展相关工作
3. 监督并提醒主席在活动前48小时，发出正式的活动通知
4. 监督并提醒主席将相关的 Pull Request 在活动通知发出之前，完成 Review/Merge 操作
5. 监督并提醒主席在活动后48小时之内，发布活动纪要
6. 在主席发布活动纪要后24小时之内，完成 Vice Chair Report(副主席报告)，回复在活动通知的留言区中

### Vice Chair Report

参加活动，对照 Chair Manual，对每次活动进行评估，并逐项给出“是（完成）”或“否（未完成）”的正式反馈。

评估反馈包括：

1. 轮值主席是否完成了[Chairman Manual]({{ '/manuals/chair/' | relative_url }})的要求（逐项检查）
    1. 活动准备
    1. 活动主持
    1. 活动总结
1. 参会会员是否符合[Member Manual]({{ '/manuals/member/' | relative_url }})的要求（逐项检查）
1. 新人是否符合[Newcomer Manual]({{ '/manuals/newcomer/' | relative_url }})的要求（逐项检查）

副主席监事报告（Vice Chair Supervisor Report)，在活动总结发布之后24小时内，以回复本次活动纪要博客留言的形式进行正式发布。

#### Vice Chair Supervisor Report Template

The following markdown can be copy/paste as the template for the report from vice chair. Put a check mark to confirm that all the manual rules were followed, and note the violation if there any.

```markdown
I, FULL_NAME, is the Vice Chair of BOT5 seminar S_SESSION_E_SPISODE.

I confirm that the Chair had followed(or not followed) the following steps in this seminar:

- [ ] Chair followed all the [Chair Manual]({{ '/manuals/chair/' | absolute_url }}) requirements
  - [ ] Before Seminar
  - [ ] During Seminar
  - [ ] After Seminar
- [ ] Members followed all the [Member Manual]({{ '/manuals/member/' | absolute_url }}) requirements
- [ ] Newcomers followed all the [Newcomer Manual]({{ '/manuals/newcomer/' | absolute_url }}) requirements

Additional Notes: put additional information here (if any).

## SIGN_FULL_NAME_AT_HERE
```

---
---

## Chair

### Before

1. 监督上任轮值主席，在上次活动后48小时内，发出上次活动纪要
1. 在上任轮值主席活动纪要发布之后的24小时之内，以回复的行使发布[Vice Chair Supervisor Report](/manuals/chair/#vice-chair-supervisor-report)
1. 在本次活动开始时间48小时之前，根据上次活动纪要，以及纪要的回复（PR）情况，按照 Issue Template ，撰写本次沙龙活动通知，并发布
1. 负责审核（Approve，或者 Request Modification）活动相关 PR，并 Merge 合格的本次活动相关的 Pull Requests, **注：PR可能会存在多条commit，所以在合并PR的时候，尽可能的选择`Squash and merge`**
1. 如果轮值主席因故无法履行本次轮值主席职责，需要在不晚于活动开始前48小时，授权轮值副主席为本次轮值主席，行使本次活动职责
1. 提前到场准备好金蛋银蛋，并启动会议相关设备

### Middle

#### 1 沙龙注意事项

1. 轮值主席负责全程按照沙龙流程进行主持
1. 轮值副主席负责协助主席开展主持工作，避免遗漏议程；如果主席无法出席代替主席进行主持
1. 每场沙龙活动理想时间为2小时(Soft limit)，最长不超过3小时(Hard limit)
1. 活动中场适度休息 10 - 15 MIN ，建议在第一个分享者之后

#### 2 沙龙流程

1. 最后一次活动回顾
1. 新人自我介绍
1. 展开本次活动内容（主席可根据情况酌情修改）
    1. 分享者 (<30min, 不可以超过 45 mins，超时后每一分钟需要发￥10红包到会员群)
    1. 为每位报告人设置定时器：
        1. 主席负责：金色 for Hard Limit (Oral/Poster 45/15 mins)
        1. 副主席负责：银色 for Soft Limit (Oral/Poster 30/10 mins)
1. 脑洞拓展：分享自己在本次活动上想到的新的好点子(1 MIN per person)
1. 选出下下任轮值主席、副主席人选，并举行“受蛋仪式”（主席和副主席不允许挂靠，副主席需要参加主席场次的活动）
    1. 将金色计时器移交给下任主席，并由下任主席负责妥善保管
    1. 将银色计时器移交给下任副主席，并由下任副主席负责妥善保管
    1. 受蛋仪式合影
1. 吐槽大会：参会人员每人至少指出一条如何在未来可以将活动办的更好的意见建议（1 MIN per person）
1. 轮值主席发言，做活动总结
1. 轮值副主席述职报告：陈述自己下周作为主席的主要工作内容
1. 所有参会人员合影（原图经过脸盲助手发到会员群）
1. 活动结束，自由交流
1. 轮值主席组织大家将场地复原（桌椅、白板、设备等）

#### 3 After Party (optional)

活动之后，主席可以根据大家实际情况和需求，酌情组织 After Party ，比如继续前往管氏串吧夜宵啤酒。

费用AA。

### After

1. 不晚于活动结束后48小时，按照最后一次活动纪要的模板，整理本次沙龙活动纪要，并将其发表于 <https://bot5.club/categories/#events> 之下。新手可以参考[Blog操作手册](https://bot5.club/manuals/blog/)
1. 协助下任轮值主席将其的 GitHub 账号，加入 GitHub Team [BOT5/chairs](https://github.com/orgs/wechaty/teams/chairs)，并将设置为 `maintainer`，并确保主席收到邀请并完成加入
1. 督促下任轮值主席，按时发出下次活动通知
