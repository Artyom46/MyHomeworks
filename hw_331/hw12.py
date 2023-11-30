from typing import (List, Dict, Tuple, Set, Union, Optional, Any)
import json
from cities import cities_list

cities_set = set()

for city in cities_list:
    cities_set.add(city['name'])

russian_letters_set = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')


def get_cities_set_from_json(file_name: str = 'cities.json') -> set:
    """
    Читает json файл и возвращает сет городов
    :param file_name: По умолчанию 'cities.json'
    :return: Сет городов
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        cities_set = set(json.load(file))

    return cities_set


def get_bad_startswith_letters(letters_set: set, cities_set: set) -> set:
    """
    Функция, которая возвращает сет плохих первых букв
    :param letters_set: Сет букв для поиска
    :param cities_set: Сет городов для анализа
    :return: Сет плохих букв, с которых не начинаются города в cities_set
    """
    bad_startswith_letters: set = set()

    for letter in letters_set:
        if not any(city.startswith(letter.upper()) for city in cities_set):
            bad_startswith_letters.add(letter)

    return bad_startswith_letters


def check_bad_startwith_letter(city: str, bad_letters: set) -> bool:
    """
    Функция принимает город и возвращает True, если он начинается на плохую букву
    :param city: Название города
    :param bad_letters: Сет плохих букв
    :return: bool
    """
    if city[0].lower() in bad_letters:
        return True
    else:
        return False


def check_main_game_rule(last_round_city: str, current_round_city: str) -> bool:
    """
    Функция принимает два города и проверяет, что первая буква города current_round_city
    равна последней букве города last_round_city
    :param last_round_city: Город из прошлого раунда
    :param current_round_city: Город из текущего раунда
    :return: bool
    """
    if last_round_city[-1].lower() == current_round_city[0].lower():
        return True
    else:
        return False


def computer_move(cities_set: set, last_round_city: str) -> str | None:
    """
    Функция принимает сет городов, город из прошлого раунда. Проходит циклом по сету
    городов, проверяя каждый город на главное правило игры
    :param cities_set:
    :param last_round_city:
    :return:
    """
    for city in cities_set:
        if check_main_game_rule(last_round_city, city):
            return city

    else:
        return None


def main():
    # Читаем json файл с городами и получаем сет городов
    cities_set = get_cities_set_from_json()

    # Объявляем переменную под город машины (None на старте)
    computer_city = None

    while cities_set:
        # Пользовательский ввод
        humans_city = input('Введите город: ').strip()

        # Проверка на стоп
        if humans_city == 'стоп':
            print('Вы проиграли')
            # Логирование
            break

        # Проверка на вхождение в сет
        if humans_city not in cities_set:
            print('Такого города нет')
            break

        # Если компьютер уже ходил. Делаем проверку на последнюю букву
        if computer_city:
            if not check_main_game_rule(computer_city, humans_city):
                print('Вы проиграли')
                break

        # Удаление из сета
        cities_set.remove(humans_city)

        # Принт ход человека
        print(f'Вы ввели: {humans_city}')

        # Ход машины
        computer_city = computer_move(cities_set, humans_city)

        if not computer_city:
            print('Вы выиграли')
            break

        # Удаление из сета
        cities_set.remove(computer_city)
        # Принт ход машины
        print(f'Машина ввела: {computer_city}')

    else:
        print('Вы терминатор. Вы выиграли!')


main()


# Игра в города на функциях. Аннотация типов. Typing
