#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import numpy as np
from tabulate import tabulate
import os


# In[2]:


dst_img = r"C:\Users\SAHYADRI\Pictures"

arr = np.array(Image.open(os.path.join(dst_img, "images.jfif")))
print(arr.shape)
print(arr.ndim)


# In[ ]:




