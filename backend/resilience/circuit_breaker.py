import time

class CircuitOpenError(Exception):
    pass


class CircuitBreaker:

    def __init__(
        self,
        name,
        failure_threshold=5,
        recovery_timeout=60,
        half_open_max_calls=3
    ):
        self.name = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_max_calls = half_open_max_calls

        self.failure_count = 0
        self.state = "CLOSED"
        self.opened_at = None

    async def call(self, func, *args, **kwargs):

        if self.state == "OPEN":
            if time.time() - self.opened_at > self.recovery_timeout:
                self.state = "HALF_OPEN"
            else:
                raise CircuitOpenError("Circuit is OPEN")

        try:
            result = await func(*args, **kwargs)

            self.failure_count = 0
            self.state = "CLOSED"

            return result

        except Exception:
            self.failure_count += 1

            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
                self.opened_at = time.time()

            raise