# 用requests模块处理更多请求与下载方式

之前我们通常使用 Python 的自带模块 urllib, 来提交网页请求。
这个模块能满足我们大部分的需求，但是为了满足你日益膨胀的其他需求，比如向网页发送信息，上传图片等等，
我们还有一个伟大的Python外部模块requests来有效的处理这些问题。

## 多功能的 Requests

## 获取网页的方式
在加载网页的时候，有几种不同类型，而这几种类型就是你打开网页的关键。
最重要的类型是
* get
* post
requests模块可以方便地向服务器发送不同类型的请求。

### Install requests

```
pip install requests
```

### requests get request

### requests post request

Access this page, fill in first name, last name and click submit

https://pythonscraping.com/pages/files/form.html

How to use requests to send this post request?

* 首先我们调出浏览器的 inspect （右键点击 inspect）
* 然后发现我们填入姓名的地方原来是在一个`<form>`里面
* 这个`<form>`里面有一些`<input>`tag, `name="firstname"` 和 `name="lastname"`, 这两个就是我们要 post 提交上去的关键信息了
* 我们填好姓名, 为了记录点击 submit 后, 浏览器究竟发生了什么变化, 我们在 inspect 窗口,
    * 选择 Network,
    * 勾选 Preserve log
    * 再点击 submit

你就能看到服务器返回给你定制化后的页面时, 你使用的方法和数据.
