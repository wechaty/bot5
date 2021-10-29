---
title: "Pull Request Manual"
permalink: /manuals/pull-request/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/bot5-banner.png
#   actions:
#     - label: "Download"
#       url: "https://github.com/mmistakes/minimal-mistakes/"
  caption: "Photo credit: [slow-growing pilot](https://chatbotsmagazine.com/why-a-slow-growing-pilot-is-vital-for-chatbot-success-cce7875f93b3)"
excerpt: "How to send Pull Request"
toc: true
toc_label: "Pull Request Manual"
toc_icon: "tasks"  # corresponding Font Awesome icon name (without fa prefix)
---

## Pull Request Check List

参加 BOT5 沙龙需要提交 Pull Request。

在 <https://github.com/wechaty/bot5.ml> 项目中，以 Pull Request 的形式，将自己想分享的主题进行内容提交。

注意：请在各自的 Pull Request 的描述中，引用本会议纪要的 issue URL，以便于会议纪要进行追踪。

轮值主席在收到大家的PR后，在会议通知发送之前进行Merge。

注意：

1. 在各自的 Pull Request 的描述中，**引用本会议纪要的 issue URL**，以便于会议纪要进行追踪。
1. 会议纪要的内容，放在 `docs/_posts` 的目录下
1. 会议纪要的图片，放在 `docs/assets/对应年份的目录下`
1. CI 对文件名的要求：`/$[a-z0-9\-\.]+$/` 注意我们统一用 - 而不用 _
1. CI 对图片的要求：尺寸不能超过2MB；同时如果宽度超过了 1920 ，那么需要用 `./scripts/fit-image.sh` 处理一下，压缩到 1920 宽度的分辨率，以加快网页加载速度
1. 发起PR的时候可能会存在多条commit，所以在合并PR的时候，尽可能的选择`Squash and merge`，使得整个repo的commit history看起来更加清爽
1. 如何创建 PR，可以参考 [Github-Creating a pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
1. Pull Request 需要通过 CI (Continous Integration) testing 之后，才能被 merge
1. Pull Request 需要至少一个人 review approve 之后，才能 merge

有任何问题，大家可以随时在群里面提出讨论。

## Contributing

1. Fork it
1. Create your paper branch (git checkout -b my-new-paper)
1. Commit your changes (git commit -am 'Added some paper')
1. Push to the branch (git push origin my-new-paper)
1. Create a new Pull Request
