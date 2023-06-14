import pandas as pd

data = ['Название судна', 'АДМИРАЛ НЕВЕЛЬСКОЙ', 'Регистровый номер', '180720']
columns = [data[i] for i in range(len(data)) if i % 2 == 0]
# Создаем пустой DataFrame
df = pd.DataFrame(columns=columns)

# Добавляем значения в DataFrame
for i in range(1, len(data), 2):
    df.loc[0, columns[i // 2]] = data[i]
df.to_excel('output.xlsx', index=False)