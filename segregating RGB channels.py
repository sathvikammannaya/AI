#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


# In[2]:


A = plt.imread(r"C:\Users\SAHYADRI\Pictures\Saved Pictures\small-fuffy-dog-breeds-1623362663.jpg")
plt.imshow(A)
plt.show()


# In[3]:


A_red = A[:, :, 0]
A_green = A[:, :, 1]
A_blue = A[:, :, 2]

plt.figure()
plt.imshow(A_red, cmap='gray') #For a single channel / grayscale image you need to mention the colourmap
plt.title('The RED channel')

plt.figure()
plt.imshow(A_green, cmap='gray')
plt.title('The GREEN channel')

plt.figure()
plt.imshow(A_blue, cmap='gray')
plt.title('The BLUE channel')

plt.show()


# In[ ]:




