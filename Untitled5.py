#!/usr/bin/env python
# coding: utf-8

# In[19]:



from skimage.color import rgb2gray
import numpy as numpy
import cv2
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy import ndimage

image=plt.imread(r'C:\Users\Devarun\Desktop\1.jpeg')

plt.imshow(image)


# In[20]:


gray = rgb2gray(image)
plt.imshow(gray, cmap='gray')


# In[21]:


gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
for i in range(gray_r.shape[0]):
    if gray_r[i]>gray_r.mean():
        gray_r[i] = 1
    else:
        gray_r[i]=0
gray=gray_r.reshape(gray.shape[0],gray.shape[1])
plt.imshow(gray,cmap = 'gray')


# In[22]:


gray = rgb2gray(image)
gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
for i in range(gray_r.shape[0]):
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 3
    elif gray_r[i] > 0.5:
        gray_r[i] = 2
    elif gray_r[i] > 0.25:
        gray_r[i] = 1
    else:
        gray_r[i] = 0
gray = gray_r.reshape(gray.shape[0],gray.shape[1])
plt.imshow(gray, cmap='gray')


# In[ ]:




