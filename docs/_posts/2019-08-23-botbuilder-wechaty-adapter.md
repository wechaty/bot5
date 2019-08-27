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
  teaser: /assets/2019/botbuilder-wechaty-adapter/botbuilder-wechaty.jpg
---

Microsoft Bot Framework v4 adapter for Wechat **Individual** Account

- Github: <https://github.com/huan/botbuilder-wechaty-adapter>
- NPM: <https://www.npmjs.com/package/botbuilder-wechaty-adapter>

![BotBuilder Wechaty Adapter](/assets/2019/botbuilder-wechaty-adapter/wechaty-connect-wechat.png)

If you are finding the Bot Framework v3 version of this adapter, please goto:

1. the [v3.0](https://github.com/huan/botbuilder-wechaty-adapter/tree/v3.0) branch, or
1. NPM [botbuilder-wechaty-connecter@3](https://www.npmjs.com/package/botbuilder-wechaty-connector)

## FEATURES

- Ready for Microsoft Bot Framework v4
- **no need a registered bot** on [dev.botframework.com](https://dev.botframework.com/), but require a wechat individual(NOT official!) account.
- Powered by [wechaty](https://github.com/chatie/wechaty)
- Support receiving and sending almost any wechat message types(WIP)

## INSTALLATION

```shell
npm install botbuilder-wechaty-adapter
```

## Preparation

We assume that, you already have a wechat individual account.

## EXAMPLE

An example is located at `examples/` directory. Using following command to run it.

```shell
git clone git@github.com:huan/botbuilder-wechaty-adapter.git
cd botbuilder-wechaty-adapter
npm install
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

> [Connect to Wechat: Bot Builder Adapter for Wechat Individual Account](https://docs.google.com/presentation/d/1b294XdtThMUv0C9ePfQ61YOFTGVL_jFpDEduxX9-SfQ/edit?usp=sharing)
