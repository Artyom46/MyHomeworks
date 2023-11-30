phone_number = input("Введите номера телефона через ; без пробелов: ").strip()

phone_number_list = []

phone_number = (phone_number
                .replace("+", "")
                .replace(" ", "")
                .replace("-", "")
                .replace("(", "")
                .replace(")", ""))

phone_number_list += phone_number.split(';')

for numbers in phone_number_list:
    if not (numbers.startswith("8") or numbers.startswith("7")):
        raise ValueError(f'номер {numbers} должен начинаться с +7 или 8')
    if not (len(numbers) == 11 and numbers.isnumeric()):
        raise ValueError(f'номер {numbers} должен состоять из 11 знаков')

print(phone_number_list)
print('Ввод корректный')

#  +7(777)-777-77-77;+7(888) 888 88 88;+(799)99999999;+72222222222;84444444444
