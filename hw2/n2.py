my_list = list(input(" ВВедите числа без пробелов -"))

for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
print(my_list)




my_list = input(' введите числа с пробелами-').split()
for i in range(1,len(my_list), 2):
    my_list.insert(i-1, my_list.pop(i))
    print(my_list)