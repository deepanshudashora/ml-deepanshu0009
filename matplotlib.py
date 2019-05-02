#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import numpy as np


# In[4]:


x = np.linspace(0,5,11)
y = x **2
z = y**2


# In[5]:


x


# In[6]:


y


# In[7]:


#functional mathod
plt.plot(x,y)
plt.xlabel('yoyo')
plt.ylabel('honey singh')
plt.title('Title')


# In[8]:


plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')


# In[9]:


##oo
fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8]) 

axes.plot(x,y)
axes.set_xlabel('x label')
axes.set_ylabel('y label')
axes.set_title('title')


# In[12]:


fig = plt.figure()

axes1  = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes3= fig.add_axes([0.3,0.5,0.5,0.8])
axes1.plot(x,y)
axes2.plot(y,x)
axes3.plot(x,y)


# In[13]:


fig,axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y)
axes[1].plot(y,x)
axes[0].set_title('jfdhg')
plt.tight_latout


# In[14]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2 , label = 'x Squred')
ax.plot(y,x**3 , label = 'y cubed')
ax.plot(y,x**2  , label = 'z circle')
ax.set_title('gjjgj')
ax.set_xlabel('fdgfdh')
ax.legend(loc = 0)


# In[15]:


fig.savefig('my.pic.png' , dpi=200)


# In[16]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color = 'black' , linewidth=1 , alpha = 1 , marker = 'o' , markersize = 20 , markerfacecolor = 'yellow' , markeredgewidth=3,markeredgecolor='green') #use color code #FF8c00 or RGB Hex code on google
#use lw instead of linewidth
#ax.plot(x,y,color='purple' , lw  = 3 , linestyle = '--' , marker = '+')
#linestyle = ls
  


# In[17]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color = 'purple' , lw=2 , ls=
        '--')
ax.set_xlim([0,1])
ax.set_ylim([0,2])


# In[ ]:


plt.scatter(x,y)


# In[ ]:




