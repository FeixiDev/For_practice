from flask import Flask, render_template, request, jsonify,url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('ajaxIndex.html')


# 特别注意的是request.args['**']获取get请求的参数
# request.form['**']获取post请求的参数,request.values['**']可以获得两种方式的参数

@app.route('/ajax')
def ajax():
    return 'get获取到' + request.args['name']


# 当两种方式分开写时函数注意不要重名
@app.route('/ajax', methods=['POST'])
def ajax_post():
    # return 'post获取到' + request.values['name']
    name=request.values['name']
    password=request.values['password']
    print("name:",name)
    if name == 'zgx':
        if password =='123':
            return "true"
    else:
        return "False"
@app.route('/user_info',methods=['GET'])
def user_info():
    return render_template('user_info.html')
    
if __name__ == '__main__':
    app.run()