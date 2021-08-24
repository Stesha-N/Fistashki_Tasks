#!/usr/bin/env python
# coding: utf-8

# #### Задание3

# In[1]:


list_of_dicts = [{'post': 'post 1', 'author': 'author 1', 'followers': 4000, 'likes': 20, 'comments':10}, 
                {'post': 'post 2', 'author': 'author 2', 'followers': 5000, 'likes': 50, 'comments':60},
                {'post': 'post 3', 'author': 'author 3', 'followers': 6000, 'likes': 70, 'comments':5}]


# In[31]:


engagement_rates = []
for post in list_of_dicts:
    engagement_rates.append((post['likes'] + post['comments'])/post['followers'])
    
print (round(sum(engagement_rates)/len(engagement_rates), 2))


# In[32]:


#для большей производительности:
accum_rates = 0
for post in list_of_dicts:
    accum_rates += (post['likes'] + post['comments'])/post['followers']
    
print(round(accum_rates/len(list_of_dicts), 2))


# #### Задание 4

# In[54]:


list_of_dicts = [{'author': 'kommersant', 'link': 'link 1', 'OTS': 50000, 'type': 'media'}, 
                {'author': 'vedomosti', 'link': 'link 1', 'OTS': 100000, 'type': 'media'},
                {'author': 'kommersant', 'link': 'link 1', 'OTS': 20000, 'type': 'VK'},
                {'author': 'kommersant', 'link': 'link 1', 'OTS': 5000, 'type': 'FB'}]


# In[55]:


coefs = {'media': 0.01, 'VK': 0.1, 'FB': 0.3}
accum_tc = 0
for post in list_of_dicts:
    accum_tc += post['OTS']*0.8*coefs[post['type']]
print ('TC для всех четырех публикаций:', int(accum_tc))


# #### Задание 5

# In[ ]:


#задание 5

#Я решил взять исходный код поста в паблике "Лентач", он хранится на Notion под названием vk_post.txt. 
#Что нужно сделать - выцепить сам текст как единых, а потом силами команды split добыть следующие вещи: 1) id автора 2) текст поста 3) ссылку на пост 4) количество лайков


# In[59]:


with open('C:/Users/User/Desktop/vk_post.txt', encoding = 'UTF-8') as file:
    text = file.read()


# In[74]:


text


# In[97]:


print ('id автора:', text.split('data-from-id=')[1].split('data-post-id')[0].replace('"', ''))


# In[85]:


print ('текст поста:', text.split('"wall_post_text">')[1].split(':<br><br>')[0])


# In[94]:


print ('ссылка на пост:', 'vk.com' + text.split('class="post_link"  href=')[1]                                         .split('onclick="return showWiki')[0].replace('"', ''))


# In[93]:


print ('количество лайков:', text.split('data-section-ref="like-button-count">')[1].split('</div>')[0])


# In[ ]:




