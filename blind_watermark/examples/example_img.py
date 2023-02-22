#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2

from blind_watermark import WaterMark
import os

original_pic = 'Lena_512x512'
original_wm = 'ztw19_QR'
embedded_pic = original_pic + original_wm + '_embedded'
extracted_wm = original_wm + '_extracted'

os.chdir(os.path.dirname(__file__))
bwm = WaterMark(password_wm=1, password_img=1)
# 读取原图
bwm.read_img(filename='pic/' + original_pic + '.jpg')
# 读取水印
bwm.read_wm('pic/' + original_wm + '.png')
# 打上盲水印
bwm.embed('output/' + embedded_pic + '.png')
wm_shape = cv2.imread('pic/' + original_wm + '.png', flags=cv2.IMREAD_GRAYSCALE).shape

# %% 解水印


bwm1 = WaterMark(password_wm=1, password_img=1)
# 注意需要设定水印的长宽wm_shape
bwm1.extract('output'+ embedded_pic + '.png', wm_shape=wm_shape, out_wm_name='output/' + extracted_wm + '.png', mode='img')
