#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


df = pd.read_csv(r'C:\Users\MANISH\Desktop\Zomato_EDA\zomato.csv' , encoding = 'latin-1')
df.head()


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.isnull().sum()


# In[10]:


[features for features in df.columns if df[features].isnull().sum() > 0]


# In[46]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[16]:


df_country = pd.read_excel(r'C:\Users\MANISH\Desktop\Zomato_EDA\Country-Code.xlsx')
df_country.head()


# In[18]:


final_df = pd.merge(df , df_country , on = 'Country Code' , how ='left')


# In[19]:


final_df


# In[21]:


final_df.dtypes


# In[22]:


final_df.columns


# In[29]:


CountryNames = final_df.Country.value_counts().index


# In[27]:


CountryValues = final_df.Country.value_counts().values


# In[47]:


plt.pie(CountryValues[:3] , labels = CountryNames[:3], autopct='%1.2f%%')


# In[34]:


final_df.columns


# In[41]:


ratings = final_df.groupby(['Aggregate rating' , 'Rating color' , 'Rating text']).size().reset_index().rename(columns = {0:'Rating Count'})


# In[42]:


ratings.head()


# In[ ]:





# In[45]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(data = ratings , x='Aggregate rating' , y = 'Rating Count')


# In[49]:


sns.barplot(data = ratings , x='Aggregate rating' , y = 'Rating Count' , hue = 'Rating color' , palette=['White' , 'Red' , 'Orange' , 'Yellow' , 'green' , 'green'])


# In[50]:


sns.countplot(x='Rating color' , data = ratings ,  palette=['White' , 'Red' , 'Orange' , 'Yellow' , 'green' , 'green'])


# In[51]:


final_df.columns


# In[59]:


#Find count that  which country gives white or 0  rating 
final_df[final_df['Rating color'] == 'White'].groupby('Country').size().reset_index()


# In[63]:


#Find which currency is used by which country ?
final_df[['Country' , 'Currency']].groupby(['Country' , 'Currency']).size().reset_index()


# In[65]:


#Which country has online deliveries option?

final_df[final_df['Has Online delivery']=='Yes'].Country.value_counts().reset_index()


# In[66]:


#Create a pie chart for city distribution
CityNames = final_df.City.value_counts().index
CityValues = final_df.City.value_counts().values


# In[70]:


plt.pie(CityValues[:4], labels = CityNames[:4], autopct='%1.2f%%')


# #Find Top 10 Cuisines 

# In[72]:


final_df.columns


# In[ ]:


final_df['Cuisines'].


# In[76]:


Count_of_Cuisine = final_df.Cuisines.value_counts().reset_index()


# In[77]:


Count_of_Cuisine[:10]


# In[ ]:




