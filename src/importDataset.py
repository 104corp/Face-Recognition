# %%
from PIL import Image
import glob

# %%
# get folder path
os.chdir('../')
# %%
cwd = os.getcwd()

print("Current Folder Path:  " + cwd)
# %% import whole img
image_list_part1 = []
for filename in glob.glob(cwd + "//dataset//0001-3000//*.jpg"):
    im = Image.open(filename)
    image_list_part1.append(im)

# %%
image_list_part2 = []
for filename in glob.glob(cwd + "//dataset//3001-6000//*.jpg"):
    im = Image.open(filename)
    image_list_part2.append(im)

# %%
image_list_part3 = []
for filename in glob.glob(cwd + "//dataset//6001-9000//*.jpg"):
    im = Image.open(filename)
    image_list_part3.append(im)

# %%
image_list_part4 = []
for filename in glob.glob(cwd + "//dataset//9001-13322//*.jpg"):
    im = Image.open(filename)
    image_list_part4.append(im)
