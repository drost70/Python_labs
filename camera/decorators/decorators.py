"""
This is a file which contains decorators
"""

import logging

def write_dictionary_of_kwargs(func):
    """
    Decorator that writes the dictionary of key-value arguments to a file.
    """
    def wrapper(*args, **kwargs):
        file_path = "error.log"
        with open(file_path, "a", encoding="utf-8") as file:
            func_name = func.__name__
            file.write(func_name)
            file.write(": ")
            for key, value in kwargs.items():
                arguments = f"{key} = {value}"
                line = f"{arguments},"
                file.write(line)
            file.write("\n")
        return func(*args, **kwargs)

    return wrapper


def exception_writer(func):
    """
    Decorator that writes exceptions and the method causing the exception to a file.
    """
    def wrapper(*args, **kwargs):
        file_path = "camera_exceptions.txt"
        try:
            result = func(*args, **kwargs)
        except (ValueError, TypeError) as exc:
            with open(file_path, 'a', encoding="utf-8") as file:
                file.write(f"Method: {func.__name__}, Exception: {type(exc).__name__}\n")
            raise exc
        return result

    return wrapper


def logged(mode):
    """
    Decorator that logs exceptions either to console or a file.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, TypeError) as exc:
                logger = logging.getLogger()
                logger.setLevel(logging.ERROR)
                formatter = logging.Formatter('Exception occurred: %(message)s')

                if mode == 'console':
                    console_handler = logging.StreamHandler()
                    console_handler.setLevel(logging.ERROR)
                    console_handler.setFormatter(formatter)
                    logger.addHandler(console_handler)
                    logger.error(str(exc))
                elif mode == 'file':
                    file_handler = logging.FileHandler('error.log', encoding="utf-8")
                    file_handler.setLevel(logging.ERROR)
                    file_handler.setFormatter(formatter)
                    logger.addHandler(file_handler)
                    logger.error(str(exc))
                else:
                    raise ValueError('Invalid logging mode') from exc


        return wrapper

    return decorator
