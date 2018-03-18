# Packaged Mask Rcnn

version: dev

Packaged Mask Rcnn code for easier access

## Usage

Copy mask_rcnn folder to project and use it as module

You will need to install pycocotools and tensorflow

Other requirements you can refer to `requirements.txt`

## Examples

### convert image

```python

import numpy as np
import skimage.io
from mask_rcnn.ez import EZ

ez = EZ()

image_filename = 'sample_images/sample2.jpg'
sample_image_input = skimage.io.imread(image_filename)
sample1_result, info = ez.detect(sample_image_input)
skimage.io.imsave('output_image.jpg', sample1_result)
```

### convert video

```python

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
```

### from webcam

```python

import imageio
import visvis as vv
from mask_rcnn.ez import EZ

ez = EZ()

reader = imageio.get_reader('<video0>')
init_img = reader.get_next_data()
init_out, info = ez.detect(init_img)
t = vv.imshow(init_out, clim=(0, 255))
for im in reader:
    vv.processEvents()
    current_out, current_info = ez.detect(im)
    t.SetData(current_out)
```

### simple usecase

```python

import numpy as np
import matplotlib.pyplot as plt

"""
To use the easy access to mask rcnn, we need to import the module
using the following import command. Make sure you have mask_rcnn folder
under your main project directory.
"""
from mask_rcnn.ez import EZ

"""
First we need to init the object. By doing this, the standard coco weights
will be downloaded to the root project directory, and then it will be loaded.
"""
ez = EZ()

"""
The simple usecase is to just feed in the relative path to the image data
that we want to mask.
"""
sample1_result, info = ez.detect('sample_images/sample1.jpg')

"""
By setting merge_image to False, the first output will be None, and second
output will be bounding boxes, masks, and scores.
"""
sample1_result, info = ez.detect('sample_images/sample1.jpg', merge_image=False)

"""
The first input can also be a image array as numpy array with shape (W, H, 3)
Note that normalization is not necessary. It will be done in the function.
With this option, we can also set merge_image to False to avoid unnecessary
processing time.
"""
import skimage.io
sample_image_input = skimage.io.imread('sample_images/sample1.jpg')
sample1_result, info = ez.detect(sample_image_input)

if type(sample1_result) is np.ndarray:
    print('output image shape: ', sample1_result.shape)
print('info fields: ', info.keys())
```

