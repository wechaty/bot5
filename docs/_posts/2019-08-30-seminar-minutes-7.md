---
title: Bot Friday 第七次活动纪要
author: darkli
categories: events
tags:
  - minutes
header:
  teaser: /assets/2019/seminar-7/group-photo.jpg
---

<< Bot5 第六次活动纪要: [Bot5 Episode 6](https://bot5.club/events/seminar-minutes-6) <<

## Bot Friday Episode 7

- 时间：2019年8月30日（周五）18:30 - 22:30（4小时）
- 地点：腾讯公司北京办公室（理想国际大厦17层）
- 轮值主席：
    1. Chair: 李云军
    1. Vice-Chair: 李卓桓
- 赞助方：腾讯公司

![attendees]({{ '/assets/2019/seminar-7/group-photo.jpg' | relative_url }})

## Attendees

### Talkers

1. 段清华，金证优智技术总监。曾任文因互联研发工程师，完成项目包括金融搜索，公告摘要抽取项目，银行问答机器人。拥有多年金融NLP经验，带领团队完成问答机器人、投研系统、监管舆情、知识图谱等项目。对金融文档解析、抽取、搜索、量化分析、知识图谱建设、对话系统等领域有深入研究。
2. 李卓桓，Github 6000 Star 的微信个人号SDK开源项目 Wechaty 作者，Conversational AI 布道者。曾任水木清华BBS站长，优酷网首席科学家。清华本科，中欧EMBA，北邮博士在读。

### Corporate Members

- Microsoft
  - 丁煜恒， Microsoft Bot Framework Product Manager
- Tencent
  - 刘晓倩（平台主席），Tencent Bot Platform Product Manager

### Makers

1. 李卓桓，Github 6000 Star 的微信个人号SDK开源项目 Wechaty 作者，Conversational AI 布道者。曾任水木清华BBS站长，优酷网首席科学家。清华本科，中欧EMBA，北邮博士在读。
1. 段清华，金证优智技术总监。曾任文因互联研发工程师，完成项目包括金融搜索，公告摘要抽取项目，银行问答机器人。拥有多年金融NLP经验，带领团队完成问答机器人、投研系统、监管舆情、知识图谱等项目。对金融文档解析、抽取、搜索、量化分析、知识图谱建设、对话系统等领域有深入研究。
1. 李佳芮，句子互动创始人。句子互动创建了覆盖全球的微信聊天机器人开发者社区，公司围绕微信生态为客户提供智能对话服务。客户覆盖教育、保险等多个领域。曾入选百度AI加速器，并由PreAngel、Plug and Play和Y Combination孵化支持，已获TSVC/Alpha公社联合千万RMB级别天使投资；
1. 李云军，圈动无界创始人CEO。资深互联网从业者。历任方正、金山安全产品总监、高级技术总监。拥有2个智能排版算法专利。圈动无界公司提供团队协作产品Teamin，结合自然语言处理及人工智能，为新型社交协作人群提供更智能的助理服务，曾获360、英诺天使千万级投资
1. 张玉睿，阅粒创始人&CEO。前百度搜索产品科学家，曾任即刻产品总监，360搜索总监。阅粒是做基于神经网络的端到端知识问答服务。
1. 曹辉，金融科技公司产品负责人。

## Talks

本次会议小圆桌讨论，不对外直播

### 1 搞定一个对话平台

![段清华]({{ '/assets/2019/seminar-7/duanqinghua.jpg' | relative_url }})

段清华，金证优智技术总监。曾任文因互联研发工程师，完成项目包括金融搜索，公告摘要抽取项目，银行问答机器人。拥有多年金融NLP经验，带领团队完成问答机器人、投研系统、监管舆情、知识图谱等项目。对金融文档解析、抽取、搜索、量化分析、知识图谱建设、对话系统等领域有深入研究。

幻灯片：[搞定一个对话平台/ 段清华](https://docs.google.com/presentation/d/1qybOUwjTAuiU3YfeyJn7eO8KxzWq2xhJ7wIdw4XjrNE/edit?usp=sharing)

<div class="zoom-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src='{{ '/assets/js/viewer-js/#/assets/2019/seminar-7/slides-duanqinghua.pdf' | relative_url }}'
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

**分享大纲：**

开始选择

- 最好别用对话
- 能不能不用对话
- 是否真的需要对话
- 用什么对话

问答与知识问答

- FAQ问题
- Factoid问题
- Non-Factoid问题

对话

- NLU是最重要的
- 对话选择
  - botframework
  - rasa

设计

- 对话目标总是解决问题
- 收集解决问题的要素
- 用20%的时间解决80%的问题，然后用剩下的80%的时间解决剩下的20%的问题

### 2 Bot Market Place — 可重用能力平台

李卓桓，Github 6000 Star 的微信个人号SDK开源项目 Wechaty 作者，Conversational AI 布道者。曾任水木清华BBS站长，优酷网首席科学家。清华本科，中欧EMBA，北邮博士在读。

幻灯片：[Bot Market Place / 李卓桓](https://docs.google.com/presentation/d/13oUOIEnzdLWO6KZWztD_pMuu22AQ3SIMjk2wp8f-f18/edit?usp=sharing)

<div class="video-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
<iframe width="560" height="315" src="https://docs.google.com/presentation/d/13oUOIEnzdLWO6KZWztD_pMuu22AQ3SIMjk2wp8f-f18/embed?start=false&loop=false&delayms=3000" frameborder="0" allowfullscreen="" style="
    position: absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
"></iframe></div>

**分享大纲：**

1. 两年前 Wechaty 101 中的 Bot 市场思路介绍  
  1.1 Hostie  
  1.2 Botie  
  1.3 Giftie  
2. RPA 的价值和挑战
3. 低代码编程的悖论
4. 未来Chatbot的AI展望：麻瓜也能变成AI大师

## 活动纪要

1、脑洞及改进建议

现场大家各自针对目前活动举办中的问题改进，提出了自己的建议：

1. 李卓桓：为了沙龙活动的良好秩序维护，要来的人务必都提前报名
脑洞：以后也许可以使用bot机器人来进行报名和分享提醒，建立积分制，通过参与活动的程度来给予相应积分
1. 李佳芮：希望每次的会员分享充分，有价值的东西都说出来
脑洞：使用giftie原理，为不同的微信群提供定制报表能力
1. 段清华：对于活动报名群里多发几次
提前确定每次分享的主题，激发大家讨论热情
脑洞：让微信、企业微信、钉钉也能有类似的channel的服务
1. 李云军：让每次分享的主题明确，每次的讨论更深入，提高沙龙活动的价值感
脑洞：当意图过多的时候不好管理，也会让对话的分析过程变得更加复杂，性能下降，意图是不是可以分多层，并且具备自生长的机制
1. 张玉睿：希望每次的活动可以聚焦，讨论透彻
脑洞：未来机器人之间的互动该怎么来做，比如chatied和小冰之间的互动？数据共享？共同协作？

## 轮值主席任命仪式

1. 下任轮值主席：李卓桓
2. 下任轮值副主席：张玉睿

![轮值主席任命仪式]({{ '/assets/2019/seminar-7/chairs.jpg' | relative_url }})

## 下次活动信息

1. 时间：8月16日（周五） 18:30 - 21:00
1. 主席：李卓桓
1. 副主席：张玉睿

## 未来分享议题

欢迎大家踊跃报名！

1. 李明/俊良：Wechaty Mini Program Support
1. 李明/俊良: What will happen after Chatbot empowered by Mini Program?
1. 邝伟鹏：Chatbot 场景分享：秒印，家校沟通的工具。
1. 肖立鹏：udesk 场景分享 （待定）
1. 刘晓倩：Chatbot 行业应用，智能对话连接数据与商业
1. 高原：企业微信开发实战分享
1. 李佳芮：如何用Chatbot做售前导流
1. 雷飚：AI + AR + Chatbot = ？
1. 段清华：打造一个超越 rasa 的chatbot平台 —— deepdialog.ai
1. 李靖：Bot Framework 产品组互动
1. 舒畅：Chatbot行业创业赛道扫描
1. 朱跃峰：教育培训行业的Chatbot应用探索
1. 张程：如何评价Chatbot交互过程中的主观评估指标
1. 彭俊：如何从0打造7代李白
1. 丁煜恒：Conversation as a Platform
1. 欧阳鑫：BERT Chatbot实践及硬件加速
1. 陈远强：Chatbot中关于反欺诈的应用
1. 金庸：Chatbot和公众号结合代运营
1. 郑譞：聊天机器人和自然语言的标注
1. 李晶莹：聊天机器人聊论语

## 集体合影

![合照]({{ '/assets/2019/seminar-7/group-photo.jpg' | relative_url }})

## After Party 🍻

主场活动结束后，3个人前往管氏串吧继续补充能量，针对团队的管理，对话技术作了进一步深入交流。

---

特别鸣谢:

1. 场地赞助方：腾讯公司
2. 晚餐赞助方：Tencent Bot Platform产品团队
3. 活动主办方：句子互动公司

RSVP:

1. 如果对活动纪要有修订或补充意见，请回复对本次活动纪要留言；
1. 如果参加下次沙龙活动，请回复下次自己愿意分享的主题；
1. 如果计划邀请新朋友参加下次沙龙活动，请让新朋友回复一句话的自我介绍；
