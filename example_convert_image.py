import numpy as np
import skimage.io
from mask_rcnn.ez import EZ

ez = EZ()

image_filename = 'sample_images/sample4.jpg'
sample_image_input = skimage.io.imread(image_filename)
sample1_result, info = ez.detect(sample_image_input)
skimage.io.imsave('output_image.jpg', sample1_result)
