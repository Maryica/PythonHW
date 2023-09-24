# В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())
print()

print(pd.DataFrame({'human': data['whoAmI'] == 'human', 'robot': data['whoAmI'] == 'robot'}).astype(int).head())


