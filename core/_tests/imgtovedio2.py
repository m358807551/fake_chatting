from skvideo.io import VideoWriter
import numpy
writer = VideoWriter(filename, frameSize=(w, h))
writer.open()
image = numpy.zeros((h, w, 3))
writer.write(image)
writer.release()
