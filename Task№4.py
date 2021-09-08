#!/usr/bin/env python
# coding: utf-8

# ### Задание 1

# In[226]:


import pandas as pd
import os


# In[227]:


hm_vk = pd.read_csv(r'C:\Users\User\Desktop\Задания\kennebecproject_report_vk_posts_hmrussia_2021-06-01_2021-09-07_wc41qc.csv', sep=';')
hm_ig = pd.read_csv(r'C:\Users\User\Desktop\Задания\kennebecproject_report_ig_posts_hm_2021-06-01_2021-09-07_ayz23v.csv', sep=';')
zara_vk = pd.read_csv(r'C:\Users\User\Desktop\Задания\kennebecproject_report_vk_posts_zara_2021-06-01_2021-09-07_a4htko.csv', sep=';')
zara_ig = pd.read_csv(r'C:\Users\User\Desktop\Задания\kennebecproject_report_ig_posts_zara_2021-06-01_2021-09-07_a0o202.csv', sep=';')


# In[228]:


hm_common = pd.concat([hm_vk, hm_ig]).fillna(0)
zara_common = pd.concat([zara_vk, zara_ig]).fillna(0)


# In[229]:


social_actions_hm = hm_common[['likes_count','comments_count', 'reposts_count']].values.sum()
social_actions_zara = zara_common[['likes_count','comments_count', 'reposts_count']].values.sum()
accum_views_hm = hm_common['views_count'].sum()
accum_views_zara = zara_common['views_count'].sum()
followers = {'hm_v': 706429, 'hm_i': 37300000,  'zara_v': 376260 , 'zara_i': 45700000 }
ER_hm = round((hm_common['likes_count'].sum()/len(hm_common) + hm_common['comments_count'].sum()/len(hm_common))/((followers['hm_v']+followers['hm_i'])/2), 3)
ER_zara = round((zara_common['likes_count'].sum()/len(zara_common) + zara_common['comments_count'].sum()/len(zara_common))/((followers['zara_v']+followers['zara_i'])/2), 3)


# In[230]:


indicators = pd.DataFrame([['followers', followers['hm_v'] + followers['hm_i'], followers['zara_v'] + followers['zara_i']],['social_actions', social_actions_hm, social_actions_zara], ['accum_views', accum_views_hm, accum_views_zara], ['ER', ER_hm, ER_zara]], columns=['indicators', 'H&M', 'Zara'])


# In[233]:


indicators.to_excel('Brand_indicators.xlsx', sheet_name='Sheet_name_1')


# ### Задание 2

# In[236]:


from pptx import Presentation
import pandas as pd

hm_vk = pd.read_excel(r'C:\Users\User\Desktop\kennebecproject_report_vk_posts_hmrussia_2021-06-01_2021-09-07_wc41qc.csv')

prs = Presentation()
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Hello, World!"
subtitle.text = "python-pptx was here!"

prs.save('test.pptx')


# In[ ]:




