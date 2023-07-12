#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from PIL import Image #Python Imaging Library


# In[7]:


A_gray = Image.open(r"C:\Users\SAHYADRI\Pictures\Saved Pictures\small-fuffy-dog-breeds-1623362663.jpg")
A_gray = A_gray.convert('L')

temp = np.asarray(A_gray.getdata(), dtype=np.float64).reshape((A_gray.size[1], A_gray.size[0]))
A_gr = np.asarray(temp, dtype=np.uint8)


# In[8]:




plane7 = A_gr & 128*np.ones(np.shape(A_gr)).astype('uint8')
plane6 = A_gr &  64*np.ones(np.shape(A_gr)).astype('uint8')
plane5 = A_gr &  32*np.ones(np.shape(A_gr)).astype('uint8')
plane4 = A_gr &  16*np.ones(np.shape(A_gr)).astype('uint8')
plane3 = A_gr &   8*np.ones(np.shape(A_gr)).astype('uint8')
plane2 = A_gr &   4*np.ones(np.shape(A_gr)).astype('uint8')
plane1 = A_gr &   2*np.ones(np.shape(A_gr)).astype('uint8')
plane0 = A_gr &   1*np.ones(np.shape(A_gr)).astype('uint8')


# In[9]:


plt.figure(figsize=(20,7))
plt.subplot(2, 4, 1)
plt.imshow(plane7, cmap='gray')
plt.title('Plane 7 (MSB)')
plt.subplot(2, 4, 2)
plt.imshow(plane6, cmap='gray')
plt.title('Plane 6')
plt.subplot(2, 4, 3)
plt.imshow(plane5, cmap='gray')
plt.title('Plane 5')
plt.subplot(2, 4, 4)
plt.imshow(plane4, cmap='gray')
plt.title('Plane 4')
plt.subplot(2, 4, 5)
plt.imshow(plane3, cmap='gray')
plt.title('Plane 3')
plt.subplot(2, 4, 6)
plt.imshow(plane2, cmap='gray')
plt.title('Plane 2')
plt.subplot(2, 4, 7)
plt.imshow(plane1, cmap='gray')
plt.title('Plane 1')
plt.subplot(2, 4, 8)
plt.imshow(plane0, cmap='gray')
plt.title('Plane 0 (LSB)');


# In[ ]:




