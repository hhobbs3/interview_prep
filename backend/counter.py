import redis
import time

# Connect to the local Redis instance that the compose file exposes on port 6379
client = redis.Redis(host="127.0.0.1", port=6379, db=0)

def increment_counter(key="my_counter", amount=1):
    """
    Atomically increments a counter stored in Redis.
    Returns the new value.
    """
    # INCRBY is atomic, so no race conditions
    return client.incrby(key, amount)

def get_counter(key="my_counter"):
    """Return the current value of the counter (or 0 if unset)."""
    val = client.get(key)
    return int(val) if val is not None else 0

if __name__ == "__main__":
    print("Current counter:", get_counter())
    new_value = increment_counter()
    print("After increment:", new_value)