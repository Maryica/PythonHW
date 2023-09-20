# Работать с файлом california_housing_train.csv,
# который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import pandas as pd
data = pd.read_csv('california_housing_train.csv')

print(data.columns)
print(data[(data['population'] <= 500)][['population', 'median_house_value']])
print(f"Средняя стоимость дома: {data[data['population'] <= 500]['median_house_value'].mean()} ")

#если с округлением стоимости:
#print(f"Средняя стоимость дома: {round(data[data['population'] <= 500]['median_house_value'].mean())}")
