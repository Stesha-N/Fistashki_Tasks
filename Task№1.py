#!/usr/bin/env python
# coding: utf-8

# ### Задание 1.

# In[134]:


import pandas as pd
df = pd.read_excel('C:/Users/User/Desktop/intro_dataset.xlsx')


# In[135]:


Total = df['Апельсины'].sum()
print ("Продано всего апельсинов:", Total)


# In[136]:


Result = '\n'.join(list(df[df['Мандарины'] == df['Мандарины'].max()]['Дата']))#в случае нескольких месяцев с одинаковыми максимальными значениями 
print ('Месяц, в котором было продано больше всего мандаринов:', Result)


# ### Задание 2.

# In[137]:


df = pd.read_csv(r'C:\Users\User\Desktop\intro_dataset_2.txt', header=None)
new_df = df.T


# In[141]:


print ('Уникальные позиции:','\n'.join(list(new_df[0].unique())), sep = '\n')


# In[140]:


print('Сколько раз пользователи покупали тот или иной товар:', new_df[0].value_counts(), sep = '\n')

