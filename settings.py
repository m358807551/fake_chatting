# coding=utf-8

"""配置."""
import os


class BasicSettings(object):
    BASIC_FOLDER = '/Users/myp/code/fake_chatting'

    TOUXIANG_FOLDER = None
    # 存储运行结果的文件夹
    OUTPUT_FOLDER = None


def _update(x):
    x.TOUXIANG_FOLDER = os.path.join(x.BASIC_FOLDER, 'static/images/touxiang')
    x.OUTPUT_FOLDER = os.path.join(x.BASIC_FOLDER, 'data/output')


settings = BasicSettings

_update(settings)
