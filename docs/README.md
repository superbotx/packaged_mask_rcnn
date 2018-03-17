# Packaged Mask Rcnn

version: dev

Packaged Mask Rcnn code for easier access

## Usage

Copy mask_rcnn folder to project and use it as module

You will need to install pycocotools and tensorflow

Other requirements you can refer to `requirements.txt`

## Examples

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

