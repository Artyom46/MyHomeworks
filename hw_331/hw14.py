import csv


def simple_password_checker_decorator(func: callable) -> callable:
    def wrapper(password: str) -> str:
        if len(password) < 8:
            raise ValueError('Пароль должен быть не менее 8 символов')
        if not any(map(str.isdigit, password)):
            raise ValueError('Пароль должен содержать минимум 1 цифру')
        if not any(map(str.isupper, password)):
            raise ValueError('Пароль должен содержать минимум 1 заглавную бувку')
        if not any(map(str.islower, password)):
            raise ValueError('Пароль должен содержать минимум 1 строчную букву')
        if not any(map(lambda x: x in '!@#$%^&*()=+-_><?/', password)):
            raise ValueError('Пароль должен содержать минимум 1 спецсимвол')
        return func(password)

    return wrapper


@simple_password_checker_decorator
def register_user(password: str) -> str:
    return f'Пользователь зарегистрирован с паролем {password}'


print(register_user('12345678Zz#'))


def username_validator(func: callable) -> callable:
    """
    Декоратор для валидации имени пользователя
    :param func: Функция для оборачивания
    :return: Обёрнутая функция
    """
    def wrapper(username: str, password: str) -> callable:
        if ' ' in username:
            raise ValueError('В имени пользователя не должно быть пробелов')
        return func(username, password)

    return wrapper


def password_validator(min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1,
                       min_special_chars: int = 1) -> callable:
    """
    Декоратор для валидации пароля
    :param min_length: Минимальная длина пароля
    :param min_uppercase: Минимальное количество больших букв
    :param min_lowercase: Минимальное количество маленьких букв
    :param min_special_chars: Минимальное количество спец. символов
    :return: Обёрнутая функция
    """
    def decorator(func: callable) -> callable:
        def wrapper(username: str, password: str) -> tuple[str, str]:
            if len(password) < min_length:
                raise ValueError(f'Пароль должен быть не короче {min_length} символов')
            if sum(1 for char in password if char.isupper()) < min_uppercase:
                raise ValueError(f'Пароль должен содержать не менее {min_uppercase} символлов в верхнем регистре')
            if sum(1 for char in password if char.islower()) < min_lowercase:
                raise ValueError(f'Пароль должен содержать не менее {min_lowercase} символов в нижнем регистре')
            if sum(1 for char in password if char.isalnum()) < min_special_chars:
                raise ValueError(f'Пароль должен содержать не менее {min_special_chars} спец. символов')
            return func(username, password)

        return wrapper

    return decorator


@username_validator
@password_validator()
def register_user(username: str, password: str) -> None:
    with open('users.csv', 'a', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([username, password])


register_user('user1', '12345678Zz!')


# Декораторы
