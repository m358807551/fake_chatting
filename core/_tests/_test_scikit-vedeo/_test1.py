import numpy as np
import skvideo

from skvideo.io import vwrite

outputdata = np.random.random(size=(5, 480, 680, 3)) * 255
outputdata = outputdata.astype(np.uint8)

skvideo.io.vwrite("outputvideo.mp4", outputdata)
