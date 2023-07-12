#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install opencv-python


# In[ ]:


import numpy as np
import cv2


# In[ ]:


image=cv2.imread(r'C:\Users\SAHYADRI\Pictures\images.jfif')
print(image)


# In[ ]:


angle = 90
scale = 1
tx, ty = 100, 50


# In[ ]:


(h, w) = image.shape[:2]


# In[ ]:


M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, scale)
M


# In[ ]:


rotated_img = cv2.warpAffine(image, M, (w, h))
#translated_img = cv2.warpAffine(rotated_img, np.float32([[1, 0, tx], [0, 1, ty]]), (w, h))


# In[ ]:


cv2.imshow('Original Image', image)
cv2.imshow('Rotated, Scaled', rotated_img)


# In[ ]:



cv2.destroyAllWindows()


# In[ ]:


import cv2
 
# Reading the image
image = cv2.imread(r'C:\Users\SAHYADRI\Pictures\images.jfif')
 
# dividing height and width by 2 to get the center of the image
height, width = image.shape[:2]
# get the center coordinates of the image to create the 2D rotation matrix
center = (width/2, height/2)
 
# using cv2.getRotationMatrix2D() to get the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)
 
# rotate the image using cv2.warpAffine
rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))
 
a=cv2.imshow('Original image', image)
b=cv2.imshow('Rotated image', rotated_image)
print(a)
print(b)
# wait indefinitely, press any key on keyboard to exit
cv2.waitKey(0)
# save the rotated image to disk
cv2.imwrite('rotated_image.jpg', rotated_image)


# In[ ]:




