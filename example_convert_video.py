import numpy as np
import imageio
from mask_rcnn.ez import EZ

imageio.plugins.ffmpeg.download()
filename = 'sample_images/sample_video1.MOV'
video = imageio.get_reader(filename)
meta = video.get_meta_data()
skip = 1
size = 5
fps = meta['fps'] // skip
f_cnt = meta['nframes'] // skip
writer = imageio.get_writer('output.mp4', fps=fps)

ez = EZ()

cnt = 0
for i, img in enumerate(video):
    if i % skip == 0:
        print(str(i // skip), '/', f_cnt)
        cnt += 1
        if cnt == size:
            break
        result, info = ez.detect(img)
        writer.append_data(result)

writer.close()
