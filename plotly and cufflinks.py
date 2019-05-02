#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from plotly import __version__


# In[2]:


print(__version__)


# In[3]:


import cufflinks as cf


# In[4]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[5]:


init_notebook_mode(connected=True)


# In[6]:


cf.go_offline()


# In[7]:


df = pd.DataFrame(np.random.randn(100,4) , columns='A B C D'.split())


# In[8]:


df.head()


# In[9]:


df2 = pd.DataFrame({'Category':['A' ,'B' ,'C'] , 'values':[32,43,50]})


# In[10]:


df2


# In[11]:


df.plot()


# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


df.iplot()


# In[17]:


df.iplot(kind='scatter' , x='A' , y='B' , mode='markers' , size = 20)


# In[20]:


df2.iplot(kind='bar' ,x='Category' , y='values' )


# In[26]:


df.sum().iplot(kind='bar')
#count() also


# In[27]:


df.iplot(kind='box')


# In[28]:


df3 = pd.DataFrame({'x':[1,2,3,4,5] ,'y':[10,20,30,40,50] , 'z':[100,200,300,400,500]})


# In[52]:


df3


# In[51]:


df3.iplot(kind='surface'  , colorscale='rdylbu')


# In[40]:


df.iplot(kind='hist' , bins=40)


# In[42]:


df[['A','B']].iplot(kind='spread')


# In[48]:


df.iplot(kind='bubble' , x='A' , y='B' , size='C')


# In[49]:


df.scatter_matrix()


# In[ ]:




