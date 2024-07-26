from functools import wraps

def log(filename = None):
    """
    @log()
    def my_function(x, y):

    return x + y

    print(my_function(1, 2))
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})")
                raise e

        return wrapper

    return decorator

@log()
def my_function(x, y):

    return x + y


print(my_function(1, 2))