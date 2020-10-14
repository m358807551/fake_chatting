# coding==utf-8

"""核心内容."""
import json

from copy import deepcopy

import imageio

import requests


def make_images():
    pass


def screenshot_wechat(data, img_name):
    """data是个配置字典，决定要显示的内容."""
    import asyncio
    from pyppeteer import launch

    async def _main():
        browser = await launch({'headless': True})
        page = await browser.newPage()
        url = 'http://127.0.0.1:5000/screenshot?data={data}'.format(data=json.dumps(data))
        await page.goto(url)
        quality = 100
        await page.screenshot(
            {'path': '{img_name}.jpeg'.format(img_name=img_name), 'type': 'jpeg', 'quality': quality, 'fullPage': True})
        await browser.close()

    asyncio.get_event_loop().run_until_complete(_main())


def create_gif(image_list, gif_name, duration=0.35):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


def main():
    # image_list = ['0.jpeg', '1.jpeg']
    # gif_name = 'aaa.gif'
    # duration = 2
    # create_gif(image_list, gif_name, duration)

    import cv2

    img_root = '/Users/myp/code/wechat_simulator/wechat_simulator/core'  # 这里写你的文件夹路径，比如：/home/youname/data/img/,注意最后一个文件夹要有斜杠
    fps = 1  # 保存视频的FPS，可以适当调整
    size = (375, 812)
    # 可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
    fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0')
    videoWriter = cv2.VideoWriter('3.avi', fourcc, fps, size)  # 最后一个是保存图片的尺寸

    for i in range(5):
        for _ in range(30):
            frame = cv2.imread(img_root + str(i) + '.jpeg')
            videoWriter.write(frame)
    videoWriter.release()


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
        screenshot_wechat(data_, i)


if __name__ == '__main__':
    main()
