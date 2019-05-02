#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


tips = sns.load_dataset('tips')


# tips.head()

# In[5]:


# FIRST TYPE DIST PLOT : IT PLOTS INLY ONE COLUMN GRAPH
#if remove the line kde=False is command , bins = number of pller
sns.distplot(tips['total_bill'] , bins = 30) , #kde=False)
sns.distplot(tips['tip'])


# In[6]:


tips.head()


# In[7]:


#SECOND TYPE JOINT PLOT : PLOTS BETWEEN TWO DATA COLUMNS 
sns.jointplot(x='total_bill',y='tip',data=tips)


# In[8]:


import seaborn as sns


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


tips = sns.load_dataset('tips')


# In[11]:


tips.head()
import numpy as np


# In[12]:


#third plot : bar ploting 
sns.barplot(x = 'sex' , y = 'total_bill' , data=tips , estimator=np.std)


# In[13]:


sns.countplot(x = 'sex' , data=tips)


# In[14]:


#forth plot: box ploting  , we can specify a special column and compare it with all 
sns.boxplot(x='day',y='total_bill' , data=tips , hue='smoker')


# In[15]:


#FIFTH PLOT
sns.violinplot(x='day' , y='total_bill' , data=tips , hue='sex' , split=True)


# In[16]:


#sixth plot
sns.stripplot(x='day' , y='total_bill' , data=tips , jitter=True , hue='sex' , split=True)


# In[31]:


sns.violinplot(x='day' , y='total_bill' , data=tips)
sns.swarmplot(x='day' , y='total_bill' , data=tips , color='black')


# In[33]:


sns.factorplot(x='day' , y='total_bill' , data=tips , kind='bar')


# In[34]:


#matrix plots


# In[35]:


import seaborn as sns


# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


tips = sns.load_dataset('tips')


# In[20]:


flights = sns.load_dataset('flights')


# In[21]:


tips.head()


# In[22]:


flights.head()


# In[25]:


tc = tips.corr()


# In[26]:


#first in matrix ploting
sns.heatmap(tc , annot=True , cmap='coolwarm')


# In[27]:


flights


# In[28]:


fp = flights.pivot_table(index='month' , columns='year' , values = 'passengers')


# In[29]:


sns.heatmap(fp , cmap='coolwarm' , linecolor='black' , linewidth=5)


# In[31]:


#SECOND MAP IN MATRIX PLOTING
sns.clustermap(fp , cmap='coolwarm' , standard_scale=1)


# In[60]:


import seaborn as sns


# In[32]:


get_ipython().run_line_magic('matplotlib', 'inline')
iris = sns.load_dataset('iris')
iris.head()


# In[33]:


sns.pairplot(iris)


# In[34]:


g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# In[35]:


tips=sns.load_dataset('tips')


# In[36]:


tips.head()


# In[37]:


g = sns.FacetGrid(data=tips , col='time' , row='smoker')
g.map(sns.distplot , 'total_bill')


# In[38]:


g.map(plt.scatter,'total_bill' , 'tip')


# In[39]:


sns.lmplot(x='total_bill' , y='tip' , data=tips , hue='sex' , markers = ['o','v'] , scatter_kws={'s':100})


# In[40]:


sns.lmplot(x='total_bill' , y='tip' , data=tips , col='day' , row='time' , hue='sex' , aspect=0.6 , size = 8)


# In[41]:


#style and coloring 


# In[42]:


sns.set_style('ticks')
sns.countplot(x = 'sex' , data=tips)
sns.despine(top=False , bottom=False)


# In[ ]:




