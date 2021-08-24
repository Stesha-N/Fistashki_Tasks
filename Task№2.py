#Задание3

list_of_dicts = [{'post': 'post 1', 'author': 'author 1', 'followers': 4000, 'likes': 20, 'comments':10}, 
                {'post': 'post 2', 'author': 'author 2', 'followers': 5000, 'likes': 50, 'comments':60},
                {'post': 'post 3', 'author': 'author 3', 'followers': 6000, 'likes': 70, 'comments':5}]
engagement_rates = []
for post in list_of_dicts:
    engagement_rates.append((post['likes'] + post['comments'])/post['followers'])
    
print (round(sum(engagement_rates)/len(engagement_rates), 2))

#для большей производительности:

accum_rates = 0
for post in list_of_dicts:
    accum_rates += (post['likes'] + post['comments'])/post['followers']
    
print(round(accum_rates/len(list_of_dicts), 2))


#Задание 4

list_of_dicts = [{'author': 'kommersant', 'link': 'link 1', 'OTS': 50000, 'type': 'media'}, 
                {'author': 'vedomosti', 'link': 'link 1', 'OTS': 100000, 'type': 'media'},
                {'author': 'kommersant', 'link': 'link 1', 'OTS': 20000, 'type': 'VK'},
                {'author': 'kommersant', 'link': 'link 1', 'OTS': 5000, 'type': 'FB'}]
coefs = {'media': 0.01, 'VK': 0.1, 'FB': 0.3}
accum_tc = 0
for post in list_of_dicts:
    accum_tc += post['OTS']*0.8*coefs[post['type']]
print ('TC для всех четырех публикаций:', int(accum_tc))


#Задание 5

with open('C:/Users/User/Desktop/vk_post.txt', encoding = 'UTF-8') as file:
    text = file.read()
print ('id автора:', text.split('data-from-id=')[1].split('data-post-id')[0].replace('"', ''))
print ('текст поста:', text.split('"wall_post_text">')[1].split(':<br><br>')[0])
print ('ссылка на пост:', 'vk.com' + text.split('class="post_link"  href=')[1]                                        
                                         .split('onclick="return showWiki')[0].replace('"', ''))
print ('количество лайков:', text.split('data-section-ref="like-button-count">')[1].split('</div>')[0])
