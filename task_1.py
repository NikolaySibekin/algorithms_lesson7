# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100].
#  Вывести на экран исходный и отсортированный массивы.
import random


def bubble_sort(array):
    for i in range(len(array), 0, -1):

        for j in range(1, i):
            if array[j - 1] < array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]

    return array


array_new = [i for i in range(-100, 100)]
random.shuffle(array_new)
print("Исходный массив:\n", array_new)

bubble_sort(array_new)
print("Конечный массив:\n", array_new)

