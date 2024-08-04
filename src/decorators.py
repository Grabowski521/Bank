from functools import wraps

def log(filename = None):
    """
    Функция-декоратор, которая регистрирует результат выполнения декорируемой функции.
    @log()
    def my_function(x, y):

    return x + y

    print(my_function(1, 2))
    Декоратор log регистрирует результаты выполнения функции в файл или консоль. Если во время выполнения происходит
    исключение, оно регистрируется вместе с входными аргументами.

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
@log("testlog.txt")
def divide(a, b):
    return a / b


print(divide(1, 2))