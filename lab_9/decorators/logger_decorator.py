"""
 logger decorator
"""
import datetime


def method_call_history_decorator(file_path):
    """
            A decorator that stores the history of method calls in a file.

            param:  Arguments of the method.
            param:  Key arguments to the method.
            return: The result of the method execution.
            """

    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(file_path, 'a', encoding="UTF-8") as file:
                file.write(f"Метод '{func.__name__}' був викликаний {current_time}\n")

            return func(*args, **kwargs)

        return wrapper

    return decorator
