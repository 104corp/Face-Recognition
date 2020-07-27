# %%
import cv2
import pandas as pd
import numpy as np
import matplotlib as plt

# %%
haarcascade_frontalface_default_path = "D:\\workspace_python\\Face-Recognition\\src\\detective\\haarcascade_frontalface_default.xml"

# %%
# load parameter from opcv
face_cascade = cv2.CascadeClassifier(haarcascade_frontalface_default_path)
face_cascade.load(haarcascade_frontalface_default_path)

# Read the input image

# imgPath = "\\dataset\\testCat.jpg"
imgPath = "\\dataset\\6001-9000\\06009A46.jpg"
img = cv2.imread(cwd + imgPath)
# img = image_list_part1[0]

# %%
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# %%
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# %%
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()

# %%
