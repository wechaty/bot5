---
title: 用Snowboy打造自己的树莓派语音助手
author: lhr0909
date: 2019-08-09 14:40 +0800
categories: talks
tags:
  - bot
  - chatbot
  - hotword
  - snowboy
  - voice assistant
  - 语音助手
  - 树莓派
  - raspberry pi
header:
  teaser: /assets/2019/snowboy-demo/jarvis-india.jpg
---

## 设想

一个聊天机器人（Chatbot）需要理解自然语言，并作出对应的回复。一个chatbot模块可以拆解成如下部分：

![Chatbot](/assets/2019/snowboy-demo/chatbot.png)

在开发者的世界里面，现在已经有不少开源的工具可以制作chatbot模块，各大云平台上也已经有各种各样的云服务来支持，对接到市面上的聊天平台上。在工作中，也
经常和Slack上面的机器人打交道，并且通过机器人在开发和运维流程里面做各种提醒和自动化。

现在各种各样的语音助手也开始出现在我们的身边，像小度和小爱，像Siri，还有Alexa和Google Home等设备。我还记得我买回来的第一个Amazon Echo，
尝试对着它说各种各样的话，看看怎么样回复，朋友也经常恶作剧，来到我家通过Echo给我在亚马逊下了各种各样的订单。手机上的Hey Siri和OK Google也非常
方便，尽管只是设一下闹钟或者是做一些功能。

作为一个开发者，和漫威电影的爱好者，我经常在想有没有办法做一个属于自己的语音助手，像钢铁侠电影里面的Jarvis和Friday一样。对于我来说，一个
voice chatbot可以拆解成下面的部分：

![Voice Chatbot](/assets/2019/snowboy-demo/voice-chatbot.png)

