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
1. 在上任轮值主席活动纪要发布之后的24小时之内，以回复的形式发布[Vice Chair Supervisor Report](/manuals/chair/#vice-chair-supervisor-report)
1. 确定活动分享人，以及分享主题：
    1. 根据已有 [Talks](https://www.bot5.club/talks/) 的情况，邀请已登记但未分享的成员或其他成员来做活动分享，确定本周分享内容
    1. Speaker 确认方法：会员本人将自我介绍、本次自己分享的主题、大纲，回复在上一次活动纪要的评论中
1. 确认本次活动场地。尽量避免连续两次使用同一场地，绝对不能连续三次使用同一场地。如主席自己没有地点，可以咨询上届主席或联系以下场地负责人：
    1. 腾讯办公室
        - 地址：中关村，第三极大厦、理想国际大厦
        - 联系人：[李卓桓](https://www.bot5.club/people/huan)
    1. 微软亚太研发集团大厦(微软总部)
        - 地址：中关村，丹棱街5号
        - 联系人：[李佳芮](https://www.bot5.club/people/huan/)
    1. Plug and Play China 孵化器
        - 地址：五道口，智造大街G座
        - 联系人：[高原](https://www.bot5.club/people/windmemory/)
    1. WeWork 协作办公空间
        - 地址：中关村，互联网金融中心
        - 联系人：[尹伯昊](https://www.bot5.club/people/)
1. 确认会前是否有小吃赞助，并最终沟通落实小吃赞助的采买
1. 在本次活动开始时间48小时之前，在活动群内发布通知
1. （可选）决定分享的会员，在活动开始时间24小时前发出分享内容的 Blog（发布[教程](https://www.bot5.club/manuals/blog/)），并同步更新 [Talks](https://www.bot5.club/talks/) 页面，在该页面的 `Queue` 部分更新好自己的分享主题和 Blog 链接
1. 负责审核（Approve，或者 Request Modification）[活动相关 Pull Requests](https://github.com/wechaty/bot5.club/pulls)（以下简称PR），并 Merge 合格的本次活动相关的 PR, **注：PR 可能会存在多条commit，所以在合并PR的时候，尽可能的选择`Squash and merge`**
1. 如果轮值主席因故无法履行本次轮值主席职责，需要在不晚于活动开始前48小时，授权轮值副主席为本次轮值主席，行使本次活动职责
1. 提前到场准备好金蛋银蛋，并启动会议相关设备
1. 主席可以根据情况，选择将活动内容分享至可能有潜在适合成为 BOT5 会员的人群中，以召集更多的新鲜血液来参加活动，在召集过程中要注意以下几点：
    1. 主席自己作为所有新人的邀请人，邀请新人加入 Bot Friday 的活动
    1. 主席需要尽到邀请人的职责，确保新人完整阅读了[新人手册](https://www.bot5.club/manuals/newcomer/)并在上一次的活动纪要下报名参加活动
    1. 主席需要控制活动的人数，保证每场活动人数不会超过15个人
    1. 主席在发布活动邀请到群中时，可以借用 `Wechaty Bot` 来发送群公告（联系高原），发送群公告的时候，需要使用英文

### Middle

#### 1 沙龙注意事项

1. 轮值主席负责全程按照沙龙流程进行主持
1. 轮值副主席负责协助主席开展主持工作，避免遗漏议程；如果主席无法出席代替主席进行主持
1. 每场沙龙活动理想时间为2小时(Soft limit)，最长不超过3小时(Hard limit)
1. 活动中场适度休息 10 - 15 MIN ，建议在第一个分享者之后

#### 2 沙龙流程

1. ![QRCode start]({{ '/assets/images/start.png' | relative_url }})
1. 最后一次活动回顾
1. 新人流程
    1. 将新人邀请进入 _“Bot Friday Open Form - BFOF”_ 微信群。（邀请人负责邀请。如果邀请人不在现场则由主席一人负责）
    1. 新人自我介绍（1 MIN）
1. 展开本次活动内容（主席可根据情况酌情修改）
    1. 分享者 (<30min, 不可以超过 45 mins，超时后每一分钟需要发￥10红包到会员群)
    1. 为每位报告人设置定时器：
        1. 主席负责：金色 for Hard Limit (Oral/Poster 45/15 mins)
        1. 副主席负责：银色 for Soft Limit (Oral/Poster 30/10 mins)
1. 会员升级
    1. 新人 -> 实习会员：第一次完成分享的新人，将升级为实习会员。由其邀请人负责将其加入 _“Bot Friday Club - BOT5”_ 会员群。（如果邀请人不在，则由当期主席负责）；
    1. 实习会员 -> 正式会员：参加了三次活动的实习会员（含三次），将有资格转为正式会员。转正要求：发送个人 Profile 页面的 Pull Request 至 <https://bot5.club/people/GITHUB_USERNAME/> 下。PR Merge 后正式成为 BOT5 会员；
    1. 正式会员 -> 实习主席：正式会员可以被提名成为主席候选人。主席候选人被选举成功之后，成为实习主席；
    1. 实习主席 -> 主席：将完成了第一次轮值主席工作的实习主席，加入 Github Team: chairs，并在 team 中授予 maintainer 权限，便于未来升级其他主席。
1. 脑洞拓展：
    1. 分享自己在本次活动上想到的新的好点子(1 MIN per person)
    1. 不讨论（讨论留到After Party）
    1. 主席负责记录。
1. 选出下下任轮值主席、副主席人选，并举行“受蛋仪式”（主席和副主席不允许挂靠，副主席需要参加主席场次的活动）
    1. 将金色计时器移交给下任主席，并由下任主席负责妥善保管
    1. 将银色计时器移交给下任副主席，并由下任副主席负责妥善保管
    1. 受蛋仪式合影
1. 吐槽大会：
    1. 参会人员每人至少指出一条如何在未来可以将活动办的更好的意见建议（1 MIN per person）
    1. 不讨论（讨论留到After Party）
    1. 主席负责记录
1. 轮值主席发言，做活动总结
1. 轮值副主席述职报告：陈述自己下周作为主席的主要工作内容
1. 所有参会人员合影（原图经过脸盲助手发到会员群，并将带名字的照片，发布在活动纪要中）
1. 活动结束，自由交流
1. 轮值主席组织大家将场地复原（桌椅、白板、设备等）
1. ![QRCode end]({{ '/assets/images/end.png' | relative_url }})

#### 3 After Party (optional)

活动之后，主席可以根据大家实际情况和需求，酌情组织 After Party ，比如继续前往管氏串吧夜宵啤酒。

费用AA。

### After

1. 不晚于活动结束后48小时，按照最后一次活动纪要的模板，整理本次沙龙活动纪要，并将其发表于 <https://bot5.club/categories/#events> 之下。新手可以参考[Blog操作手册](https://bot5.club/manuals/blog/)
1. 协助下任轮值主席将其的 GitHub 账号，加入 GitHub Team [BOT5/chairs](https://github.com/orgs/wechaty/teams/chairs)，并将设置为 `maintainer`，并确保主席收到邀请并完成加入
1. 督促下任轮值主席，按时发出下次活动通知
