# -*- coding: utf-8 -*-

# Функция генератор, которая выдает последовательость простых чисел
def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        # проходим по списку уже добавленных простых чисел
        for prime in prime_numbers:
            if number % prime == 0:  # Если делится без остатка, то значит не наше число
                break
        else:  # если не было break
            yield number
            prime_numbers.append(number)


for num in prime_numbers_generator(n=10000):
    print(num)
