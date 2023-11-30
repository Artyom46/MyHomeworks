from pprint import pprint
from typing import List, Dict, Any, Callable

# 1. Сделайте импорт `full_dict` из документа `Marvel.py`
from marvel import full_dict

# 2. Напишите пользовательский ввод цифр через пробел, разбейте его на список,
# и примените к каждому элементу списка `int` используя `map`, но только в том случае,
# если этот элемент списка число, иначе замените его на `None`

user_input: List[str] = input('Введите числа через пробел: ').split(' ')
user_input_int: List[int | None] = list(map(lambda x: int(x) if x.isdigit() else None, user_input))
pprint(user_input_int)

# 3. Используйте `filter` и получите аналогичный по структуре словарь,
# который будет содержать исходные `id` и остальные ключи, но только
# тех фильмов, `id` которых есть в полученном списке в п.2

filtered_by_id: dict = dict(filter(lambda x: x[0] in user_input_int, full_dict.items()))
pprint(filtered_by_id)

# 4. Составьте `set comprehension` (генератор множества) собрав множество содержимого ключа
#  `director` словаря дата-сета

directors_set_comprehansion: set = {movie['director'] for movie in full_dict.values() if movie['director'] != 'TBA'}
pprint(directors_set_comprehansion)

# 5. Составьте `dict comprehension` (генератор словаря) сделав копию исходного словаря `full_dict`,
# при этом применим в к каждому `'year'` значению, функцию `str`

str_dict_comprehension: Dict[int, Dict[str, str]] = {key: {k: str(v) if k == 'year' else v
                                                           for k, v in value.items()} for key, value in
                                                     full_dict.items()}

pprint(str_dict_comprehension)

# 6. Используйте `filter` и получите аналогичный по структуре словарь, который будет содержать
#  исходные `id` и остальные ключи, но только тех фильмов, которые начинаются на букву `Ч`

filtered_by_ch: Dict[int, Dict[str, Any]] = dict(filter(lambda x: x[1]['title'].startswith('Ч'), full_dict.items()))
pprint(filtered_by_ch)

# 7. Сделайте сортировку словаря `full_dict` по одному (любому) параметру,
# с использованием `lambda` на выходе аналогичный по структуре словарь.
# Обязательно подпишите, по какому параметру вы делаете сортировку!

# Сортировка по одному параметру title
sorted_by_title: Dict[int, Dict[str, str | int]] = dict(sorted(full_dict.items(), key=lambda x: x[1]['title']))
pprint(sorted_by_title, sort_dicts=False)


# ДЗ 13
