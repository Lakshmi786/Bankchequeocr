#!/usr/bin/env python
# coding: utf-8


import pytesseract
from PIL import Image
import requests
from io import BytesIO
import cv2
import numpy as np

def extract_mcr(image):
    image.shape
    (h, w,) = image.shape[:2]
    delta = int(h - (h * 0.15))
    bottom = image[delta:h, 0:w]
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    mcr_code = pytesseract.image_to_string(image, lang = 'eng')
    return mcr_code
 
if __name__ == "__main__":
    image = cv2.imread('/bank-check-ocr-master/personal_check_single_preprinted_blank.jpg')
    mcr_code = extract_mcr(image)
    
    
    