看起来，我只需要把每个部件连接起来，然后放到一个机器上面跑就可以了！但是想了一下，又想到了一个问题，这个语音助手需要像市面上的设备一样，需要唤醒。
如果没有唤醒步骤，一直做监听的话，对存储资源和网络连接的需求是非常大的。经过一番搜索之后，我找到了[Snowboy](https://snowboy.kitt.ai/)。

Snowboy是[kitt.ai](https://kitt.ai)制作的一个热词检测库 (Hotwords Detection Library)。通过训练热词之后，可以离线运行，并且
[功耗很低](http://docs.kitt.ai/snowboy/#what-s-the-cpu-ram-usage)，可以支持在树莓派等设备上运行。官方提供Python, Golang, NodeJS, iOS
和Android的wrapper可以整合到代码里面。

## 实践

于是我就拿出了尘封已久的树莓派，连上了麦克风和音箱，开始自己倒腾能不能做出来一个简单的能听懂我说话的小Jarvis。最近也入购了一个iPad Pro，所以
我准备直接通过iPad Pro连接树莓派进入ssh编程，顺便练一下vim，哈哈。

![The Setup](/assets/2019/snowboy-demo/setup.jpg)

下面列举一下配置：

* Board: [NanoPi K1 Plus](https://www.friendlyarm.com/index.php?route=product/product&product_id=220) - 特别喜欢友善之臂的板子，
性价比高。这个板子有2G内存，有Wi-Fi + Ethernet（需要网线接口连接iPad），甚至带有板载麦克风。搭配的OS是UbuntuCore 16.04 LTS，可以通过`apt`安装绝大部分的依赖。
* Microphone: [Blue Snowball](https://www.bluedesigns.com/products/snowball/) - 因为我主要在家办公，所以经常需要视频会议。
Blue的麦克风是USB连接的，在Linux下可以免驱直接使用。

根据上图Voice Chatbot的拆解，我决定把以下这几个服务连接起来测试一下完整流程：

* Hotword Detection: Snowboy
* Speech-to-Text: [科大讯飞语音听写](https://www.xfyun.cn/services/voicedictation)
* Chatbot: [图灵机器人](http://www.turingapi.com/)
* Text-to-Speech: [科大讯飞在线语音合成](https://www.xfyun.cn/services/online_tts)

机器启动之后安装[nvm](https://github.com/nvm-sh/nvm) 用最新版的NodeJS v10 LTS。然后创建 `package.json` 并安装 `snowboy` nodejs wrapper:

```shell
npm init
npm install snowboy --save
```

需要详细读取文档安装所有Snowboy编译所需的依赖（TODO）。依赖安装完之后，我们参考一下Snowboy的[sample](https://github.com/Kitt-AI/snowboy/blob/master/examples/Node/microphone.js)代码：

```javascript
// index.js

const record = require('node-record-lpcm16');
const Detector = require('snowboy').Detector;
const Models = require('snowboy').Models;

const models = new Models();

models.add({
  file: 'resources/models/snowboy.umdl',
  sensitivity: '0.5',
  hotwords : 'snowboy'
});

const detector = new Detector({
  resource: "resources/common.res",
  models: models,
  audioGain: 2.0,
  applyFrontend: true
});

detector.on('silence', function () {
  console.log('silence');
});

detector.on('sound', function (buffer) {
  // <buffer> contains the last chunk of the audio that triggers the "sound"
  // event. It could be written to a wav stream.
  console.log('sound');
});

detector.on('error', function () {
  console.log('error');
});

detector.on('hotword', function (index, hotword, buffer) {
  // <buffer> contains the last chunk of the audio that triggers the "hotword"
  // event. It could be written to a wav stream. You will have to use it
  // together with the <buffer> in the "sound" event if you want to get audio
  // data after the hotword.
  console.log(buffer);
  console.log('hotword', index, hotword);
});

const mic = record.start({
  threshold: 0,
  verbose: true
});

mic.pipe(detector);
```

因为这个sample没有指定`node-record-lpcm16`的版本号，经过一番调试发现新版1.x版本已经改了API，所以我这边翻了一下文档才发现API的改动：

```javascript
// index.js

const { record } = require('node-record-lpcm16');

const mic = record({
  sampleRate: 16000,
  threshold: 0.5,
  recorder: 'rec',
  device: 'plughw:CARD=Snowball',
}).stream();
```

这里加了一些新的参数，首先是指定Snowball的硬件ID，这个硬件ID可以通过`arecord -L`命令找到。另外设置了16k的采样率，
因为Snowboy的model都是用16k采样率的音频来训练的，采样率不一致就识别不出来。另外把阈值调高了一些，阻挡一些噪音。

按照[文档](https://github.com/kitt-ai/snowboy#pretrained-universal-models)修改使用Jarvis的模型，并调整灵敏度参数：

```javascript
// index.js

models.add({
  file: 'snowboy/resources/models/jarvis.umdl',
  sensitivity: '0.8,0.80',
  hotwords : ['jarvis', 'jarvis'],
});
```

使用Jarvis模型测试之后发现已经可以识别Jarvis的hotword，并且触发`hotword`回调。这里我想了一下，我需要把音频流保存下来，然后传到讯飞进行听写获取文字。
所以当`hotword`事件触发的时候，需要把mic的流转移到一个`fsWriteStream`里面写入音频文件。Snowboy的Detector也有`sound`和`silence`的回调，所以我通过一个
简单的flag来实现了语音录制，并在说话结束的时候传到讯飞的听写API。

```javascript
// index.js

const { xunfeiTranscriber } = require('./xunfei_stt');

let audios = 0;
let duplex;
let silenceCount;
let speaking;

const init = () => {
  const filename = `audio${audios}.wav`;
  duplex = fs.createWriteStream(filename, { binary: true });
  silenceCount = 0;
  speaking = false;
  console.log(`initialized audio write stream to ${filename}`);
};

const transcribe = () => {
  console.log('transcribing');
  const filename = `audio${audios}.wav`;
  xunfeiTranscriber.push(filename);
};

detector.on('silence', function () {
  if (speaking) {
    if (++silenceCount > MAX_SILENCE_COUNT) {
      mic.unpipe(duplex);
      duplex.destroy();
      transcribe();
      audios++;
      init();
    }
  }
  console.log('silence', speaking, silenceCount);
});

detector.on('sound', function (buffer) {
  if (speaking) {
    silenceCount = 0;
  }

  console.log('sound');
});

detector.on('hotword', function (index, hotword, buffer) {
  if (!speaking) {
    silenceCount = 0;
    speaking = true;
    mic.pipe(duplex);
  }

  console.log('hotword', index, hotword);
});

mic.pipe(detector);
init();
```

上面这段代码里面`xunfeiTranscriber`就是我们的讯飞听写模块。因为现在存的是一个音频文件，所以如果API是直接把整个音频传过去然后获得文字的话，是
最舒服的。但是很遗憾，讯飞弃用了REST API，而转用了基于WebSocket的流式听写API，所以只能老老实实手撸一个client。这里我用了`EventEmitter`来做
消息通信，这样可以比较快地和主程序互通信息。

```javascript
// xunfei_stt.js

const EventEmitter = require('events');
const WebSocket = require('ws');

let ws;
let transcriptionBuffer = '';

class XunfeiTranscriber extends EventEmitter {
  constructor() {
    super();
    this.ready = false;
    this.on('ready', () => {
      console.log('transcriber ready');
      this.ready = true;
    });
    this.on('error', (err) => {
      console.log(err);
    });
    this.on('result', () => {
      cleanupWs();
      this.ready = false;
      init();
    });
  }

  push(audioFile) {
    if (!this.ready) {
      console.log('transcriber not ready');
      return;
    }

    this.emit('push', audioFile);
  }
}

function init() {
  const host = 'iat-api.xfyun.cn';
  const path = '/v2/iat';

  const xunfeiUrl = () => {
    return `ws://${host}${path}?host=${host}&date=${encodeURIComponent(dateString)}&authorization=${authorization}`;
  };

  const url = xunfeiUrl();

  console.log(url);

  ws = new WebSocket(url);

  ws.on('open', () => {
    console.log('transcriber connection established');
    xunfeiTranscriber.emit('ready');
  });

  ws.on('message', (data) => {
    console.log('incoming xunfei transcription result');

    const payload = JSON.parse(data);

    if (payload.code !== 0) {
      cleanupWs();
      init();
      xunfeiTranscriber.emit('error', payload);
      return;
    }

    if (payload.data) {
      transcriptionBuffer += payload.data.result.ws.reduce((acc, item) => {
        return acc + item.cw.map(cw => cw.w);
      }, '');

      if (payload.data.status === 2) {
        xunfeiTranscriber.emit('result', transcriptionBuffer);
      }
    }
  });

  ws.on('error', (error) => {
    console.log(error);
    cleanupWs();
  });

  ws.on('close', () => {
    console.log('closed');
    init();
  });
}

const xunfeiTranscriber = new XunfeiTranscriber();

init();

module.exports = {
  xunfeiTranscriber,
};
```

处理`push`事件这个地方比较棘手，经过测试发现，讯飞听写API只支持每条websocket消息发送13k的音频信息。音频信息是通过base64编码的，所以每条最多只能发大概9k字节。
这里需要根据讯飞API文档进行分批发送，并且在最后一定需要发end frame，不然API会超时导致关闭。返回的文字也是分段的，所以需要一个buffer来存储，等全部文字都返回之后再拼接输出。

```javascript
// xunfei_stt.js

const fs = require('fs');

xunfeiTranscriber.on('push', function pushAudioFile(audioFile) {
  transcriptionBuffer = '';

  const audioPayload = (statusCode, audioBase64) => ({
    common: statusCode === 0 ? {
      app_id: process.env.XUNFEI_APPID,
    } : undefined,
    business: statusCode === 0 ? {
      language: 'zh_cn',
      domain: 'iat',
      ptt: 0,
    } : undefined,
    data: {
      status: statusCode,
      format: 'audio/L16;rate=16000',
      encoding: 'raw',
      audio: audioBase64,
    },
  });

  const chunkSize = 9000;
  const buffer = new Buffer(chunkSize);

  fs.open(audioFile, 'r', (err, fd) => {
    if (err) {
      throw err;
    }

    let i = 0;

    function readNextChunk() {
      fs.read(fd, buffer, 0, chunkSize, null, (errr, nread) => {
        if (errr) {
          throw errr;
        }

        if (nread === 0) {
          console.log('sending end frame');

          ws.send(JSON.stringify({
            data: { status: 2 },
          }));

          return fs.close(fd, (err) => {
            if (err) {
              throw err;
            }
          });
        }

        let data;
        if (nread < chunkSize) {
          data = buffer.slice(0, nread);
        } else {
          data = buffer;
        }

        const audioBase64 = data.toString('base64');
        console.log('chunk', i, 'size', audioBase64.length);
        const payload = audioPayload(i >= 1 ? 1 : 0, audioBase64);

        ws.send(JSON.stringify(payload));
        i++;

        readNextChunk();
      });
    }

    readNextChunk();
  });
});
```

细心的同学应该留意到有些重启逻辑在这段代码里面，这是因为测试过程中，发现讯飞这个API每个连接只支持发送一条消息，接受新的音频流需要重新连接API。。。
所以只好在每条消息发送完之后主动关闭WebSocket连接。

接下来是整合图灵机器人获取回复的部分了，`xunfeiTranscriber`提供一个`result`事件，所以这里通过监听`result`事件，把消息收到之后传入图灵机器人。

```javascript
// index.js

const { tulingBot } = require('./tuling_bot');

xunfeiTranscriber.on('result', async (data) => {
  console.log('transcriber result:', data);
  const response = await tulingBot(data);
  console.log(response);
});
```

```javascript
// tuling_bot.js

const axios = require('axios');

const url = 'http://openapi.tuling123.com/openapi/api/v2';

async function tulingBot(text) {
  const response = await axios.post(url, {
    reqType: 0,
    perception: {
      inputText: {
        text,
      },
    },
    userInfo: {
      apiKey: process.env.TULING_API_KEY,
      userId: 'myUser',
    },
  });

  console.log(JSON.stringify(response.data, null, 2));
  return response.data;
}

module.exports = {
  tulingBot,
};
```

对接完图灵机器人之后，我们需要把图灵机器人返回的文字进行语音合成。这里讯飞语音合成的WebAPI还是基于REST的，也已经有人做了对应的开源实现了，所以比较简单。

```javascript
// index.js

const { xunfeiTTS } = require('./xunfei_tts');

xunfeiTranscriber.on('result', async (data) => {
  console.log('transcriber result:', data);
  const response = await tulingBot(data);

  const playVoice = (filename) => {
    return new Promise((resolve, reject) => {
      const speaker = new Speaker({
        channels: 1,
        bitDepth: 16,
        sampleRate: 16000,
      });
      const outStream = fs.createReadStream(filename);
      // this is just to activate the speaker, 2s delay
      speaker.write(Buffer.alloc(32000, 10));
      outStream.pipe(speaker);
      outStream.on('end', resolve);
    });
  };

  for (let i = 0; i < response.results.length; i++) {
    const result = response.results[i];
    if (result.values && result.values.text) {
      const outputFilename = await xunfeiTTS(result.values.text, `${audios-1}-${i}`);
      if (outputFilename) {
        await playVoice(outputFilename);
      }
    }
  }
});
```

```javascript
// xunfei_tts.js
const fs = require('fs');
const xunfei = require('xunfeisdk');
const { promisify } = require('util');

const writeFileAsync = promisify(fs.writeFile);

const client = new xunfei.Client(process.env.XUNFEI_APPID);
client.TTSAppKey = process.env.XUNFEI_TTS_KEY;

async function xunfeiTTS(text, audios) {
  console.log('turning following text into speech:', text);

  try {
    const result = await client.TTS(
      text,
      xunfei.TTSAufType.L16_16K,
      xunfei.TTSAueType.RAW,
      xunfei.TTSVoiceName.XiaoYan,
    );

    console.log(result);

    const filename = `response${audios}.wav`;

    await writeFileAsync(filename, result.audio);

    console.log(`response written to ${filename}`);

    return filename;
  } catch (err) {
    console.log(err.response.status);
    console.log(err.response.headers);
    console.log(err.response.data);

    return null;
  }
}

module.exports = {
  xunfeiTTS,
};
```

最后这个机器人就可以听懂我说的话啦！

下面附上[完整代码](https://github.com/xanthous-tech/snowboy-rpi-demo)

## 后记

我觉得整体的运行效果还是不错的，并且可以高度自定义。我希望后面再测试一下其他不同厂商的语音API，并且对接上Rasa和Wechaty，这样在家里就可以和机器人对话，
并且能够在微信里面获得一些图文的信息。讯飞的API整合出乎意料之外地复杂，并且有一个我觉得比较致命的问题是，讯飞的WebAPI连接延时特别严重，我一开始以为是
板子的问题，后面发现单独调用图灵API和讯飞API，发现图灵API的响应速度非常快，但是讯飞API就在连接上就花了很长时间，所以现在的STT模块需要预热，等连接准备
好才可以说话。后面我想换用其他厂商的API，看看能不能改善一下体验。

希望这个demo能够起到一个抛砖引玉的作用，在未来可以看到更多更酷炫的语音助手和机器人。

## 链接

* [Original](https://x-tech.io/zh/posts/voice-chatbot-snowboy/)
