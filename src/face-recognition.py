# %%
import numpy as np
import cv2
import os
from PIL import Image
import glob
image_list = []
# %%
# get folder path
os.chdir('../')

# %% import whole img
image_list = []
for filename in glob.glob("dataset/*.jpg"):
    im = Image.open(filename)
    image_list.append(im)

# %%
