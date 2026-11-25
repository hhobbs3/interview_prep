from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from .schema import schema

app = FastAPI()

# Allow all origins for simplicity
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REST endpoints for counter
@app.get("/api/counter")
async def get_counter():
    from .counter import get_counter as get_counter_fn
    return {"counter": get_counter_fn()}

@app.post("/api/counter")
async def increment_counter(amount: int = 1):
    from .counter import increment_counter as inc_fn
    new_value = inc_fn(amount=amount)
    return {"counter": new_value}
@app.get("/api/hello")
async def hello():
    return {"message": "hello world"}

# GraphQL endpoint
graphql_router = GraphQLRouter(
    schema,
    graphql_ide="graphiql"
)

app.include_router(graphql_router, prefix="/graphql")
