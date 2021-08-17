#Задание1
import pandas as pd
df = pd.read_excel('intro_dataset.xlsx')
total = df['Апельсины'].sum()
print ("Продано всего апельсинов:", total)
result = '\n'.join(list(df[df['Мандарины'] == df['Мандарины'].max()]['Дата']))#в случае нескольких месяцев с одинаковыми максимальными значениями 
print ('Месяц, в котором было продано больше всего мандаринов:', result)
#Задание2
df = pd.read_csv('intro_dataset_2.txt', header=None)
new_df = df.T
print ('Уникальные позиции:','\n'.join(list(new_df[0].unique())), sep = '\n')
print('Сколько раз пользователи покупали тот или иной товар:', new_df[0].value_counts(), sep = '\n')

