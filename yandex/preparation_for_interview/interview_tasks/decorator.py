import random
from time import sleep
from typing import Tuple, Type


def debug(func):
    def wrapper(*args, **kwargs):
        print(f'Run {str(func).split()[1]} with args: {args}, kwargs: {kwargs}')
        return func(*args, **kwargs)

    return wrapper


def retry(times: int, exceptions: Tuple[Type[Exception]] = Exception, attempt_delay: int = 2000):
    """
    Retry Decorator
    Retries the wrapped function/method `times` times if the exceptions listed
    in ``exceptions`` are thrown
    :param attempt_delay:
    :param times: The number of times to repeat the wrapped function/method
    :param exceptions: Lists of exceptions that trigger a retry attempt
    """

    def decorator(func):
        def newfn(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except exceptions as ex:
                    if attempt >= times:
                        raise
                    print(
                        'Exception thrown when attempting to run %s, attempt '
                        '%d of %d, wait %i second before new attempt'
                        ', error: %s' % (str(func).split()[1], attempt + 1, times, attempt_delay, ex)
                    )
                    attempt += 1
                    sleep(attempt_delay)

        return newfn

    return decorator


@retry(10, exceptions=(Exception,), attempt_delay=1)
@debug
def test(a: int, b: int) -> int:
    if random.randint(0, 1) != 1:
        raise Exception("Some random problem")
    return a + b


def main():
    test(1, b=2)


if __name__ == "__main__":
    main()
