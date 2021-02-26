def generate_password(length: int) -> str:
    """
    generate password with given length
    Homework
    функция должна возвращать строку из случайных символов заданной длины.
    """
    return ''


def encrypt_message(message: str) -> str:
    key = 2
    return ''.join( chr(num + key) for num in map(ord, message) )


def lucky_number(ticket: str) -> bool:
    """
    lucky number (tram ticket)
    667766 - is lucky (6 + 6 + 7 == 7 + 6 + 6)
    сумма первых трех числе должна равняться сумме последних трех чисел
    """
    return True


def fizz_buzz(num: int) -> str:
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"



def password_is_strong(password) -> bool:
    """
    is password is strong
    (has number, char, lowercase, uppercase, at least length is 10)
    вернуть True если пароль надежный
    Праметры:
        1. Пароль должен содержать как минимум одну цифру
        2. Пароль должен содержать как минимум один сивол в нижнем регистре
        3. Пароль должен содержать как минимум один сивол в верхнем регистре
        4. Пароль должен быть как минимум 10 символов
    """


    return True

def number_is_prime(num: int) -> bool:
    """
    number is prime
    на вход принимаем число
    вернуть True если число является простым
    https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE#:~:text=2%2C%203%2C%205%2C%207,%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%B1%D1%8B%D1%82%D1%8C%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%8B%D0%BC%20%D0%BD%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D1%82%D1%81%D1%8F%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D1%82%D0%BE%D0%B9.
    """
    return True


def decrypt_message(message: str) -> str:

    key = 2
    return ''.join(chr(num - key) for num in map(ord, message))



def volume_of_sphere(radius: float) -> float:
    """
    Volume of a Sphere
    на вход принимаем радиус сферы.
    Необходимо рассчитать объем сферы и округлить результат до двух знаков после точки
    round to 2 places
    """
    return 0.0


def days_diff(start_date: ..., end_date: ...) -> int:
    """
    calculate number of days between two dates.
    найти разницу между двумя датами
    """
    return 0


def prs(client_choice: str) -> bool:
    """
    paper rock scissors
    принимаем значение от клиента из списка значений (например ['p', 'r', 's'])
    сгенерировать случайный выбор на сервере
    реализовать игру в камень-ножницы-бумага между клиент-сервер
    """
    return True


def integer_as_roman(integer: int) -> str:
    """
    ***
    integer to Roman Number
    вывести значение в виде римского числа
    """
    return ''





if __name__ == '__main__':
    assert encrypt_message('Dima') == 'Fkoc'

if __name__ == '__main__':
    assert decrypt_message('Ucujc') == 'Sasha'