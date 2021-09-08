import pandas as pd

hm_vk = pd.read_csv(r'C:\Users\User\Desktop\Задания\kennebecproject_report_vk_posts_hmrussia_2021-06-01_2021-09-07_wc41qc.csv', sep=';')
hm_ig = pd.read_csv(r'C:\Users\User\Desktop\Задания\kennebecproject_report_ig_posts_hm_2021-06-01_2021-09-07_ayz23v.csv', sep=';')
zara_vk = pd.read_csv(r'C:\Users\User\Desktop\Задания\kennebecproject_report_vk_posts_zara_2021-06-01_2021-09-07_a4htko.csv', sep=';')
zara_ig = pd.read_csv(r'C:\Users\User\Desktop\Задания\kennebecproject_report_ig_posts_zara_2021-06-01_2021-09-07_a0o202.csv', sep=';')

hm_common = pd.concat([hm_vk, hm_ig]).fillna(0)
zara_common = pd.concat([zara_vk, zara_ig]).fillna(0)

social_actions_hm = hm_common[['likes_count','comments_count', 'reposts_count']].values.sum()
social_actions_zara = zara_common[['likes_count','comments_count', 'reposts_count']].values.sum()
accum_views_hm = hm_common['views_count'].sum()
accum_views_zara = zara_common['views_count'].sum()
followers = {'hm_v': 706429, 'hm_i': 37300000,  'zara_v': 376260 , 'zara_i': 45700000 }
ER_hm = round((hm_common['likes_count'].sum()/len(hm_common) + hm_common['comments_count'].sum()/len(hm_common))/((followers['hm_v']+followers['hm_i'])/2), 3)
ER_zara = round((zara_common['likes_count'].sum()/len(zara_common) + zara_common['comments_count'].sum()/len(zara_common))/((followers['zara_v']+followers['zara_i'])/2), 3)

indicators = pd.DataFrame([['followers', followers['hm_v'] + followers['hm_i'], followers['zara_v'] + followers['zara_i']],['social_actions', social_actions_hm, social_actions_zara], ['accum_views', accum_views_hm, accum_views_zara], ['ER', ER_hm, ER_zara]], columns=['indicators', 'H&M', 'Zara'])
indicators.to_excel('Brand_indicators.xlsx', sheet_name='Sheet_name_1')
