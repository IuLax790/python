import signal

import skimage
from matplotlib import pylab
from skimage.color import rgb2gray

print(skimage.__version__)
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageChops import add, subtract, multiply, difference, screen
import PIL.ImageStat as stat
from skimage.io import imread, imsave, imshow, show, imread_collection, imshow_collection
from skimage import color, viewer, exposure, img_as_float, data
from skimage.transform import SimilarityTransform, warp, swirl
from skimage.util import invert, random_noise, montage
import matplotlib.image as mpimg
import matplotlib.pylab as plt
from scipy.ndimage import affine_transform, zoom
from scipy import misc

img = Image.open("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Documents\\GitHub\\Computer_Vision_Images\\Dogs (1).png")
# read the image, provide the correct path
print(img.width, img.height, img.mode, img.format, type(img))
# 453 340 RGB PNG <class 'PIL.PngImagePlugin.PngImageFile'>
print(img.show()) # display the image

im_g = img.convert('L') # convert the RGB color image to a grayscale image
im_g.save("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Documents\\GitHub\\Computer_Vision_Images\\Dogs (1).png") # save the image to disk
Image.open("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Documents\\GitHub\\Computer_Vision_Images\\Dogs (1).png").show() # read the grayscale image from disk and show

img = mpimg.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Documents\\GitHub\\Computer_Vision_Images\\Dogs (1).png") # read the image from disk as a numpy ndarray
print(img.shape, img.dtype, type(img)) # this image contains an α channel, hence num_channels= 4
# (960, 1280, 4) float32 <class 'numpy.ndarray'>
plt.figure(figsize=(10,10))
plt.imshow(img) # display the image
plt.axis('off')
plt.show()

im1 = img
im1[im1 < 0.5] = 0 # make the image look darker
plt.imshow(im1)
plt.axis('off')
plt.tight_layout()
plt.savefig("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Documents\\GitHub\\Computer_Vision_Images\\Dogs (1).png") # save the dark image
plt.close()
img = mpimg.imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Documents\\GitHub\\Computer_Vision_Images\\Dogs (1).png") # read the dark image
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis('off') # no axis ticks
plt.tight_layout()
plt.show()


img = rgb2gray(imread("C:\\Users\\idoch\\OneDrive - Bar-Ilan University\\Documents\\GitHub\\Computer_Vision_Images\\Dogs (1).png")).astype(float)
print(np.max(img))
print(img.shape)
blur_box_kernel = np.ones((3,3)) / 9
edge_laplace_kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
im_blurred = signal.convolve2d(img, blur_box_kernel)
im_edges = np.clip(signal.convolve2d(img, edge_laplace_kernel), 0, 1)
fig, axes = pylab.subplots(ncols=3, sharex=True, sharey=True, figsize=(18,6))
axes[0].imshow(img, cmap=pylab.cm.gray)
axes[0].set_title('Original Image', size=20)
axes[1].imshow(im_blurred, cmap=pylab.cm.gray)
axes[1].set_title('Box Blur', size=20)
axes[2].imshow(im_edges, cmap=pylab.cm.gray)
axes[2].set_title('Laplace Edge Detection', size=20)
for ax in axes:
    ax.axis('off')
print(pylab.show())