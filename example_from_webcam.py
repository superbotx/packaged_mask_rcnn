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
