#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца
print(my_favorite_movies[0:10])
print(my_favorite_movies[42:])
print(my_favorite_movies[12:25])
print(my_favorite_movies[35:40])

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

