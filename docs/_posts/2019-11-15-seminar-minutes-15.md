---
title: Bot Friday 第十五次活动纪要
author: lijiarui
categories: events
tags:
  - minutes
header:
  teaser: /assets/2019/seminar-15/group.jpg
---

<< Bot5 第十四次活动纪要: [Bot5 Episode 14](https://bot5.club/events/seminar-minutes-14) <<

## Bot Friday Episode 15

- 时间：2019年11月15日（周五）19:00 - 21:30（3小时）
- 地点：中国电子交易大厦，第三极710，腾讯会议室
- 轮值主席：
    1. Chair: 李佳芮
    1. Vice-Chair: 姜宁
- 赞助方：朱竣峰

![attendees]({{ '/assets/2019/seminar-15/group.jpg' | relative_url }})

## Attendees

1. 王磊: 后英语时代创始人,十年工程技术经验
1. 吴际：教育公司轻课技术负责人
1. 李博：微信NLP算法团队产品经理
1. 牛成：微信NLP算法团队负责人
1. 张宁：微信NLP算法团队前端工程师
1. 李娜：微信NLP算法团队工程师
1. 张金超：微信NLP算法团队工程师
1. [段清华](/people/qhduan)：金证优智技术总监
1. [李卓桓](/people/huan/)：PreAngel合伙人
1. 杨理想：南京摄星智能创始人，NLP爱好者
1. 郑譞：伽利略资本董事总经理
1. [高原](/people/windmemory)：句子互动CTO
1. [李佳芮](/people/lijiarui/)：句子互动创始人
1. 郭成凯：前小米深度学习组算法专家
1. [朱跃峰](/people/jeffzhu76)：厦门联络易创始人
1. 李乾：句子互动运营总监

## Talks

### 1 ChatBot 在线下活动中的应用

![王磊]({{ '/assets/2019/seminar-15/wanglei.jpg' | relative_url }})

幻灯片：

<div class="video-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-15/pet-chatbot.pdf' | relative_url }}'
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

### 2 在线教育微信社群管理的实践和构想 by 轻课

![吴际]({{ '/assets/2019/seminar-15/wuji.jpg' | relative_url }})

幻灯片：

<div class="video-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-15/qingke-education.pdf' | relative_url }}'
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

### 3  微信智能对话平台介绍

![libo]({{ '/assets/2019/seminar-15/libo.jpg' | relative_url }})

幻灯片：

<div class="video-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-15/openai-weixin.pdf' | relative_url }}'
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

## 活动纪要

### 脑洞

- 高原：未来可以有一个黑名单，自动将扰乱群内秩序的人的微信号放到黑名单里面。
- 郭成凯：在游戏运营中，可以将游戏里的人自动分类，不同爱好的人在不同的群中交流。
- 张金超：张小龙除了让微信更好之外，更重要的是保证了微信的不死。站在微信团队上看，既要用微信做商业的事，也得让微信活下去，广州微信的总部有一个大大的slogan："少发微信，多和朋友见见面"
- 牛成：微信机器人是一个灰色地带，虽然这个地带有很多人正在提供有正向价值的服务，但在今天还没办法保证这些服务不破坏微信生态且保证微信的数据安全。
- 张宁: wechaty 可以做一个机器人商店，开发者写好的机器人都展示出来，比如英语机器人、写诗机器人等等。机器人不能模仿人，机器人只是一种服务的方式，机器人应该更加坦诚。
- 李佳芮：未来是不是可能给个人号一个类似公众号的严格审核流程，建立秩序，进而能让个人号在秩序中提供服务。
- 李卓桓：垃圾广告的判定，可以参考反垃圾邮件时代的Distributed Checksum Clearinghouses（DCC），每一个用户点这封邮件是垃圾邮件的时候，系统会把这封邮件的hash去传到服务器，再次有其他人发这个邮件的时候，两个hash 做对比，如果极度相似就不允许发，这样就能在不知道用户发送内容的前提下做内容审查。
- 郑譞：做一个群内爬楼机器人，自动整理会议总结，或者机器人自动汇报群内工作总结，能大大提供商务工作效率。
- 李乾：未来希望有一个微信机器人的助理，在自己不打开微信的时候，机器人助理可以临时处理基础的微信消息。
- 王磊: 希望做一个保证群里的秩序的同时还能保证群里的活跃度的机器人，另外，通过机器人收集群内用户的行为，找到最有价值的共享者。
- 李娜：希望机器人能在微信之外，比如电商领域，发挥更大的机制。
- 李博：未来希望有一个自动写稿机器人，在今天是ugc(User Generated Content)和pgc（Professional Generated Content），未来是如果有bgc（Bot Generated Content）会是一个很有趣的事情。
- 朱跃峰：能设计出一个机器人，立刻筛选出群内广告，就把这个人踢掉，净化群内环境。
- 段清华：让机器人在群内互相聊天的方式做出商品推荐。

### 改进建议

- 李博&张宁： 晚餐没吃饱，没餐巾纸和水
- 李卓桓：会议室太热
- 王磊: 吃完东西桌子应该收拾一下，拍照能好看一些
- 吴际：记不住所有人的信息，如果现场有每个人的信息提示就好了
- 李乾：每个人发给名片签就会方便很多了
- 端清华：现场投影不清楚
- 张金超：会议信息内容多，需要做内容总结
- 李佳芮：这次报名流程没有不规范
- 牛博：希望大家用微信openAI，希望收到大家吐槽
- 高原：饭来晚了
- 朱跃峰：break time 漏掉了

## 轮值主席任命仪式

1. 下任轮值主席：姜宁
2. 下任轮值副主席：王磊

![轮值主席任命仪式]({{ '/assets/2019/seminar-15/chairs.jpg' | relative_url }})

## 下次活动信息

1. 时间：11月22日（周五） 19:00 - 21:00
1. 主席：姜宁
1. 副主席：王磊

## 集体合影

![合照]({{ '/assets/2019/seminar-15/group.jpg' | relative_url }})

## After Party 🍻

![After Party]({{ '/assets/2019/seminar-15/after-party.jpg' | relative_url }})

After Party 上，大家达成一致，bot5 将会举办 ski bot5，在2019年的雪季，把bot5 club将会到崇礼举办一次ski bot活动，畅聊chatbot后，在崇礼滑雪+温泉！@朱峻峰 回来组织我们的 ski bot5 活动！

-----

特别鸣谢:

1. 场地赞助方：腾讯公司
2. 晚餐赞助方：朱竣峰
3. 演讲嘉宾：王磊、吴际、李博

RSVP:

1. 如果对活动纪要有修订或补充意见，请回复对本次活动纪要留言；
1. 副主席请在活动纪要发布后24小时内，以回复的行使发布[Vice Chair Supervisor Report](/manuals/chair/#vice-chair-supervisor-report)
1. 参加下次沙龙活动报名要求：回复“姓名、个人的一句话介绍（如果是新人）、推荐人（如果是新人）、是否参加 After Party 🍻”。鼓励大家在报名中提交自己愿意分享的话题进行登记（完整话题列表在[这里](https://www.bot5.club/talks/))；
