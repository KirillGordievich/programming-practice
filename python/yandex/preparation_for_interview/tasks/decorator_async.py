import asyncio
import random
from asyncio import sleep as async_sleep, iscoroutinefunction
from random import randint
from typing import Tuple, Type


def retry(times: int, exceptions: Tuple[Type[Exception]] = Exception, attempt_delay: int = 1):
    """
    Retry Decorator
    Retries the wrapped function/method `times` times if the exceptions listed
    in ``exceptions`` are thrown
    :param attempt_delay:
    :param times: The number of times to repeat the wrapped function/method
    :param exceptions: Lists of exceptions that trigger a retry attempt
    """

    def decorator(func):
        async def newfn(*args, **kwargs):
            attempt = 1
            while True:
                try:
                    return await func(*args, **kwargs)
                except exceptions as ex:
                    if attempt >= times:
                        raise ex
                    print(
                        'Exception thrown when attempting to run %s, attempt '
                        '%d of %d, wait %i second before new attempt'
                        ', error: %s' % (str(func).split()[1], attempt, times, attempt_delay, ex)
                    )
                    attempt += 1
                    await async_sleep(attempt_delay)

        return newfn

    return decorator


@retry(5, exceptions=(Exception,))
async def test(a: int, b: int) -> int:
    if random.randint(0, 1) != 1:
        raise Exception("Some random problem")
    return a + b


async def main():
    await test(1, 2)


if __name__ == "__main__":
    asyncio.run(main())
