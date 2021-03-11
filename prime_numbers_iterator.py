# -*- coding: utf-8 -*-

# Итератор на классах. Выдает последовательность чисел до n
class PrimeNumbers:

    def __init__(self, n):
        self.prime_numbers = []
        self.number = n
        self.next_number = 2

    def __iter__(self):
        # обнуляем список прстых чисел и счетчик
        self.prime_numbers = []
        self.next_number = 2
        return self

    def __next__(self):
        # проходим по списку каждый раз начиная со следующего числа для ускорения
        for number in range(self.next_number, self.number + 1):
            if number == self.number:  # стоп, если прошли по всему списку
                raise StopIteration

            # проходим по списку уже добавленных простых чисел
            for prime in self.prime_numbers:
                if number % prime == 0:  # Если делится без остатка, то значит не наше число
                    break
            else:  # если не было break
                self.prime_numbers.append(number)
                self.next_number = number + 1
                return number


prime_number_iterator = PrimeNumbers(n=10000)
for num in prime_number_iterator:
    print(num)
