# coding==utf-8

"""核心内容."""
import json
import os
from copy import deepcopy

import pandas as pd


from settings import settings
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
    df['speaker_img'] = df['speaker_name'].apply(get_speaker_img)
    df['speaker_type'] = df['speaker_name'].apply(lambda x: 'me' if x == '我' else 'others')
    df['content_type'] = df['content'].apply(lambda x: 'img' if x.count('.') == 1 else 'text')
    df['time'] = '18:06'
    return df.to_dict('records')


def get_speaker_img(speaker_name):
    """通过发言人的名字得到其头像文件名."""
    filenames = os.listdir(settings.TOUXIANG_FOLDER)
    for filename in filenames:
        if speaker_name == filename.split('.')[0]:
            return filename
    return ''


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
                'path': os.path.join(settings.OUTPUT_FOLDER, '{0}.jpeg'.format(i)),
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


if __name__ == '__main__':
    main()
