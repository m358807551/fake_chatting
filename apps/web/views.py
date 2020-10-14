# coding=utf-8

"""视图."""
import json

from flask import Flask, render_template, request

app = Flask(
    __name__,
    static_folder='/Users/myp/code/wechat_simulator/wechat_simulator/apps/web/static',
    static_url_path='',
)


@app.route('/', methods=['GET'])
def index():
    """入口."""
    # 每行line都是一个对话
    data_str = request.args['data']
    data = json.loads(data_str)
    return render_template('wechat.html', data=data, zoom=1)


@app.route('/screenshot', methods=['GET'])
def screenshot():
    """专门用来大屏截图."""
    data_str = request.args['data']
    data = json.loads(data_str)
    return render_template('wechat.html', data=data, zoom=5)


@app.route('/wechat_edit', methods=['GET'])
def wechat_edit():
    """专门用来编辑页面."""
    return render_template('wechat_edit.html')


def main():
    """测试入口."""
    app.run()


if __name__ == '__main__':
    main()
