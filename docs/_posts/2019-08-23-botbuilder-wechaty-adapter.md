---
title: "Connect to Wechat: Bot Builder Adapter for Wechat Individual Account"
author: huan
categories: talks
tags:
  - botbuilder
  - botframework
  - wechat
  - wechaty
  - adapter
header:
  teaser: /assets/2019/botbuilder-wechaty-adapter/wechaty-connect-wechat.png
---

![BotBuilder Wechaty Adapter](https://raw.githubusercontent.com/huan/botbuilder-wechaty-adapter/HEAD/docs/images/botbuilder-wechaty.jpg)
> Source: [Time to do it differently, build chatbots with streams](http://fizzylogic.nl/2018/03/09/time-to-do-it-differently-build-chatbots-with-streams/)

Microsoft Bot Framework v4 adapter for Wechat **Individual** Account

If you are finding the Bot Framework v3 version of this adapter, please goto:

1. the [v3.0](https://github.com/huan/botbuilder-wechaty-adapter/tree/v3.0) branch, or
1. NPM [botbuilder-wechaty-connecter@3](https://www.npmjs.com/package/botbuilder-wechaty-connector)

## FEATURES

* Ready for Microsoft Bot Framework v4
* **no need a registered bot** on [dev.botframework.com](https://dev.botframework.com/), but require a wechat individual(NOT official!) account.
* Powered by [wechaty](https://github.com/chatie/wechaty)
* Support receiving and sending almost any wechat message types(WIP)

## INSTALLATION

```shell
npm install botbuilder-wechaty-adapter
```

## Preparation

We assume that, you already have a wechat individual account.

## Usage

**Step 1**, create your wechaty adapter:

```ts
import { WechatyAdapter } from "botbuilder-wechaty-adapter"

const adapter = new WechatyAdapter()
```

**Step 2**, start listening your wechaty adapter:

```ts
const closeFn = await adapter.listen(async (context: TurnContext) => {
  // ...
})
```

From there you can pass the `context` to your bot logic's `onTurn()` method.

### Attachment

To Be Supported.

## EXAMPLE

An example is located at `examples/` directory. Using following command to run it.

```shell
npm run example
```

```ts
import {
  ActivityTypes,
  TurnContext,
}                 from 'botbuilder'

import { WechatyAdapter } from 'botbuilder-wechaty-adapter'

export class EchoBot {

  public async onTurn (
    turnContext: TurnContext,
  ): Promise<void> {
    console.info('EchoBot', 'onTurn() %s', turnContext)
    if (turnContext.activity.type === ActivityTypes.Message) {
      const text = turnContext.activity.text
      console.info('RECV:', text)
      switch (text.toLowerCase()) {
        case 'quit':
          console.info('Quiting...')
          process.exit(0)
          break

        case 'ding':
          console.info('Replying `dong`...')
          await turnContext.sendActivity('dong')
          console.info('Replied.')
          break

        default:
          console.info('EchoBot', 'onTurn() skip message "%s"', text)
      }
    }
  }

}

const echoBot = new EchoBot()
const adapter = new WechatyAdapter()
adapter.listen(async (turnContext: TurnContext) => {
  await echoBot.onTurn(turnContext)
}).catch(console.error)

console.info('> Wechaty EchoBot is online. I will reply `dong` if you send me `ding`!')
console.info('> Say "quit" to end.\n')
```

## THANKS

This package is greatly inspired by:

1. [BotBuilder v4 - BotBuilderCommunity/botbuilder-community-js/botbuilder-adapters](https://github.com/BotBuilderCommunity/botbuilder-community-js/tree/master/libraries/botbuilder-adapters)

## ISSUES

Please feel free to [open issues](https://github.com/huan/botbuilder-wechaty-adapter/issues/new), if you have any suggestion.

## SEE ALSO

* [Create a bot with the Bot Builder SDK for Node.js](https://docs.microsoft.com/en-us/azure/bot-service/nodejs/bot-builder-nodejs-quickstart)
* [Key concepts in the Bot Builder SDK for Node.js](https://docs.microsoft.com/en-us/azure/bot-service/nodejs/bot-builder-nodejs-concepts)
* [VIDEO: Become a Bot Builder with Microsoft Bot Framework - James Mann speaking at dotnetsheff in April, 2017](https://pusher.com/sessions/meetup/dotnetsheff/become-a-bot-builder-with-microsoft-bot-framework)

## CHANGELOG

### v4.0 master

Upgrade to Microsoft BotBuilder v4

1. Package name was rename to `botbuilder-wechaty-adapter` from `botbuilder-wechaty-connect` for following the v4 naming style.

### v3.0 Jan 11, 2019

Release `botbuilder-wechaty-adapter@3.0` for BotBuilder v3

1. Work with Microsoft Bot Framework v3
1. Skip messages from other than a individual account(like official account, and SYS message)
1. Refactoring all the code from `ConsoleConnector`

### v0.0.1 Apr 17, 2018

1. Working with Wechaty Individual Text Messages.
1. An example run by `npm run example`

## TODO

* [ ] Add Room Message Support
* [ ] Add Full Message Types Support(current we only support text messages)

## AUTHOR

[Huan LI](http://linkedin.com/in/zixia) \<zixia@zixia.net\>, who is recognized as both [Microsoft Regional Director (RD)](https://rd.microsoft.com/en-us/huan-li) and [Microsoft Most Valuable Professional (MVP)](https://mvp.microsoft.com/en-us/PublicProfile/5003061) from Microsoft.

<a href="https://stackexchange.com/users/265499">
  <img src="https://stackexchange.com/users/flair/265499.png" width="208" height="58" alt="profile for zixia on Stack Exchange, a network of free, community-driven Q&amp;A sites" title="profile for zixia on Stack Exchange, a network of free, community-driven Q&amp;A sites">
</a>

## Slides

<div class="zoom-container" style="
    position: relative;
    padding-bottom:56.25%;
    padding-top:30px;
    height:0;
    overflow:hidden;
">
  <iframe
    src="https://docs.google.com/presentation/d/e/2PACX-1vQuR4VQbUXdS4rsVjTs7FDNwWbhRb1voaXBzMBsza62ukwwbppCN1D5DdxMym5PpcCG2lmub6-EQ0KX/embed?start=false&loop=false&delayms=3000"
    width='1306'
    height='763'
    allowfullscreen
    webkitallowfullscreen="true"
    mozallowfullscreen="true"
    webkitallowfullscreen="true"
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
