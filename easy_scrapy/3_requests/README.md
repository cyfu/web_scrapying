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

```html
<form method="post" action="processing.php">
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname"><br>
<input type="submit" value="Submit" id="submit">
</form>
```

### Upload file

传照片也是 post 的一种, 我们得将本地的照片文件传送到服务器. 我们使用这个网页来模拟一次传照片的过程.

https://pythonscraping.com/pages/files/form2.html

```html
<form action="processing2.php" method="post" enctype="multipart/form-data">
  Submit a jpg, png, or gif: <input type="file" name="uploadFile"><br>
  <input type="submit" value="Upload File">
</form>
```

### Log in website with cookie
用 post 还有一个重要的作用, 就是模拟登录.

https://pythonscraping.com/pages/cookies/login.html

我们总结一下, 为了这次登录账号, 我们的浏览器做了什么.
1. 使用 post 方法登录了第一个红框的 url
2. post 的时候, 使用了 Form data 中的用户名和密码
3. 生成了一些 cookies

cookies 的传递也特别重要, 比如我用 requests.post + payload 的用户信息发给网页, 返回的 r 里面会有生成的 cookies 信息.
接着我请求去登录后的页面时, 使用 request.get, 并将之前的 cookies 传入到 get 请求. 这样就能已登录的名义访问 get 的页面了.

### Log in website with session
每次都要传递 cookies 是很麻烦的, 好在 requests 有个很 handy 的功能, 那就是 Session. 在一次会话中, 我们的 cookies 信息都是相连通的, 它自动帮我们传递这些 cookies 信息.
创建完一个 session 过后, 我们直接只用 session 来 post 和 get. 而且这次 get 的时候, 我们并没有传入 cookies. 但是实际上 session 内部就已经有了之前的 cookies 了.

## Download file

今天我们来爬这张图, 还有下载这张图.

我们首先要到这张图所在的[网页](https://mofanpy.com/learning-steps/),找出图片的link。然后使用get请求下载图片。


![莫烦Python的个性化学习路线](https://static.mofanpy.com/img/description/learning_step_flowchart.png)