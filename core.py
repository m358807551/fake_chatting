# coding==utf-8

"""核心内容."""
import json
import os
from copy import deepcopy

import pandas as pd


FOLDER_INPUT = '/Users/myp/code/fake_chatting/data/input'


def to_chattings():
    """获得对话."""
    return [
        {
            'speaker_name': '王凡凡',
            'speaker_img': '王凡凡.jpeg',
            'content': '人世几回伤往事',
            'content_type': 'text',
            'time': '18:06',
        }
    ]


def xls_to_chattings(xls_name):
    """从xls解析出对话."""
    xls_name = xls_name.split('.xls')[0]
    xls_path = os.path.join(FOLDER_INPUT, '{0}.xls'.format(xls_name))
    df = pd.read_excel(xls_path)
    df = df.rename(columns={'发言人': 'speaker_name', '内容': 'content'})
    df['speaker_img'] = '王凡凡.jpeg'
    df['content_type'] = 'text'
    df['time'] = '18:06'
    return df.to_dict('records')


xls_to_chattings('测试用的对话')


def to_jpegs(data):
    """
    data是个配置字典，决定要显示的内容.

    data: {
        'room_name': 'abc',
        'chattings': [..., ...]
    }
    """
    import asyncio
    from pyppeteer import launch

    async def _main():
        browser = await launch({'headless': True})
        page = await browser.newPage()
        new_chattings = []
        for i, chatting in enumerate(data['chattings']):
            print(i)
            new_chattings.append(chatting)
            new_data = {'room_name': data['room_name'], 'chattings': new_chattings}
            url = 'http://127.0.0.1:5000/screenshot?data={0}'.format(json.dumps(new_data))
            await page.goto(url)
            quality = 100
            await page.screenshot({
                'path': '{0}.jpeg'.format(i),
                'type': 'jpeg',
                'quality': quality,
                'fullPage': True,
            })
        await browser.close()

    asyncio.get_event_loop().run_until_complete(_main())


def main():
    """测试入口."""
    chattings = xls_to_chattings('测试用的对话')
    data = {'room_name': 'ABCF', 'chattings': chattings}
    to_jpegs(data)


def main2():
    """测试入口."""
    data = {
        'lines': [
            {
                'speaker': {
                    'name': '王凡凡',  # 说话的用户名
                    'type': 'others',  # 只能是 me 或者others. 其余按 others 看待，me的话会忽视name.
                    'img': 'touxiang6.jpeg',  # 头像名
                },
                'content': {
                    'type': 'text',  # 只能是 text 或者 img, 表示文字或者图片.
                    'text': '我是小猪',  # 仅在 type 是 text的时候生效
                    'img': '',  # 仅在 type 是 img 的时候生效
                }
            },
            {
                'speaker': {
                    'name': '',  # 说话的用户名
                    'type': 'me',  # 只能是 me 或者others. 其余按 others 看待，me的话会忽视name.
                    'img': 'touxiang4.jpeg',  # 头像名
                },
                'content': {
                    'type': 'text',  # 只能是 text 或者 img, 表示文字或者图片.
                    'text': '啊啊啊啊啊啊啊啊啊啊你们不要这样纸',  # 仅在 type 是 text的时候生效
                    'img': '',  # 仅在 type 是 img 的时候生效
                }
            },
            {
                'speaker': {
                    'name': '高芸芸',  # 说话的用户名
                    'type': 'others',  # 只能是 me 或者 others. 其余按 others 看待，me的话会忽视name.
                    'img': 'touxiang5.jpeg',  # 头像名
                },
                'content': {
                    'type': 'img',  # 只能是 text 或者 img, 表示文字或者图片.
                    'text': '',  # 仅在 type 是 text的时候生效
                    'img': 'doutu1.jpeg',  # 仅在 type 是 img 的时候生效
                }
            },
            {
                'speaker': {
                    'name': '',  # 说话的用户名
                    'type': 'me',  # 只能是 me 或者others. 其余按 others 看待，me的话会忽视name.
                    'img': 'touxiang4.jpeg',  # 头像名
                },
                'content': {
                    'type': 'text',  # 只能是 text 或者 img, 表示文字或者图片.
                    'text': '🙂hello?',  # 仅在 type 是 text的时候生效
                    'img': '',  # 仅在 type 是 img 的时候生效
                }
            },
            {
                'speaker': {
                    'name': '',  # 说话的用户名
                    'type': 'me',  # 只能是 me 或者others. 其余按 others 看待，me的话会忽视name.
                    'img': 'touxiang4.jpeg',  # 头像名
                },
                'content': {
                    'type': 'img',  # 只能是 text 或者 img, 表示文字或者图片.
                    'text': '',  # 仅在 type 是 text的时候生效
                    'img': 'doutu2.jpeg',  # 仅在 type 是 img 的时候生效
                }
            },
        ]
    }
    for i in range(len(data['lines'])):
        data_ = deepcopy(data)
        data_['lines'] = data['lines'][: i+1]
        to_jpegs(data_, i)


if __name__ == '__main__':
    main()
