# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    try:
        res = x ** y
    except TypeError:
        return 'Ведите положительное число и отрицательное целое число!'
    return res


print(my_func(5.5, -5))


# --------------------------------------------------------

def my_func_2(x, y):
    try:

        if x <= 0 or y >= 0:
            return 'Ведите x - положительное, y - целое и отрицательное!'
        else:
            num = 1

            for _ in range(abs(y)):
                num /= x
            return f'x в степени y: {round(num, 9)}'
    except ValueError:
        return 'Вводите только числа!'


print(my_func_2(float(input("Введите положительное число: ")), int(input("Введите целое отрацельное число: "))))
