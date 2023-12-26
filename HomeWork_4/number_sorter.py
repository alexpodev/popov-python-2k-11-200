def is_int_checker(val):
    try:
        return int(val)
    except ValueError:
        return -1
    
def is_odd_checker(val):
    if val % 2 != 0 and val > 0:
        return val
    
def is_even_checker(val):
    if val % 2 == 0 and val >= 0 or val == 0:
        return val
    
def is_negative_checker(val):
    if val < 0:
        return val


def number_sorter(num_str):
    num_list = [is_int_checker(x) for x in (num_str.split(' '))]
    
    #odd_numbers = list(filter(lambda x: x % 2 != 0 and x > 0, num_list))
    #even_numbers = list(filter(lambda x: x % 2 == 0 and x >= 0 or x == 0, num_list))
    #negative_numbers = list(filter(lambda x: x < 0, num_list))
    
    odd_numbers = [i for i in list(map(is_odd_checker, num_list)) if i is not None]
    even_numbers = [i for i in list(map(is_even_checker, num_list)) if i is not None]
    negative_numbers = [i for i in list(map(is_negative_checker, num_list)) if i is not None]

    print(odd_numbers, even_numbers, negative_numbers)


values = input('Write numbers with spaces separated: ')
number_sorter(values)
