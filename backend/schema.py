import strawberry
import redis

# Connect to Redis (same as your counter example)
client = redis.Redis(host="127.0.0.1", port=6379, db=0)

@strawberry.type
class Counter:
    value: int

@strawberry.type
class Query:
    @strawberry.field
    def counter(self) -> Counter:
        """Return the current counter value."""
        val = client.get("my_counter")
        return Counter(value=int(val) if val else 0)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def increment_counter(self, amount: int = 1) -> Counter:
        """Atomically increment the counter."""
        new = client.incrby("my_counter", amount)
        return Counter(value=new)

schema = strawberry.Schema(query=Query, mutation=Mutation)