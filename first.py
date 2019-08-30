#!/usr/bin/env python3
# from flask import Flask,render_template,url_for
#
#
# app = Flask(__name__)  # 创建一个Web应用
# app.config['DEBUG'] = True
#
# @app.route('/')
# @app.route('/user/')
# def user():
#     print(url_for('user',id=10,name='XeanYu',age=16))
#     return 'Test'
# def index():
#     return render_template("index.html",name='Stronger') # 模板名称为 index.html
#
# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port=8080,debug=True)  # 运行，指定监听地址为 127.0.0.1:8080


# from flask import Flask, url_for, redirect,abort
#
# app = Flask(__name__)
#
#
# # @app.route('/', methods=['GET', 'POST'])
# @app.route('/')
# def index():
#     return redirect(url_for('user'))
#
#
# @app.route('/user/')
# def user():
#     # abort(401)放弃请求并返回错误代码，用 abort() 函数
#     return 'This is User'
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)
# Get
# from flask import Flask, request
#
# app = Flask(__name__)
#
#
# @app.route('/get/', methods=['GET'])
# def index():
#     name = request.args.get('name')
#     age = request.args.get('age')
#     print("name: %s \nage: %s " % (name, age))
#     return 'OK'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
# Post
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/get/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        print("POST 方法 \nname: %s \nage: %s" % (name, age))

        return '已经获取数据'


if __name__ == '__main__':
    app.run(debug=True)