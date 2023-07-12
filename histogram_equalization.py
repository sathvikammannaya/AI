#!/usr/bin/env python
# coding: utf-8

# In[1]:


from skimage import io
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


img = io.imread(r"C:\Users\SAHYADRI\Pictures\Saved Pictures\small-fuffy-dog-breeds-1623362663.jpg")
io.imshow(img)


# In[4]:


plt.figure(figsize=(5,5))
plt.hist(img.flatten(),bins=256)
plt.xlabel('before')
plt.show()


# In[5]:


nk = np.linspace(0,0,256)
nk2 = np.linspace(0,0,256)
prrk = np.linspace(0,0,256)
prsk = np.linspace(0,0,256)
sk = np.linspace(0,0,256)
sk2 = np.linspace(0,0,256)
m = np.linspace(0,0,256)


# In[6]:


for i in range(256):
    for j in range(256):
        nk[img[i][j]] = nk[img[i][j]] + 1
for i in range(256):
    prrk[i] = (nk[i]/65536)
    if i == 0:
        sk2[i] = prrk[i]
    else: 
        sk2[i] = (prrk[i] + sk2[i-1])
    m[i] = int((255)*sk2[i]+0.5)
for i in range(256):
    for j in range(256):
        img[i][j] = m[img[i][j]]
for i in range(256):
    for j in range(256):
        nk2[img[i][j]] = nk2[img[i][j]] + 1 
tot = 0
for i in range(256):
    prsk[i] = (nk2[i]/65536)
io.imshow(img)
plt.figure(figsize=(5,5))
plt.hist(img.flatten(),bins=256)
plt.xlabel('after')
plt.show()


# In[ ]:




