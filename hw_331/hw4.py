phone_number = input("Введите номер телефона: ").strip()

# if phone_number.startswith("8") or phone_number.startswith("+7") or phone_number.startswith("+"):
#     if len(phone_number) == 11 and phone_number.isnumeric():
#         phone_number = (phone_number.replace("+", "") and
#                         phone_number.replace(" ", "") and
#                         phone_number.replace("-", "") and
#                         phone_number.replace("(", "") and
#                         phone_number.replace(")", ""))
#         print("Правильный формат")
#     else:
#         print("Неверный формат")
# else:
#     print("Неверный формат")

phone_number = (phone_number
                .replace("+", "")
                .replace(" ", "")
                .replace("-", "")
                .replace("(", "")
                .replace(")", ""))

if phone_number.startswith("8") or phone_number.startswith("7") or phone_number.startswith("+"):
    if len(phone_number) == 11 and phone_number.isnumeric():
        print("Правильный формат! len == 11")
    else:
        print("Неверный формат! len != 11")
    print("Правильный формат +7, 8")
else:
    print("Неверный формат! not +7, 8")

print(phone_number)

# =======================================================================

# password = input('Введите пароль: ')
#
# if (((len(password) >= 7 and (any([i.isdigit() for i in password])) and
#       not (password.islower() or password.isupper())) and
#      ('!' in password or '@' in password or
#       '#' in password or '*' in password or
#       '+' in password or '-' in password)) and
#         not (' ' in password)):
#     print('Пароль подходит')
# else:
#     print('В пароле должно быть минимум 7 знаков, \n'
#           'не должно быть пробелов, \n'
#           'должны быть символы разных регистров, \n'
#           'должен быть хотя бы один спецзнак № * ! + -')


# Проверка номера телефона и пароля на валидность
