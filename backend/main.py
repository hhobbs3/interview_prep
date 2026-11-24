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

# REST endpoint
@app.get("/api/hello")
async def hello():
    return {"message": "hello world"}

# GraphQL endpoint
graphql_router = GraphQLRouter(
    schema,
    graphql_ide="graphiql"
)

app.include_router(graphql_router, prefix="/graphql")
