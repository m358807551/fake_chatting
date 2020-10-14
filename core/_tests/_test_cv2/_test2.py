import cv2

import numpy as np

img_root = '/Users/myp/code/wechat_simulator/wechat_simulator/data/'

writer = cv2.VideoWriter("output2.avi", cv2.VideoWriter_fourcc(*"MJPG"), 1, (1875, 4060))

for i in range(5):
    frame = cv2.imread(img_root + str(i) + '.jpeg')
    writer.write(frame)

writer.release()


# fps = 1  # 保存视频的FPS，可以适当调整
# zoom = 3
# size = (375 * zoom, 812 * zoom)
# # 可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
# fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0')
# videoWriter = cv2.VideoWriter('3.avi', fourcc, fps, size)  # 最后一个是保存图片的尺寸
#
# for i in range(5):
#     frame = cv2.imread(img_root + str(i) + '.jpeg')
#     videoWriter.write(frame)
# videoWriter.release()


#
#
# if __name__ == '__main__':
#     main()
