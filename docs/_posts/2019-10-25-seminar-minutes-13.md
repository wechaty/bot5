---
title: Bot Friday 第十三次活动纪要
author: windmemory
categories: events
tags:
  - minutes
header:
  teaser: /assets/2019/seminar-13/group.jpg
---

<< Bot5 第十二次活动纪要: [Bot5 Episode 12](https://bot5.ml/events/seminar-minutes-12) <<

## Bot Friday Episode 13

- 时间：2019年10月18日（周五）19:00 - 22:00（3小时）
- 地点：中关村智造大街G座PNP孵化器惠斯勒会议室
- 轮值主席：
    1. Chair: 高原
    1. Vice-Chair: 郭成凯
- 赞助方：句子互动

![attendees]({{ '/assets/2019/seminar-13/group.jpg' | relative_url }})

## Attendees

1. 梁皓然 (Speaker)，[XTech](https://x-tech.io)创始人&CEO。
1. 高原，句子互动联合创始人CTO。
1. 郭成凯: 曾任小米深度学习组研究员，负责了小米旗舰机的相机单摄虚化算法，算法基本逼平、部分领域超过商汤、虹软、Google等竞争对手，并在人脸人像，目标检测，语音合成，音视频分析等领域拥有自主知识产权深度学习算法。
1. [李佳芮](/people/lijiarui/)，句子互动创始人CEO。

## Talks

### 1 Rasa v1 new features: FAQ and knowledge base

![梁皓然]({{ '/assets/2019/seminar-13/talk1.jpg' | relative_url }})

介绍 Rasa V1 的新功能，大大简化了 Chatbot Stories 的编写和添加了新的 Knowledge Base 功能。

Slides：

<div class="zoom-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-13/talk1.pdf' | relative_url }}'
    width='560'
    height='315'
    allowfullscreen
    webkitallowfullscreen
    frameborder="0"
    style="
      position: absolute;
      top:0;
      left:0;
      width:100%;
      height:100%;
    "
  ></iframe>
</div>

### 2 Bot Friday Bot 的设计与规划

![高原]({{ '/assets/2019/seminar-13/talk2.jpg' | relative_url }})

整理了一下 Bot Friday 的主席的职能，以及其中可以使用 Bot 来协助的部分，大家一起讨论一下具体的实施细节

幻灯片：

<div class="video-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-13/talk2.pdf' | relative_url }}'
    width='560'
    height='315'
    allowfullscreen
    webkitallowfullscreen
    frameborder="0"
    style="
      position: absolute;
      top:0;
      left:0;
      width:100%;
      height:100%;
    "
  ></iframe>
</div>

#### 后续计划

##### 分工（暂定）

- 需求分析：TBD
- 数据处理：TBD
- 流程设计：高原
- 对话脚本撰写：李卓桓
- 系统搭建：梁皓然（github信息存储调用）,段清华（其他一切）
- 任务测评：郭成凯
- 平台渠道接入：段清华
- 运营反馈：李佳芮

句子互动提供服务器，微信号，token

##### Milestone 1

重点将微信信息和github信息打通，并管理

- 搭项目
- 打通github账号和微信
  - 新用户提供github信息后，拉入活动群
  - 老用户加好友
  - 老用户定期询问github信息，直到收集到为止
- 拉取github上面成员信息，存储
- 聊天信息存储

##### 其他

- 建议增加数据库存储消息数据，供未来训练模型使用

## 活动纪要

### 改进建议

- 郭成凯：主席没控制好时间。人少的时候是不是可以以更自由的方式来沟通
- 梁皓然：准备时间不足，新鲜血液不够，没有足够的分享话题，大家要多邀请新人参加
- 李佳芮：活动开始晚了几分钟，主席要控制时间，准时开始

### 脑洞

- 李佳芮：国内做一个类似chatbase或者dashbot的平台，做chatbot的分析在国内会很有前景
- 梁皓然：国内的intercom之后是让用户在PC上继续聊还是在手机上聊，是不是可以直接扫码打开小程序，让用户登录等，就可以后续跟踪
- 郭成凯：nifty.ai做了建筑行业的ai，把一句话做一个结构化的解析，然后录入系统。可能通过说话的方式来填一个人的信息的表格，是一个新的思路。用自然语言来填表，可以直接对接后面的系统
- 高原：如果把 chatbot 变成一种 monitor bot，在聊天过程中监控聊天内容而非回复消息，然后根据内容自动抽取重要信息来辅助人，是不是有一定的可行性

## 轮值主席任命仪式

1. 下任轮值主席：郭成凯
2. 下任轮值副主席：李佳芮

![轮值主席任命仪式]({{ '/assets/2019/seminar-13/chairs.jpg' | relative_url }})

## 下次活动信息

1. 时间：11月1日（周五） 19:00 - 21:00
1. 主席：郭成凯
1. 副主席：李佳芮

## 集体合影

![合照]({{ '/assets/2019/seminar-13/group.jpg' | relative_url }})

## After Party 🍻

![合照]({{ '/assets/2019/seminar-13/after.jpg' | relative_url }})

-----

特别鸣谢:

1. 场地赞助方：句子互动公司
2. 晚餐赞助方：句子互动公司
3. 演讲嘉宾：郭成凯、朱竣峰

RSVP:

1. 如果对活动纪要有修订或补充意见，请回复对本次活动纪要留言；
1. 副主席请在活动纪要发布后24小时内，以回复的行使发布[Vice Chair Supervisor Report](/manuals/chair/#vice-chair-supervisor-report)
1. 参加下次沙龙活动报名要求：回复“姓名、个人的一句话介绍（如果是新人）、推荐人（如果是新人）、是否参加 After Party 🍻”。鼓励大家在报名中提交自己愿意分享的话题进行登记（完整话题列表在[这里](https://www.bot5.ml/talks/))；
