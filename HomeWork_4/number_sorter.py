def is_int_checker(val):
    try:
        return int(val)
    except ValueError:
        return -1


def number_sorter(num_str):
    num_list = [is_int_checker(x) for x in (
        num_str.split(' '))]
    odd_numbers = list(filter(lambda x: x % 2 != 0 and x > 0, num_list))
    even_numbers = list(filter(lambda x: x %
                        2 != 0 and x >= 0 or x == 0, num_list))
    negative_numbers = list(filter(lambda x: x < 0, num_list))

    print(odd_numbers, even_numbers, negative_numbers)


values = input('Write numbers with spaces separated: ')
number_sorter(values)
