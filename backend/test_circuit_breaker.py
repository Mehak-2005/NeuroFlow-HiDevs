import asyncio

from resilience.circuit_breaker import CircuitBreaker, CircuitOpenError

breaker = CircuitBreaker("openai")


async def failing_function():
    raise Exception("API failed")


async def test():

    for i in range(5):
        try:
            await breaker.call(failing_function)
        except Exception:
            print(f"Failure {i + 1}")

    try:
        await breaker.call(failing_function)
    except CircuitOpenError:
        print("CircuitOpenError triggered successfully")


asyncio.run(test())