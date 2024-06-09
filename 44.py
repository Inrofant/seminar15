import pandas as pd
import random

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Original DataFrame:")
print(data.head())

# Преобразование в one-hot представление
data_one_hot = pd.DataFrame()
data_one_hot['human'] = (data['whoAmI'] == 'human').astype(int)
data_one_hot['robot'] = (data['whoAmI'] == 'robot').astype(int)

print("\nOne-hot Encoded DataFrame:")
print(data_one_hot.head())
