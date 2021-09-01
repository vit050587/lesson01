# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

spisok = [7, 5, 3, 3, 2]
print(f"Рейтинг: {spisok}")
i = float(input("Введите число: "))
while i:
    for el in range(len(spisok)):
        if spisok[el] == i:
            spisok.insert(el, i) # Добавляет цифру, если она уже есть, не по условию задачи.Поменяйте строку 3 и проверьте цифрой
                                 # была ошибка в строке (el +1, i) тем самым отодвигал введенную цифру вперед по списку - соответственно вправо.
                                 # i = float(input("Введите число: "))
            break
        elif spisok[0] < i:
            spisok.insert(0, i)
        elif spisok[-1] > i:
            spisok.append(i)
        elif spisok[el] > i and spisok[el + 1] < i:
            spisok.insert(el + 1, i)
    print(f"Обновленный рейтинг: {spisok}")
    i = int(input("Введите число: "))

#цикл бесконечный но тем и интересен.)

# -------------------------Решение GB--------------------------------------

my_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
new_namber = int(input('Введите новый элемент рейтинга в виде натурального числа: '))
i = 0
for n in my_list:
    if new_namber <= n:
        i += 1
    else:
        break
my_list.insert(i, new_namber)
print(my_list)
