data_lst = ['1', '2', '3', '4d', 5]

void_list = []

for item in data_lst:
    try:
        item = int(item)
        void_list.append(item)
    except ValueError:
        print(f'Не валидные данные: {item}')
print(void_list)


# Проверка на значения
