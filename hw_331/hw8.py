from marvel import full_dict
from pprint import pprint

stage_dict = {
    1: "Первая фаза",
    2: "Вторая фаза",
    3: "Третья фаза",
    4: "Четвертая фаза",
    5: "Пятая фаза",
    6: "Шестая фаза",
}

input_user_stage = input('Введите номер фазы: ')

if not input_user_stage.isdigit():
    raise TypeError('Введите фазу цифрой')

user_stage = int(input_user_stage)

if user_stage not in stage_dict.keys():
    raise ValueError('Такой фазы не существует')

stage_string = stage_dict[user_stage]

for film, film_dict in full_dict.items():
    if film_dict['stage'] == stage_string:
        result = film_dict['title']
        pprint(result)
