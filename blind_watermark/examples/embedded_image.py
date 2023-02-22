from blind_watermark import WaterMark
import cv2
bwm1 = WaterMark(password_wm=1, password_img=1)
# read original image
bwm1.read_img('./pic/ori_img.jpeg')
# read watermark
bwm1.read_wm('./pic/watermark.png')
# embed
bwm1.embed('./output/embedded.png')