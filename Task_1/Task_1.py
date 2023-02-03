# Создайте список из случайных чисел. Найдите количество различных элементов в нем.
import random

n = int(input("Задайте количество элементов: "))
some_list = []
for i in range(n):
    some_list.append(random.randint(1, 10))
print('Создан список:', some_list)
print('Различных элементов в списке:', len(set(some_list)))