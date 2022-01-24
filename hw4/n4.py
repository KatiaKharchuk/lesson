from random import randint
from time import perf_counter
start = perf_counter()

my_list = [randint(-10, 10) for i in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(perf_counter()- start)