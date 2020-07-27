# %%
import numpy as np
import cv2

# %%
img = cv2.imread('cat.jpg')

# %%
cv2.imshow('window_name', img)
cv2.waitKey(0)
# %%
