my_list = [34, 3, 65, 23, 87, 334]
new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num -1]]
print(new_list)
