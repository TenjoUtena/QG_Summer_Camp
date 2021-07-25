# FLASK

### run方法参数

| 参数    | 说明                                      | 默认值    |
| ------- | ----------------------------------------- | --------- |
| debug   | 代码更新是否自动重启                      | False     |
| theaded | 是否开启多线程                            | False     |
| port    | 指定端口                                  | 5000      |
| host    | 指定主机（设置0.0.0.0可以通过本地IP访问） | 127.0.0.1 |



### Flask HTTP方法

| 序号 | 方法与描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | **GET**以未加密的形式将数据发送到服务器。最常见的方法。      |
| 2    | **HEAD**和GET方法相同，但没有响应体。                        |
| 3    | **POST**用于将HTML表单数据发送到服务器。POST方法接收的数据不由服务器缓存。 |
| 4    | **PUT**用上传的内容替换目标资源的所有当前表示。              |
| 5    | **DELETE** 删除由URL给出的目标资源的所有当前表示。           |



-   **Form** - 它是一个字典对象，包含表单参数及其值的键和值对。
-   **args** - 解析查询字符串的内容，它是问号（？）之后的URL的一部分。
-   **Cookies** - 保存Cookie名称和值的字典对象。
-   **files** - 与上传文件有关的数据。
-   **method** - 当前请求方法。

```python
#设置cookies
@app.route("/set_cookies/")
#cookies: name = utena
def set_cookie():
    resp = make_response('success')
    resp.set_cookie('name', 'utena', max_age=3600)
    return resp

#获取cookies
@app.route("/get_cookies/")
def get_cookie():
    cookie_1 = request.cookies.get('name')
    return cookie_1

#删除cookie
@app.route("/delete_cookies/")
def delete_cookie():
    resp = make_response('del success')
    resp.delete_cookie('name')
    return resp
```

```python
#会话session登录登出
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return '登录用户名是:' + username + '<br>' + "<b><a href = '/logout'>点击这里注销</a></b>"
    return "您暂未登录， <br><a href = '/login'></b>" + "点击这里登录</b></a>"
    
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action = "" method = "post">
        <p><input type ="text" name ="username"/></p>
        <p><input type ="submit" value ="登录"/></p>
        </form>
       '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
```

```python
@app.route('/postID/<int:postID>')
def show_blow(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' %revNo
```

**redirect()**函数的原型：

```
Flask.redirect(location, statuscode, response)
```

-   **location**参数是应该重定向响应的URL。
-   **statuscode**发送到浏览器标头，默认为302。
-   **response**参数用于实例化响应。



上传文件

```python
#记得头文件
import os
from werkzeug.utils import secure_filename

#c
app.config['UPLOAD_FOLDER'] = './'

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        #暂时存贮文件
        f = request.files['file']
        print(request.files)
        #存贮文件
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'
    else:
        return render_template('upload.html')
```