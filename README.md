## 简介

最近在用`墨墨背单词`这个单词软件，各方面做的都很好。可惜存在单词上限，每背一个单词，就少一个，如果没有任何增加单词上限的途径的话，只能背500个单词你就可以删软件了。。

除了签到以及印章连连看的方式之外，还有没有增加上限的途径呢？是有的，就是每次打完卡之后可以对当日的学习情况进行分享。这个页面一旦被浏览过一次，你的单词上限就会+1（当然，一个ip只算一次），每日上限20个。于是我就写了一个自动刷访问量的脚本，原本是单线程的，很慢，后来再修改了一下弄成多线程的了。大体思路是：

1. 去免费代理ip网站爬代理
2. 利用代理访问文章
3. 增加访问量

多线程利用的自然是生产者-消费者模型。实现得有点简陋，正好最近在线程进程这边补缺补漏，就当练手了吧。

均在linux下运行（unix或许也行

需要安装：

`pip install termcolor`

 MoMo-aiohttp.py在Py3.x下运行，需要安装aiohttp

### 版本

1. `MoMo.py` 自己实现的多线程访问
2. `MoMo-aiohttp.py` 利用aiohttp实现的协程访问（在数量较小的情况下，和1差不多，但是数量上去了，差别会越来越大）

## 运行示例

![example](https://github.com/Macr0phag3/MoMo/blob/master/PicForREADME/example.png)