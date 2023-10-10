def func_details_decorator(func):
    func_name = func.__name__

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func_name}-INPUT: args = {args}, kwargs = {kwargs}')
        print(f'{func_name}-OUTPUT: {result}')
        return result
    return wrapper
