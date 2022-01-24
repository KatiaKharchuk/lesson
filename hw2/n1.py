result_list = [7, None, 37.4, 'hello', {2:'age'},(345, 87)]

for iterator, current_element in enumerate(result_list, 1):
    print(f"{iterator}:::: item vale = {current_element} - and type of ... is {type(current_element)}")

