import cv2
import numpy as np
import os

path = '/Users/myp/code/wechat_simulator/wechat_simulator/core/'
filelist = os.listdir(path)

fps = 1  # 视频每秒24帧
size = (2048, 1024)  # 需要转为视频的图片的尺寸
# fourcc = cv2.VideoWriter_fourcc(*"MJPG")
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter('output.mov', fourcc, fps, size)

# 视频保存在当前目录下
for item in filelist:
    if item.endswith('jpeg'):
        item = path + item
        # 路径为中文名
        # img = cv2.imdecode(np.fromfile(item, dtype=np.uint8), 1)
        # 路径为英文名
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()
