#!/usr/bin/env python
# coding: utf-8

# ## **Detectando objetos com YOLO v4**

# **Etapa 1 - Download do Darknet**

# In[15]:


get_ipython().system('git clone https://github.com/AlexeyAB/darknet')


# In[16]:


#cd darknet


# In[17]:


#ls


# **Etapa 2 - Compilando a biblioteca**

# In[18]:


get_ipython().system("sed -i 's/OPENCV=0/OPENCV=1/' Makefile")
get_ipython().system("sed -i 's/GPU=0/GPU=1/' Makefile")
get_ipython().system("sed -i 's/CUDNN=0/CUDNN=1' Makefile")


# In[19]:


import tensorflow as tf
device_name = tf.test.gpu_device_name()
print(device_name)


# In[20]:


get_ipython().system('make')


# **Etapa 3 - Baixando os pesos do modelo pré-treinado**

# In[21]:


from google.colab import drive
drive.mount('/content/gdrive')


# !mkdir darknet
# !cd darknet
# !wget -r -np -nH --cut-dirs=3 -R index.html https://github.com/AlexeyAB/darknet/

# 

# 

# In[22]:


import zipfile
path = "/content/gdrive/MyDrive/YOLO/modelo_YOLOv4.zip"
zip_object = zipfile.ZipFile(file = path, mode = "r")
zip_object.extractall("./")
zip_object.close()


# **Etapa 4 - Carregando o vídeo**

# 4.1 - De uma url

# In[25]:


get_ipython().system('wget http://github/gabevr/yolo/raw/master/videos/video_teste02.mp4')


# 4.2 - Do Google Drive

# In[26]:


get_ipython().system('cp /content/gdrive/MyDrive/YOLO/videos/video_teste02.mp4 ./')


# In[27]:


get_ipython().system('ls')


# **Etapa 5 - Realizando a detecção em vídeo**

# In[28]:


get_ipython().system('./darknet detector demo cfg/coco.data cfg/yolov4.cfg yolov4.weights -dont_show video_teste02.mp4 -i 0 -out_filename resultado.avi')


# In[29]:


get_ipython().system('du -h resultado.avi')


# **Etapa 6 - Visualizando o resultado**

# In[32]:


get_ipython().system('cp ./resultado.avi /content/gdrive/MyDrive/YOLO/videos/resultado1.avi')


# **Especificando um threshold**

# In[33]:


get_ipython().system('cp /content/gdrive/MyDrive/YOLO/videos/video_rua01.mp4 ./')


# In[35]:


get_ipython().system('./darknet detector demo cfg/coco.data cfg/yolov4.cfg yolov4.weights -dont_show video_rua01.mp4 -i 0 -out_filename resultado02.avi -thresh 0.3')


# In[36]:


get_ipython().system('cp ./resultado02.avi /content/gdrive/MyDrive/YOLO/videos/resultado1.avi')

