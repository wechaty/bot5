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

## wechaty的小程序实现

由于项目的需求，接入了wechaty，感觉很好用，后来发现在发小程序部分还不能实现，在大神们的鼓励下，历经艰辛，改成了能用的状态。后来李卓桓建议我们提交PR，第一次给开源项目提交PR，本以为很简单，实际中也碰到了一些问题，好在都解决了。

### 开发环境的建立

新手做开发时，在这一步可能会花费大量的时间，我首次建立本地开发环境时，就花了一天的时间，这个时间完全可以节省下来，这里对wechaty-puppet-padpro本地开发环境的配置，做个简要说明，希望后续的开发者能更加容易的用wechaty做开发。

开发涉及到wechaty,wechaty-puppet,wechaty-puppet-padpro三个库，测试使用官方的wechaty-getting-started，各种关联错综复杂，这里需要感谢一下苏畅，在他的帮助下，我也花费了一天时间才跑通，但是在捅破窗户纸之后，发现其实也很简单

各个库之间的关联

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

小程序的payload接口的定义如下

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

还有一些文本信息，如果以空格开头，也会影响识别，下面是去除开头空格的正则表达式

```js
msgText = msgText.replace(/(^\s*)/g, '')
```

* 时间歧义

在`周日晚上6:30`这种语言环境下，晚上6:30没有歧义，但是周日，可以看到nlp解析出两个日期，上周日和本周日，一般本周日才是我们要表达的，所以此处选用第二个结果

![time1.jpg](/assets/2019/send-miniprogram/time1.jpg)

在`6月9日10点`这种语言环境下，会产生两个歧义四种结果，今年或明年的6月9日，上午或下午10点，所以可以看到识别的结果是四个，第二个结果正好巧合是我们需要的。

![time2.jpg](/assets/2019/send-miniprogram/time2.jpg)

而换成`6月9日22点`这种语言描述，时间的歧义没有了，会返回两个年的结果，今年或明年的6月9日，按照之前惯例，仍然选用第二个识别结果，就会产生误差，明年的6月9日，明显不是需要的结果。

![time3.jpg](/assets/2019/send-miniprogram/time3.jpg)

* 九号楼的歧义

在实际测试中，在时间前会出现`某某号楼`这样的词语，例如下面的实例，出现`九号楼`，会导致识别成日期9日

![building9-1.jpg](/assets/2019/send-miniprogram/building9-1.jpg)

为了避免类似问题，通过正则表达式，在号楼前加入#,可以较好的解决这类问题。

```js
    var msgText2 = msgText.replace(/号楼/g, '#号楼')
```

![building9-2.jpg](/assets/2019/send-miniprogram/building9-2.jpg)

* 2-6点歧义

在时间识别中，还有类似`2-6点`这种描述，NLP会识别出6点，而我们想要的却是开始时间2点

![timewithdash-1.jpg](/assets/2019/send-miniprogram/timewithdash-1.jpg)

通过正则表达式，将 `(数字)-(数字)点` 这种描述，改写成 `(数字)点-(数字)点`，就能较好的识别出开始时间

```js
var msgText2 = msgText2.replace(/(\d+)\-(\d+)点/g, '$1点-$2点')
```

![timewithdash-2.jpg](/assets/2019/send-miniprogram/timewithdash-2.jpg)

* 小助手新加好友的处理

由于和客户沟通的入口，都放在微信小助手，而小助手新加好友后，微信会有自动回复：`我通过了您的朋友验证请求，现在我们可以开始聊天了`，其中关键词`现在`，会导致识别出当前时间，让小助手创建提醒，并推送给新加好友，造成不好的体验。

![newfriend-1.jpg](/assets/2019/send-miniprogram/newfriend-1.jpg)

![newfriend-2.jpg](/assets/2019/send-miniprogram/newfriend-2.jpg)

然而关键字`现在`也很重要，所以这里通过正则表达式，将`现在我们`删除，防止错误的识别，同时也能保留关键词`现在`

```js
var msgText2 = msgText2.replace(/现在我们/g, '')
```

![newfriend-3.jpg](/assets/2019/send-miniprogram/newfriend-3.jpg)

### 与现有产品的挂接

经过前面的处理后，如果正确识别出了时间，就可以根据句子中的关键词，给用户推送相应的服务。目前小助手支持会议模式，直播模式和课堂模式。

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
      .....
    }
```

实际测试效果，如下图所示

![linktomaodou.jpg](/assets/2019/send-miniprogram/linktomaodou.jpg)

## demo-毛豆课堂现场的快速体验

最后，在现场做了一个[毛豆课堂](https://maodouketang.com)的demo，通过和小助手互动，我创建了课程和小程序提醒，将小程序推送给现场嘉宾，加入小程序提醒后，会收到短信上课提醒，通过短信中的链接，能很快速进入课堂进行互动。

![demo.jpg](/assets/2019/send-miniprogram/demo.jpg)

## 后续工作

目前，wechaty发送微信小程序，毛豆小助手的时间识别，还有许多需要改进的地方。我们希望逐步的完善，找到一个最佳的体验。

* 完善小程序cdn图片
小程序的图片cdn地址，目前在wechaty-puppet-padpro中无法生成，如果有熟悉这部分的高手，可以接着完善

* 挂接讯飞stt语音转文字
毛豆小助手，目前只能识别分析文本信息，计划未来可以接入讯飞语音转文字接口，让小助手具有更佳的用户体验

* 聊天机器人训练引擎化
将代码引擎化，通过配置文件或api进行训练与更新，能让非技术人员也方便的完善机器人的训练
