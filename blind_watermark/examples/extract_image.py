from blind_watermark import WaterMark
import cv2
bwm1 = WaterMark(password_wm=1, password_img=1)
# notice that wm_shape is necessary
bwm1.extract(filename='output/embedded.png', wm_shape=(128, 128), out_wm_name='output/extracted.png', )