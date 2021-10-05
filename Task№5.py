#1задание
import vk
import time
vk_api = vk.API(session,  v = '5.131')
session = vk.Session(access_token='')
offset = 0
member_counts = vk_api.groups.getMembers(group_id = "kult_patrul")['count']
members_list = []
while offset <= member_counts:
    basa = vk_api.groups.getMembers(group_id = "kult_patrul", offset = offset, fields = 'country, city')['items']
    for i in basa:
        members_dict = {'URL':'https://vk.com/id'+ str(i['id']), 
                    'ФИО':i['last_name'] + ' ' + i['first_name'],
                    'Страна':i['country']['title'] if 'country' in i else 'Страна не указана',
                    'Город':i['city']['title'] if 'city' in i else 'Город не указан'}
        members_list.append(members_dict)
    offset += 1000
    time.sleep(0.5)
print('Количество подписчиков:', len(members_list))
print(members_list)

#2задание
def get_posts_and_comments(name_group):
    offset = 0
    posts_list = []
    posts_counts = vk_api.wall.get(domain = name_group)['count']
    while offset <= posts_counts:
        baza = vk_api.wall.get(domain = name_group, offset = offset, extended=1, fields = 'text')['items']
        for y in baza:
            text_list = {'URL текста':'https://vk.com/'+ name_group + '?w=wall' + str(y['from_id'])+ '_' + str(y['id']), 
                        'Текст':y['text'] if 'text' in y else 'Текста нет'}
            time.sleep(0.5)
            datas = vk_api.wall.getComments(owner_id = y['owner_id'], post_id = y['id'], extended=1)
            comments_list = []
            for t in range(len(datas['items'])):
                comments_list.append(datas['items'][t]['text'])
            text_list['Текст комментов'] = comments_list 
            posts_list.append(text_list)
        offset += 100
        time.sleep(0.5)
    return posts_list




