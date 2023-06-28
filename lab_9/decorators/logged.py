import logging


def logged(exception, mode):
    """A decorator that logs exceptions raised by the decorated function.
        Args:
            exception (Exception): The type of exception to be caught and logged.
            mode (str): The logging mode. Can be either "console" or "file".
        Returns:
            function: The decorated function."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as error:
                if mode == "console":
                    logging.basicConfig(format='%(levelname)s - %(message)s')
                    logging.error(error.message)
                elif mode == "file":
                    logging.basicConfig(filename='app.log', filemode='w',
                                        format='%(levelname)s - %(message)s')
                    logging.error(error.message)
                raise error

        return wrapper

    return decorator