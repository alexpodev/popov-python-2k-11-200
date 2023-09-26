def find_max(*args):
    try:
        max_val = 0
        for i in args:
            if i > max_val:
                max_val = i
        return max_val 
    except TypeError as e:
        return e
    
print(find_max(1, 2, 3, 4, 5))