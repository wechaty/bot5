---
title: The Bad Part of My Chatbot Experience
author: limingth
date: 2019-07-26 19:00 +0800
categories: talk
tags:
  - time_nlp
  - recognizers
  - BosonNLP
  - bothub
header:
  teaser: /assets/2019/maodou-bot/maodou-bothub-arch.jpg
---

<< 本次活动通知: [Bot Friday 第二弹](https://blog.chatie.io/bot-friday-second/) <<

## Bot Friday - 沙龙第2场分享

The Bad Part of My Chatbot Experience

2019-07-26 于北京腾讯，[limingth](https://github.com/limingth)

## NLP技术到底哪家强

### 需求背景

从一句话中识别出时间，主题和地点，这是我们正在做的项目[毛豆课堂](https://blog.chatie.io/send-miniprogram-using-padpro/)中衍生出的一个需求，通过添加[毛豆课堂小助手](https://blog.chatie.io/assets/2019/maodou-ketang-qrcode.png)为微信好友后，发送一句话可以通过这个 chatbot 来创建一个课程提醒。

![maodou-time-nlp-ra.png](/assets/2019/maodou-bot/maodou-time-nlp-ra.png)

原本这应该是做 Chatbot 项目要用到 NLP 中最常见的一个需求，特别是时间，如何能够快速得到最符合文本中人类意图的时间。但找了一圈可以识别时间的NLP，却没有发现真正能够符合我们需求的解决方案。

常见解决方案的不足表现在：

1. 识别出了时间实体所包含的分词，但却没有转换为时间变量，无法在程序中使用。例如讯飞和百度的开放平台。

2. 有的虽然能转化为时间变量，但返回的却是json格式的多项复杂结果，还需要继续写代码做筛选和取舍。例如微软提供的NLP库。

3. 其他存在的问题，表现在大量采用了正则匹配，而忽略了上下文的语义分析。例如把9号楼（地点）识别为9号（时间）。

作为非NLP领域的技术人员，只为了在工程应用里加入一个时间识别功能，却不得不花费好几天研究各家的NLP接口和返回结果，是非常低效的一件事情，因此不由发出了 “NLP技术到底哪家强？” 的感慨。

以下是我对这个过程的一点总结，希望能够对后来者有所借鉴。

<!--more-->

## AI开放平台调研

经过研究和测试，发现各大AI平台提供的接口，都是词法分析的结果为核心，返回各个实体的文本字段。真正对于工程有价值的，应该不是一个文本，而是一个 Date 变量，因此就没有采用这方面的接口。

* 讯飞开放平台
  * 词法分析: [https://www.xfyun.cn/services/lexicalAnalysis](https://www.xfyun.cn/services/lexicalAnalysis)
  * 关键字提取: [https://www.xfyun.cn/services/keyword-extraction](https://www.xfyun.cn/services/keyword-extraction)

![maodou-xunfei-nlp.png](/assets/2019/maodou-bot/maodou-xunfei-nlp.png)

* 百度开放平台
  * 词法分析: [https://ai.baidu.com/tech/nlp_basic/lexical](https://ai.baidu.com/tech/nlp_basic/lexical)

![maodou-baidu-nlp.png](/assets/2019/maodou-bot/maodou-baidu-nlp.png)

## 实际使用的库和效果

经过比对和验证，最后实际使用的库是微软的 recognizers，用来实现从一句话中获取时间，还有玻森的BosonNLP，用来获取主题和地点。只不过这两家给出的结果，都是带有数组结构的 json，还需要加上不少的 if-else 才能筛选出合适的期望结果。

这也是目前我们认为还很不满意的地方，实现的源码我放在了[这里](https://github.com/maodouio/wechaty-getting-started/blob/master/examples/third-party/maodou/maodou-nlp.js)。希望看过这篇博客，能给出更好解决方案的人和我联系。（我的微信号 limingth）

### @microsoft/recognizers

* npm安装包：[https://www.npmjs.com/package/@microsoft/recognizers-text-suite](https://www.npmjs.com/package/@microsoft/recognizers-text-suite)

recognizers 给出的返回值：
![maodou-ms-recognizer.png](/assets/2019/maodou-bot/maodou-ms-recognizer.png)

### BosonNLP

* 命名实体识别：[http://docs.bosonnlp.com/ner.html](http://docs.bosonnlp.com/ner.html)
* npm安装包：[https://www.npmjs.com/package/bosonnlp](https://www.npmjs.com/package/bosonnlp)

BosonNLP 给出的返回值：
![maodou-boson-ner](/assets/2019/maodou-bot/maodou-boson-ner.png)

### Time-NLP

* 代码库：[https://github.com/shinyke/Time-NLP](https://github.com/shinyke/Time-NLP)
* npm安装包：[https://github.com/JohnnieFucker/ChiTimeNLP](https://github.com/JohnnieFucker/ChiTimeNLP)

虽然最终我们没有采用 chi-time-nlp，原本已经调通的代码后来注释了，但我还是想借这个例子，说明一下我认为理想中的API是什么样子。这是我最早调试跑通的库，也是最快能解决问题的一个方案，可惜原作者已经不维护了，不过它仍然有如下这样的示范价值。

#### 理想中的API是这样的

* 搜索排在首页
![maodou-google-nlp](/assets/2019/maodou-bot/maodou-google-nlp.png)

* 接口和返回值简单清晰
![maodou-api-simple](/assets/2019/maodou-bot/maodou-api-simple.png)

* 无需注册Key/Token
![maodou-api-notoken](/assets/2019/maodou-bot/maodou-api-notoken.png)

* 自带测试调用范例代码
![maodou-api-sample](/assets/2019/maodou-bot/maodou-api-sample.png)

* 部署一个Demo网页  
这方面可以参考讯飞开放平台的[Demo页面](https://www.xfyun.cn/services/lexicalAnalysis)。

## 开放问题讨论

* “有一天微信SDK开放了 wechat.say() 怎么办”  

> Wechaty这个项目之所以会存在，是因为微信没有开放底层聊天协议，但实际上目前除了微信，已经有很多开放平台，例如今日头条推出的飞书平台，已经提供了全套[机器人发送消息API](https://open.feishu.cn/document/ukTMukTMukTM/uUjNz4SN2MjL1YzM)。
> 如果微信也推出SDK，可以实现类似我们的 bot.say()，这样的话，Wechaty的使用价值，包括在此之上构建的 Bot App 都会面临着**大厦将倾**的危机。虽然@卓桓表示我们完全可以加入一个新的 wechaty-puppet-xxx 来对接微信自己的接口，从而保障之前的应用可以不受影响，但这真的可以长久吗？我比较担心，有一天新生代的程序员会不知道Wechay的存在。

* “像统一小程序开发一样统一chatbot”

> 由上面这个问题继续引发思考，提供 say() 接口的聊天机器人平台越来越多，同样的一个 chatbot 业务逻辑可能会面临着需要移植到各个平台上的工作。就像现在搞定了微信小程序之后，还需要写支付宝小程序、百度小程序、qq小程序等，终于滴滴的研发同学推出了跨端解决方案 [chameleon项目](https://github.com/didi/chameleon) 一统江湖，让一套代码可以运行多端。
> 基于 Wechaty 开发的 chatbot 未来有很多，而且很快除了微信平台大家也会需要一个维护一套代码就可以构建多个平台入口的解决方案。这个需求我们不妨把它称作 chateleon（取自 chatbot + chameleon）。这个聚合各大平台机器人聊天接口的中间抽象层，和 wechaty-puppet 层有些类似，未来承载着可以接入更多底层的聊天平台支持，从而有一天可以在这个基础上，长出一个像 BotHub 这样的开发者社区。

* “给Chatbot开发做一套最好的智能AI接口吧”

> 接着刚才上面的想法，BotHub 上构建的 chatbot 从业务上可能都需要一套 AI 智能接口，解决像 maodou-bot 一样类似的获取时间需求，包括词法分析和语义分析等等，如果每个开发 bot 业务逻辑的工程师，都要花费大量时间去评估底层 AI 接口的能力，这也将是重复找轮子的工作。
> 有没有一个专注于聊天场景的 AI 接口服务，提供绝大部分常见的 AI 接口，我们姑且给它取名 chaty.ai，可以帮助我们实现一个最好的 parseTime() 接口，我们只需要调用它去实现上层业务逻辑，而它只专注于寻找或者实现最好的AI算法来解决我们需要的接口问题。

最后一张图，描绘一下我理想中的大同世界。That's what I call **Future of Chatbot Friday** :-O
![maodou-bothub-arch.png](/assets/2019/maodou-bot/maodou-bothub-arch.png)
