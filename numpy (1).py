#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3])


# In[3]:


a


# In[4]:


b = np.array([[1,2,3],[4,4,6]])


# In[5]:


b


# In[6]:


b.shape


# In[19]:


a.shape


# In[20]:


b.dtype


# In[21]:


b.ndim


# In[22]:


print(type(a))


# In[23]:


print(type(b))


# In[24]:


np.arange(11)


# In[25]:


c = range(10000)


# In[26]:


get_ipython().run_line_magic('timeit', '[i**3 for i in c]')


# In[27]:


c_numpy = np.arange(10000)


# In[28]:


get_ipython().run_line_magic('timeit', 'c_numpy**3')


# In[29]:


l1 = range(10000)
l2 = [i**2 for i in range(10000)]


# In[30]:


get_ipython().run_line_magic('timeit', 'list(map(lambda x,y: x*y , l1,l2))')


# In[31]:


a1 = np.array(l1)
b1 = np.array(l2)


# In[32]:


get_ipython().run_line_magic('timeit', 'a1*b1')


# In[33]:


#giving the space of two
np.arange(2,12,2)


# In[34]:


np.zeros((3,2))


# In[35]:


np.ones((3,2))


# In[36]:


np.eye(3)


# In[37]:


np.full((3,3),2)


# In[43]:


np.full((3,3),2.2 , dtype=np.int)


# In[44]:



np.diag([1,2,3,4,5])


# In[45]:


v = np.array([1,2,3])


# In[46]:


v


# In[47]:


np.tile(v,(3,1))


# In[48]:


n = np.random.random()


# In[49]:


n


# In[50]:


n*45


# In[51]:


np.random.random([3,3])


# In[52]:


a = np.linspace(1,50,100)


# In[53]:


a


# In[54]:


a.itemsize


# In[55]:


#because 2*3*3 = 18
np.arange(18).reshape(2,3,3)


# In[56]:


a = np.array([2,4,6,8,10,12,14,16])


# In[57]:


a


# In[58]:


a[0]


# In[59]:


a[[2,5,7]]


# In[60]:


a[2:]


# In[61]:


a[0::2]


# In[62]:


a = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[63]:


a


# In[64]:


a[0,2]


# In[65]:


a>2


# In[66]:


a[(a<6)&(a>2)]


# In[67]:


a = np.arange(10)


# In[68]:


a


# In[69]:


b =a


# In[70]:


b


# In[71]:


b[0] =11


# In[72]:


b


# In[73]:


a


# In[74]:


np.shares_memory(a,b)


# In[75]:


a = np.arange(10)


# In[76]:


b = a.copy()


# In[77]:


b


# In[78]:


b[0] = 34


# In[79]:


b


# In[80]:


a


# In[81]:


np.shares_memory(a,b)


# In[82]:


a = np.array([[1,2,3],[4,5,6]])


# In[83]:


a


# In[84]:


a.T


# In[85]:


a.T.shape


# In[86]:


b = np.array([[7,8,9],[10,12,13]])


# In[87]:


b


# In[88]:


a == b


# In[89]:


np.vstack((a,b))


# In[90]:


a = np.arange(1,10)


# In[91]:


a


# In[92]:


np.sin(a)


# In[93]:


np.tan(a)


# In[94]:


np.exp(a)


# In[95]:


np.sum(a)


# In[96]:


np.median(a)


# In[97]:


a.std()


# In[98]:


np.square(a)


# In[99]:


a = np.arange(1,10).reshape(3,3)


# In[100]:


a


# In[101]:


np.linalg.det(a)


# In[102]:


np.linalg.inv(a)


# In[103]:


np.linalg.eig(a)


# In[104]:


#for dot product
np.dot(a,b)


# In[105]:


a = np.array([1,1,0],dtype = bool)
b = np.array([1,0,1],dtype = bool)


# In[106]:


a,b


# In[107]:


np.logical_or(a,b)


# In[108]:


np.all(a == a)


# In[109]:


a = np.array([[1,2],[3,4]])


# In[110]:


a


# In[111]:


a.sum()


# In[112]:


a.sum(axis = 0)


# In[113]:


a.sum(axis = 1)


# In[114]:


a.max()


# In[115]:


a.argmax()


# In[116]:








a.shape


# In[117]:


a = np.arange(10)


# In[118]:


a


# In[119]:


a.shape


# In[120]:


a[:,np.newaxis].shape


# In[121]:


np.sort(a)


# In[ ]:





# In[ ]:




