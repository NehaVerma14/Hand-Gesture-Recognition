#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# path_videos
# path_labels
# path_train
# path_validation
# path_test
class DataLoader():
 def __init__(self, path_vid, path_labels, path_train=None, path_val=None, path_test=None):
     self.path_vid = path_vid
     self.path_labels = path_labels
     self.path_train = path_train
     self.path_val = path_val
     self.path_test = path_test
     
     self.get_labels(path_labels)
     
     # create dataframes if the paths exist
     if self.path_train:
         self.train_df = self.load_video_labels(self.path_train)
     if self.path_val:
         self.val_df = self.load_video_labels(self.path_val)
     if self.path_test:
         self.test_df = self.load_video_labels(self.path_test, mode="input")
     
 def get_labels(self, path_labels):
     # load labels into dataframe
     self.labels_df = pd.read_csv(path_labels, names=['label'])
     # extract labels from dataframe
     self.labels = [str(label[0]) for label in self.labels_df.values]
     self.n_labels = len(self.labels)
     # create dictionaries to convert label to integer
     self.label_to_int = dict(zip(self.labels, range(self.n_labels)))
     # create dicionaries to convert integer to label
     self.int_to_label = dict(enumerate(self.labels))
     #dictionary={0:Swiping Left}
             
     
     
 def load_video_labels(self, path_subset, mode='label'):
     if mode=='Input':
         names=["video_id"]
     elif mode=='label':
         names=["video_id","label"]
     
     df=pd.read_csv(path_subset, sep=';' , names=names)   
     
     if mode=='label':
         df=df[df.label.isin(self.labels)]
         
     return df
 
     


# In[ ]:




