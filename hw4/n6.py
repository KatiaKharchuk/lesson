from itertools import count, cycle

print('Программа генерирует целые числа, начиная с указанного . для генерации нажать Enter', 'для выхода q')
for i in count(int(input('введите стартовое число - '))):
    print(i, end=' ')
    quit = input()
    if quit =='q':
        break