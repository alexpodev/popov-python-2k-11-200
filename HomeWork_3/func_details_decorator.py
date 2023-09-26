def func_details_decorator(func):
    func_name = func.__name__

    def wrapper(*args, **kwargs):
        print(f'{func_name}-INPUT: args = {args}, kwargs = {kwargs}')
        print(f'{func_name}-OUTPUT: {func(*args, **kwargs)}')
        return func(*args, **kwargs)
    return wrapper
