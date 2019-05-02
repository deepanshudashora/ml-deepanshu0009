#!/usr/bin/env python
# coding: utf-8

# #create pandas series  

# In[1]:


import pandas as pd


# In[2]:


a = pd.Series([1,2,3,4,5])


# In[3]:


a


# In[4]:


type(a)


# In[5]:


a[2]


# In[6]:


a = pd.Series(['a','b','c','c'])


# In[7]:


a


# In[8]:


a[3]


# In[9]:


type(a)


# In[10]:


a = pd.date_range(start = '01-01-2018',end = '23-03-2019')


# In[11]:


a


# In[12]:


type(a
    )


# In[13]:


import numpy as np


# In[14]:


temp = np.random.randint(low=20 , high=100, size=[20,])
name = np.random.choice(['abhay','teclov','geekshub','ankit'],20)
random = np.random.choice([10,11,13,14],20)


# In[15]:


a = list(zip(temp,name,random))


# In[16]:


df = pd.DataFrame(data = a ,columns = ['temp','name','random'])


# In[17]:


df


# In[18]:


z =  np.random.randint(low = 20,high = 100,size = [20,20])


# In[19]:


z


# In[20]:


name = np.random.choice(['a','d','s','n','p'],[20,23])


# In[21]:


name


# In[22]:


df= pd.DataFrame({'temp':temp,'name':name,'random':random})


# In[ ]:


type(df)


# In[ ]:


df


# In[23]:


happy = np.random.choice([1,2,3,45],6)


# In[24]:


lucky = np.random.randint(low=10,high=1000,size=[20,])


# In[25]:


fd = pd.DataFrame({'temp':happy,'jocker':lucky})


# In[26]:


happy


# In[27]:


lucky


# In[28]:


c = list(zip(happy,lucky))


# In[29]:


kl = pd.DataFrame(data = c , columns = ['happy','lucky'])


# In[30]:


kl


# In[31]:


kl


# In[32]:


#first five values of dataframe
kl.head()


# In[33]:


#last five values of data frame
kl.tail()


# In[34]:


kl.columns


# In[35]:


kl.happy


# In[36]:


kl.lucky


# In[37]:


df.name


# In[38]:


df['name']


# In[39]:


#all the statitics
df['temp'].describe()


# In[40]:


df.info()


# In[41]:





df.values


# In[42]:


kl.set_index('happy' , inplace = True)


# In[43]:


kl


# In[44]:


kl.sort_index(axis = 0 , ascending=False)


# In[47]:


kl.sort_values('lucky',ascending = False )


# In[48]:


kl.drop(['lucky'] , axis =1
       )


# In[49]:


kl.head()


# In[50]:


#the key of dict become the data pf our data frame
data = {'col_1':[3,2,1,0] , 'col_2':['a','b','c','d']}


# In[51]:


data


# In[53]:


a = list(zip(data))


# In[54]:


j = pd.DataFrame(data = a , columns=['col_1','col_2'])


# In[55]:


df.iloc[[0,1]]


# In[56]:


df.iloc[1:3,1]


# In[57]:


df.iloc[[True,True,False,True]]


# In[58]:


df.iloc[0:3]


# In[59]:


df


# In[60]:


df.loc[[4,12]]


# In[61]:


df.loc[3,:]


# In[62]:


df.loc[[True,True,False,True]]


# In[63]:


df.loc[df.random>13]


# In[64]:


df.loc[(df.random>13)or(df.random == 10),:]


# In[65]:


#how to read the data from files like csv and xl


# In[66]:


df1 = pd.read_csv("weather_data.csv")


# In[67]:


df1 = pd.read_csv("GOOG.csv")


# In[68]:


df1 = pd.read_csv("happy.csv")


# In[69]:


df1


# In[70]:


df1.to_excel("df_data.xlsx")


# In[71]:


df2 = pd.read_excel("df_data.xlsx")


# In[111]:


df2


# In[112]:


df2.to_csv("file.csv")


# In[113]:


pd.read_csv("file.csv")


# In[52]:


import numpy as np
import pandas as pd


# In[54]:


reg = np.random.randint(low=20, high =100, size=[20,])
chappati = np.random.randint(low=3,high=6,size=[20,])


# In[55]:


reg


# In[56]:


fruit=np.random.choice(['apple','tomato','orange','potato','carrot'],20)


# In[57]:


fruit


# In[61]:


df1 = list(zip(reg,fruit,chappati))


# In[62]:


pd.DataFrame(data=df1 , columns=['reg','fruit','chappati'])


# In[64]:


reg = np.random.randint(low=10,high=100,size=[20,])


# In[68]:


vegiss = np.random.choice(['ladyfinger','potato','tomato','gingeger'],20)


