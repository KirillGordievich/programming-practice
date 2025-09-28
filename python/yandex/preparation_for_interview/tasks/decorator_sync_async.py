import asyncio
import functools

def sync_async_decorator(func):
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        # Logic to execute before the function call for async functions
        print(f"Async: Before calling {func.__name__}")
        result = await func(*args, **kwargs)
        # Logic to execute after the function call for async functions
        print(f"Async: After calling {func.__name__}")
        return result

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        # Logic to execute before the function call for sync functions
        print(f"Sync: Before calling {func.__name__}")
        result = func(*args, **kwargs)
        # Logic to execute after the function call for sync functions
        print(f"Sync: After calling {func.__name__}")
        return result

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper

# Example usage with a synchronous function
@sync_async_decorator
def my_sync_function():
    """ I love this sync function so much """

    print("Inside synchronous function")
    return "Sync Result"

# Example usage with an asynchronous function
@sync_async_decorator
async def my_async_function():
    """ I love this async function so much """

    print("Inside asynchronous function")
    await asyncio.sleep(0.1)  # Simulate some async work
    return "Async Result"

if __name__ == "__main__":
    # Call the synchronous function
    sync_result = my_sync_function()
    print(f"Returned: {sync_result} from {my_sync_function.__name__} / {my_sync_function.__doc__}")

    # Call the asynchronous function
    async def main():
        async_result = await my_async_function()
        print(f"Returned: {async_result} from {my_async_function.__name__} / {my_async_function.__doc__}")

    asyncio.run(main())