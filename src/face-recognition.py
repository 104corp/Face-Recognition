# %%
import numpy as np
import cv2
import os

# get folder path
os.chdir('../')
cwd = os.getcwd() + '\\'
print('Current Folder Path' + cwd)
# %%
testCat = cv2.imread(cwd + 'img\cat.jpg')
cv2.imshow('TestOpenCv', testCat)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%


# %%