# In[69]:


chapatti = np.random.randint(low = 3,high=6,size=[20,])


# In[71]:


df2 = list(zip(reg,vegiss,chapatti))


# In[72]:


pd.DataFrame(data=df2,columns=['reg','vegiss','chapatti'])


# In[84]:


animal = np.random.choice(['lion','tiger'],2)


# In[85]:


number = np.random.randint(low = 0,high=5,size=[2,])


# In[86]:


a = list(zip(animal,number))


# In[87]:


df1 = pd.DataFrame(data=a,columns=['animal','number'])


# In[88]:


df1


# In[89]:


name = np.random.choice(['aniket','ankit'],2)


# In[90]:


number = np.random.randint(low=0,high=5,size=[2,])


# In[91]:


b= list(zip(name,number))


# In[92]:


df2 = pd.DataFrame(data=b,columns=['name','number'])


# In[93]:


df2


# In[96]:


#index ignoence is optoonal
#by row axis =0
pd.concat([df1,df2],axis=0,ignore_index=True,sort=False)


# In[98]:


#by columns ,axis =1
pd.concat([df1,df2],axis = 1 , ignore_index=True,sort= False)


# In[103]:


group = df1.groupby("event")


# In[105]:


temp = np.random.randint(low = 20,high = 100 , size = [30,])


# In[106]:


sickp = np.random.randint(low = 10,high = 300 , size = [30,])


# In[107]:


g = list(zip(temp,sickp))


# In[108]:


df = pd.DataFrame(data=g , columns = ['temp','sickp'])


# In[109]:


df


# In[110]:


df.to_csv('deep.csv' , index=False)


# In[111]:


pd.read_csv("deep.csv")


# In[112]:


df_group = df.groupby("temp")


# In[113]:


df_group


# In[114]:


for temp in df_group:
    print(temp)


# In[116]:


tmep = np.random.randint(low=5,high=45,size=[4,])


# In[119]:


date = np.random.choice(['23/04/2019','25/04/2019','27/04/2019','29/04/2019'],4)


# In[126]:


event = np.random.choice(['sunny','cool','heat','rain'],4)


# In[127]:


a = list(zip(tmep,date,event))


# In[128]:


df = pd.DataFrame(data=a , columns = ['temp','date','event'])


# In[129]:


df


# In[130]:


df.to_csv("deepa.csv")


# In[131]:


df_group = df.groupby("event")


# In[132]:


df_group


# In[136]:


for temp in df_group:
    print(tmep)


# In[139]:


df_group.get_group("date")


# In[141]:


df.describe


# In[148]:


def hot_temp(x):
    if x > 30:
        return True
    else:
        return False


# In[149]:


df['hot_temp'] = df['temp']


# In[150]:


df


# In[152]:


df["hot_tempr"] = df["temp"].apply(lambda x : x>30)


# In[ ]:





# In[153]:


df


# In[154]:


d1 = pd.DataFrame({"city":["lucknow","kanpur","agra","delhi"],"temprature":[32,45,30,40]})


# In[155]:


d1


# In[160]:


d2 = pd.DataFrame({"city":["delhi","kanpur","agra","lucknow"],"humidity":[68,89,75,43]})


# In[161]:


df =  pd.merge(d1,d2,on='city')


# In[162]:


df


# In[163]:


#pivot table


# In[167]:


df2.pivot_table(values='humidity' , index = 'city',aggfunc='mean')


# In[2]:


import pandas as pd
import numpy as np
tmep = np.random.randint(low=5,high=45,size=[4,])
date = np.random.choice(['23/04/2019','25/04/2019','27/04/2019','29/04/2019'],4)
event = np.random.choice(['sunny','cool','heat','rain'],4)
a = list(zip(tmep,date,event))
df = pd.DataFrame(data=a , columns = ['temp','date','event'])
df


# In[5]:


df.pivot_table(values = 'temp',index = 'event' , aggfunc = 'mean')


# In[6]:


df.pivot_table(columns = 'temp')


# In[7]:


help(pd.DataFrame.pivot_table) 


# In[10]:


import numpy as np
import pandas as pd


# In[11]:


from numpy.random import randn


# In[13]:


np.random.seed(101)


# In[14]:


df = pd.DataFrame(randn(5,4) , ['A','B','C','D','E'] , ['W','X','Y','Z'])


# In[15]:


df


# In[16]:


df['W']


# In[20]:


df['new'] = df['W'] + df['Y']


# In[21]:


df['new']


# In[25]:


df.drop('new' , axis=1 , inplace = True)


# In[26]:


df


# In[28]:


df.loc['A']


# In[29]:


df.iloc[2]


# In[ ]:




