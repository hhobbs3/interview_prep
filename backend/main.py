from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from pydantic import BaseModel
import ollama
from schema import schema as schema_obj
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tool definitions for LLM

tools = [
    {
        "type": "function",
        "function": {
            "name": "click_counter_button",
            "description": "Clicks the counter button on the user's screen a specific number of times.",
            "parameters": {
                "type": "object",
                "properties": {
                    "times": {
                        "type": "integer",
                        "description": "Number of times to click the button"
                    }
                },
                "required": ["times"]
            }
        }
    }
]

class ChatRequest(BaseModel):
    message: str

# Chat endpoint using Ollama

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[{"role": "user", "content": req.message}],
        tools=tools
    )
    # handle response…
    return {"reply": "…", "actions": []}



# REST endpoints for counter
@app.get("/api/counter")
async def get_counter():
    from counter import get_counter as get_counter_fn
    return {"counter": get_counter_fn()}

@app.post("/api/counter")
async def increment_counter(req: dict = {"amount":1}):
    from counter import increment_counter as inc_fn
    amount = req.get("amount", 1)
    new_value = inc_fn(amount=amount)
    return {"counter": new_value}
@app.get("/api/hello")
async def hello():
    return {"message": "hello world"}

# GraphQL endpoint
graphql_router = GraphQLRouter(
    schema_obj,
    graphql_ide="graphiql"
)

app.include_router(graphql_router, prefix="/graphql")
