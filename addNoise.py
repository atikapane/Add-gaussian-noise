import PIL
import os
import os.path
import skimage
import numpy as np
from PIL import Image
from skimage import util

f = r'D:/Kuliah/TA/testFrame'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = np.array(img)

    noise_img = util.random_noise(img,mode='gaussian', var=0.10)
    pil_image = Image.fromarray((noise_img * 255).astype(np.uint8))

    pil_image.save(f_img)