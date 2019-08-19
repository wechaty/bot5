---
title: 实现支持微信小程序的聊天机器人
author: 赵俊良
date: 2019-08-16 19:00 +0800
categories: talks
tags:
  - wechaty
  - miniprogram
  - time_nlp
header:
  teaser: /assets/2019/send-miniprogram/cover.png
---

<< 本次活动通知: [Bot Friday 第五弹](https://blog.chatie.io/bot-friday-fifth/) <<

## Bot Friday - 沙龙第5场分享

实现支持微信小程序的聊天机器人

2019-08-16 于北京微软，[zhaoic](https://github.com/zhaoic)

## 简介

由于项目的需求，接入了wechaty，感觉很好用，后来发现在发小程序部分还不能实现，在大神们的鼓励下，历经艰辛，改成了能用的状态。后来李卓桓建议我们提交PR，第一次给开源项目提交PR，本以为很简单，实际中也碰到了一些问题，好在都解决了。

## wechaty的小程序实现

### 开发环境的建立

新手做开发时，在这一步可能会花费大量的时间，我首次建立本地开发环境时，就花了一天的时间，这个时间完全可以节省下来，这里对wechaty-puppet-padpro本地开发环境的配置，做个简要说明，希望后续的开发者能更加容易的用wechaty做开发。

开发涉及到wechaty,wechaty-puppet,wechaty-puppet-padpro三个库，测试使用官方的wechaty-getting-started，各种关联错综复杂，这里需要感谢一下苏畅，在他的帮助下，我花了一天时间跑通了本地的开发环境，在捅破窗户纸之后，其实也很简单
各个库之间的关联如下图所示
![wechaty-link.jpg](/assets/2019/send-miniprogram/wechaty-link.jpg)

* wechaty,wechaty-puppet,wechaty-puppet-padpro这三个库在本地都需要
  * npm i && npm run dist && npm link
  * 改动代码后需要运行 npm run dist
  * npm i之后，需要运行npm link

* wechaty链接上本地库

```bash
npm link wechaty-puppet
npm link wechaty-puppet-padpro
```

* wechaty-getting-started链接上本地wechaty

```bash
npm link wechaty
```

即搭建好了开发环境，使用下面的命令即可开发测试，其中WECHATY_PUPPET_PADPRO_TOKEN需要获得有效的token

```bash
ECHATY_PUPPET=wechaty-puppet-padpro WECHATY_PUPPET_PADPRO_TOKEN=puppet_padpro_xxxx node examples/some-example.js
```

### 开发测试

小程序的payload接口的定义

```ts
export interface MiniProgramPayload {
    appid?          : string,    // optional, appid, get from wechat (mp.weixin.qq.com)
    description?    : string,    // optional, mini program title
    pagepath?       : string,    // optional, mini program page path
    thumbnailurl?   : string,    // optional, default picture, convert to thumbnail
    title?          : string,    // optional, mini program title
    username?       : string,    // original ID, get from wechat (mp.weixin.qq.com)
}
```

其中username和appid可以在小程序的后台获得，有这两项，就可以发送出小程序了，但是样子是这样的
![miniprogram-empty.jpg](/assets/2019/send-miniprogram/miniprogram-empty.jpg)

thumbnailurl是预留的，目前还不起作用，计划未来通过这个url传送一个图片，用于小程序的封面，其余各项对应关系如下图
![miniprogram-no-cover.jpg](/assets/2019/send-miniprogram/miniprogram-no-cover.jpg)

到这一步，由于无法自动生成cdnthumbnail相关的信息，小程序还不能显示出图片，为了满足业务的需要，我们通过分析小程序xml，提取出了相关数据，硬编码在padpro里，这样终于可以发送出一个相对完整的小程序了，缺点是图片是固定的。未来如果有高手熟悉小程序cdn这部分，可以继续完善padpro。
![miniprogram-padpro.jpg](/assets/2019/send-miniprogram/miniprogram-padpro.jpg)

关于wechaty-puppet-padpro中小程序的详细部分，可以参考[如何用PadPro实现发送微信小程序](https://blog.chatie.io/send-miniprogram-using-padpro/)

## 用正则表达式实现聊天机器人

我们目前的业务场景，还是比较简单的，程序里通过正则表达式就能比较好的满足我们的需求

### 对于时间的识别

毛豆少儿课堂小程序，初步是想通过识别出时间，设置课程提醒，所以对于时间的识别就很关键，经过测试对比，我们NLP最终选用了微软的[@microsoft/recognizers-text-suite](https://github.com/microsoft/Recognizers-Text)，微软NLP比较复杂，根据输入的文本，返回一个复杂的json值，在这个返回值中，找到需要字段中的时间。寻找优先级路径如下图，如果在datetime中找到有效时间，就返回，否则在time中查找，如此一级一级，如果所有字段都没有有效时间，返回空，不建立课程提醒。

![nlp-gettime.jpg](/assets/2019/send-miniprogram/nlp-gettime.jpg)

### 一些识别歧义的处理

在文本的识别中，有一些特殊需要处理的地方

* 特殊符号的处理

在微信文本中，经常会遇到一些表情符号，有可能会影响到识别，通过正则表达式，可以去除

```js
var msgText = originalText.replace(/<[^>]*>?/gm, '')
```

经实测，文本如果以空格开头，也会影响识别，下面是去除空格的正则表达式

```js
msgText = msgText.replace(/(^\s*)/g, '')
```

* 时间歧义
可以看到nlp解析出两个日期，上周日和本周日，一般我们认为是本周日，所以选用第二个结果
![time1.jpg](/assets/2019/send-miniprogram/time1.jpg)

根据提供日期和时间，可以分析出两种情况
第一种，有四个结果，第二个结果
![time1.jpg](/assets/2019/send-miniprogram/time1.jpg)

![time2.jpg](/assets/2019/send-miniprogram/time2.jpg)

![time3.jpg](/assets/2019/send-miniprogram/time3.jpg)

* 九号楼的歧义

```js
    var msgText2 = msgText.replace(/号楼/g, '#号楼')
```

![building9-1.jpg](/assets/2019/send-miniprogram/building9-1.jpg)

![building9-2.jpg](/assets/2019/send-miniprogram/building9-2.jpg)

* 2-6点歧义

```js
var msgText2 = msgText2.replace(/(\d+)\-(\d+)点/g, '$1点-$2点')
```

![timewithdash-1.jpg](/assets/2019/send-miniprogram/timewithdash-1.jpg)

![timewithdash-2.jpg](/assets/2019/send-miniprogram/timewithdash-2.jpg)

* 小助手新加好友的处理

```js
var msgText2 = msgText2.replace(/现在/g, '')
```

![newfriend-1.jpg](/assets/2019/send-miniprogram/newfriend-1.jpg)

![newfriend-2.jpg](/assets/2019/send-miniprogram/newfriend-2.jpg)

![newfriend-3.jpg](/assets/2019/send-miniprogram/newfriend-3.jpg)

### 与现有产品的挂接

现有产品

```js
    const reg = /zoom|视频会议|音频会议|演讲|群学习/g

    if(msgText.match(/直播/g)){
              let invite_url = '\n邀请连麦链接\nhttps://smh.maodou.io/invite/' + live_id + '/1234567890'
      let admin_url = '\n\n直播间后台链接\nhttps://smh.maodou.io/admin/content/course/' + live_id
        ....
    }
    else if(msgText.match(reg)){
      console.log(chalk.red('匹配到会议关键词'))
      let meeting_url
      if(msgText.match(/zoom|视频会议/g)){
        meeting_url = '\n视频会议链接\nhttps://kaihui.maodou.io/j/683175?mode=zoom'
      }
      else if(msgText.match(/音频会议/g)){
        meeting_url = '\n音频会议链接\nhttps://kaihui.maodou.io/j/683175?mode=audio'
      }
      else if(msgText.match(/演讲/g)){
        meeting_url = '\n演讲链接\nhttps://kaihui.maodou.io/j/683175?mode=lecture'
      }
      else if(msgText.match(/群学习/g)){
        meeting_url = '\n群学习链接\nhttps://kaihui.maodou.io/j/683175?mode=qunlearn'
      }
      .....
    }
```

## demo-毛豆课堂现场的快速体验

创建课程

![demo.jpg](/assets/2019/send-miniprogram/demo.jpg)

## 后续工作

* 完善小程序cdn图片

* 挂接讯飞stt语音转文字

* 聊天机器人训练引擎化
