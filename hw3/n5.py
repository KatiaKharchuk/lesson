def sum_num():
    s = 0
    while True:
        in_list = input('введите числа или Q для выхода: ').split()
        for num in in_list:
            if num == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print('чтобы выйти из программы нажмите q ')

        print(f'сумма чисел = {s}')

print(sum_num())
