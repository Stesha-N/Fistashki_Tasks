#Задание1

import pandas as pd
data = pd.read_excel('dataset_lesson2.xlsx')
#1.1
data_list = list(data.T.to_dict().values())
#1.2
idx = 0
subscribes_sum = 0
ER_sum = 0
users = []
while subscribes_sum <= 1000000:
    users.append(data_list[idx])
    subscribes_sum += data_list[idx]['Followers']
    ER_sum += data_list[idx]['ER']
    idx += 1
print('Cписок людей до тех пор, пока у нас их суммарное количество подписчиков не составит 1000000 человек:\n', users, subscribes_sum)
#1.3
print('Cреднее количество подписчиков:', round(subscribes_sum/len(users), 2))
print('Cреднее ER:', round(ER_sum/len(users), 2))


#Задание2

idx = 0
subscribes_sum = 0
ER_sum = 0
users = []
while subscribes_sum <= 1000000:
    if data_list[idx]['ER'] >= 0.05:
        users.append(data_list[idx])
        subscribes_sum += data_list[idx]['Followers']
        ER_sum += data_list[idx]['ER']
    idx += 1
print('Cписок людей до тех пор, пока у нас их суммарное количество подписчиков не составит 1000000 человек и ER которых был не меньше 5%:\n', users, subscribes_sum)
print('Cреднее количество подписчиков:', round(subscribes_sum/len(users), 2))
print('Cреднее ER:', round(ER_sum/len(users), 2))

#Задание 3

with open('followers.txt') as file:
    text = file.read()
#3.1
data = text.split('<a href="https://www.instagram.com/')
nicknames_list = []
for nickname in data[1:]:
    nicknames_list.append(nickname.split('">')[0])
print(nicknames_list)
#3.2
nicknames_dict = {x: 'https://www.instagram.com/'+ x for x in nicknames_list}
print(nicknames_dict)
#3.4
print(nicknames_list[::100])

#Задание 4

def compute_metrics(*args):
    accum_followers = 0
    accum_ER = 0
    for x in args:
        accum_followers += x['Followers']
        accum_ER += x['ER']
    return accum_followers, round(accum_ER/len(args), 2)
print("общее количество подписчиков {} и средний ER {}".format(*compute_metrics(*data_list)))

#Задание 5

import pyexcel
campaigns = pyexcel.get_records(file_name="dataset_lesson2_2.xlsx", name_columns_by_row=0)
accum_impressions = 0
accum_spend = 0
for campaign in campaigns:
    if campaign['Spend']:
        accum_impressions += float(str(campaign['Impressions']).replace('k', '000'))
        accum_spend += float(campaign['Spend'])
print('Общее количество показов', round(accum_impressions, 2))
print('CPM по всей активности', round(accum_spend*1000/accum_impressions, 2))
