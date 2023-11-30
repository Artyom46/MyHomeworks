from cities import cities_list

cities_set = set()

computer_city = None

for city in cities_list:
    if city['name'][-1].lower() not in 'ьъы':
        cities_set.add(city['name'])

while cities_set:
    humans_city = input('Введите город: ').strip()

    if humans_city == 'стоп':
        print('Вы проиграли')
        break

    if humans_city not in cities_set:
        print('Такого города нет')
        break

    if computer_city:
        if computer_city[-1].lower() != humans_city[0].lower():
            print('Вы проиграли')
            break

    cities_set.remove(humans_city)

    print(f'Вы ввели: {humans_city}')

    for city in cities_set:
        if city[0].lower() == humans_city[-1].lower():
            computer_city = city

    cities_set.remove(computer_city)

    print(f'Машина ввела: {computer_city}')

else:
    print('Вы выиграли!')
