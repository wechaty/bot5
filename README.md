# BOT Friday CLUB Website [![NPM](https://github.com/wechaty/bot5.ml/actions/workflows/npm.yml/badge.svg)](https://github.com/wechaty/bot5.ml/actions/workflows/npm.yml)

[![Powered by Wechaty](https://img.shields.io/badge/Powered%20By-Wechaty-brightgreen.svg)](https://github.com/Wechaty/wechaty)

## Voice of Members

> "Bot Friday 是支撑我每周活下去的动力" [link](https://www.bot5.club/events/seminar-minutes-19/)  
> &mdash; <cite>[@尹伯昊](https://github.com/rickyyin98), [奇迹创坛](https://www.miracleplus.com/)首席实习生</cite>
>

## Bot Domain

- [.BOT is an identity for bots.](https://www.amazonregistry.com/bot) - Currently, anyone who owns, operates or manages bots published using a supported tool (Amazon Lex, Botkit Studio, Dialogflow, Gupshup, Microsoft Bot Framework, and Pandorabots) can validate a bot and register a .BOT domain name.

## Usage

### Jekyll

Install all the Jekyll requirements and run it at localhost for blog preview.

#### 1 Use Docker Compose

This is the recommended way for new users to easy getting started

```sh
make docker
```

#### 2 ~~Install Jekyll by Hand~~

You should not use this way except you are a Ruby expert.

```sh
make install
make serve
```

### Test

In order to make sure everything(file name, file size, etc) is ok, you can run the following command to check them before `git push`.

```sh
npm install
npm test
```

## Viewers

### Slide Viewer

[Viewer.js](https://viewerjs.org/) is the best easy to use.

Others:

1. [reveal.js - The HTML Presentation Framework](https://revealjs.com) Used by slides.com
1. [PDF.js JSFiddle Example](https://jsfiddle.net/pdfjs/wagvs9Lf) from [PDF.js Examples 3](https://mozilla.github.io/pdf.js/examples/)
1. [Online PowerPoint to HTML5 Converter](https://www.digitalofficepro.com/powerpoint/powerpoint-to-html5-converter.html)
1. [React MDX-based presentation decks](https://github.com/jxnblk/mdx-deck)
1. [WikiPedia:Web-based slideshow](https://en.wikipedia.org/wiki/Web-based_slideshow)

## Resources

1. [Jekyll cheatsheet](https://devhints.io/jekyll)
1. [Jekyll Liquid Cheatsheet](https://gist.github.com/JJediny/a466eed62cee30ad45e2)
1. [Minimal Mistakes Official Examples](https://mmistakes.github.io/minimal-mistakes/year-archive/)

## Troubleshooting

### `scripts/fit-image.sh` Realted

Linux

```sh
sudo apt-get install imagemagick
sudo apt-get install webp
```

Mac

```sh
brew install imagemagick
```

### Jekyll Related

If you have a question about using Jekyll, start a discussion on the [Jekyll Forum](https://talk.jekyllrb.com/) or [StackOverflow](https://stackoverflow.com/questions/tagged/jekyll). Other resources:

- [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
- [Setting up a Jekyll site with GitHub Pages](https://jekyllrb.com/docs/github-pages/)
- [Configuring GitHub Metadata](https://github.com/jekyll/github-metadata/blob/master/docs/configuration.md#configuration) to work properly when developing locally and avoid `No GitHub API authentication could be found. Some fields may be missing or have incorrect data.` warnings.

## Contributors

[![contributor](https://sourcerer.io/fame/huan/wechaty/bot5.club/images/0)](https://sourcerer.io/fame/huan/wechaty/bot5.club/links/0)
[![contributor](https://sourcerer.io/fame/huan/wechaty/bot5.club/images/1)](https://sourcerer.io/fame/huan/wechaty/bot5.club/links/1)
[![contributor](https://sourcerer.io/fame/huan/wechaty/bot5.club/images/2)](https://sourcerer.io/fame/huan/wechaty/bot5.club/links/2)
[![contributor](https://sourcerer.io/fame/huan/wechaty/bot5.club/images/3)](https://sourcerer.io/fame/huan/wechaty/bot5.club/links/3)
[![contributor](https://sourcerer.io/fame/huan/wechaty/bot5.club/images/4)](https://sourcerer.io/fame/huan/wechaty/bot5.club/links/4)
[![contributor](https://sourcerer.io/fame/huan/wechaty/bot5.club/images/5)](https://sourcerer.io/fame/huan/wechaty/bot5.club/links/5)
[![contributor](https://sourcerer.io/fame/huan/wechaty/bot5.club/images/6)](https://sourcerer.io/fame/huan/wechaty/bot5.club/links/6)
[![contributor](https://sourcerer.io/fame/huan/wechaty/bot5.club/images/7)](https://sourcerer.io/fame/huan/wechaty/bot5.club/links/7)

## Author

[Huan LI (李卓桓)](http://linkedin.com/in/zixia) <zixia@zixia.net>

[![Profile of Huan LI (李卓桓) on StackOverflow](https://stackexchange.com/users/flair/265499.png)](https://stackexchange.com/users/265499)

## Copyright & License

- Code & Docs © 2019 - now Huan LI <zixia@zixia.net>
- Code released under the Apache-2.0 License
- Docs released under Creative Commons
