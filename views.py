# coding=utf-8

"""封装视图."""
import json

from flask import Flask, render_template, request

app = Flask(
    __name__,
    static_folder='/Users/myp/code/fake_chatting/static',
    template_folder='/Users/myp/code/fake_chatting/templates',
    static_url_path='',
)


@app.route('/', methods=['GET'])
def index():
    """入口."""
    # 每行line都是一个对话
    # data_str = request.args['data']
    # data = json.loads(data_str)
    return render_template('wechat.html', data={'lines': []}, zoom=1)


@app.route('/screenshot', methods=['GET'])
def screenshot():
    """专门用来大屏截图."""
    data = json.loads(request.args['data'])
    # data = {}
    return render_template('wechat.html', data=data, zoom=5)


def main():
    """测试入口."""
    app.run()


if __name__ == '__main__':
    main()
