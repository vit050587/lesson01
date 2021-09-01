# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def str_num():
    summa = 0
    while True:
        string_num = input('Введите числа, через пробел: ').split()
        for num in string_num:
            if num.lower() == "q":
                return summa
            else:
                try:
                    summa += int(num)
                except ValueError:
                    print('Для выхода нажмите "q"')
        print(f'Сумма введенных чисел:  {summa}')


print(str_num())