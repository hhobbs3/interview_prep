# Setting Up a Local LLM with Frontend Tool Calling

Many new web workflows involve integrating pathways for AI to affect the site – e.g. a chatbot that collects details and then registers you as a patient. If you have a React front‑end with a Python backend, you can keep it simple by letting the AI *click* buttons a number of times based on a conversation. The easiest way to let an AI affect your site is **Frontend Tool Calling** (Structured Action Payloads). Instead of letting the AI manipulate the DOM directly, your Python backend uses LLM Tool Calling to decide when an action should happen, sends a simple JSON instruction alongside the chat text to React, and React triggers your existing state functions.

## How the Architecture Works

1. **User chats**: "Please increment the counter 3 times."
2. **Python Backend (FastAPI/Flask)**: Calls the LLM with a defined tool (e.g., `click_button(times: int)`). The LLM responds with a tool call instead of—or alongside—text.
3. **API Response**: Python returns both the chat reply and an actions array to React:
   ```json
   {
     "reply": "Sure, I've clicked the button 3 times for you!",
     "actions": [{ "type": "CLICK_BUTTON", "count": 3 }]
   }
   ```
4. **React Frontend**: Checks for actions in the API response and executes your standard React state setter.

## Minimal Implementation Example

### 1. Python Backend (FastAPI + OpenAI/Gemini/Ollama SDK)

```python
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Define the tool schema for your LLM
# (compatible with OpenAI, Anthropic, Gemini, and local Ollama models)

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

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    # 1. Send req.message + tools to your LLM client
    # (Pseudo-code representing standard LLM tool‑call response)
    llm_response = call_your_llm(messages=[{"role": "user", "content": req.message}], tools=tools)
    
    actions = []
    reply_text = llm_response.content or "Done!"

    # 2. If the LLM decided to use the tool, package it for React
    if llm_response.tool_calls:
        for tool in llm_response.tool_calls:
            if tool.function.name == "click_counter_button":
                args = json.loads(tool.function.arguments)
                actions.append({
                    "type": "CLICK_BUTTON",
                    "times": args.get("times", 1)
                })
                reply_text = f"Clicking the button {args.get('times', 1)} time(s)."

    return {"reply": reply_text, "actions": actions}
```

### 2. React Frontend

```jsx
import { useState } from 'react';

export default function App() {
  const [count, setCount] = useState(0);
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  // The normal button handler
  const handleButtonClick = (times = 1) => {
    setCount(prev => prev + times);
  };

  const sendMessage = async () => {
    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();

    // Execute any UI actions returned by the AI
    if (data.actions && data.actions.length > 0) {
      data.actions.forEach(action => {
        if (action.type === 'CLICK_BUTTON') {
          handleButtonClick(action.times);
        }
      });
    }

    setMessages([...messages, { user: input, bot: data.reply }]);
    setInput('');
  };

  return (
    <div>
      {/* Standard UI Button */}
      <button onClick={() => handleButtonClick(1)}>
        Clicked {count} times
      </button>

      {/* Simple Chat Interface */}
      <div>
        {messages.map((m, i) => (
          <p key={i}>
            <strong>You:</strong> {m.user} <br />
            <strong>AI:</strong> {m.bot}
          </p>
        ))}
        <input value={input} onChange={e => setInput(e.target.value)} />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}
```

## Why This Pattern Scales Well

* **Zero DOM Fragility** – You are triggering clean React state updates instead of fragile `document.querySelector(...).click()`.
* **Easy to Expand** – Add a `submit_patient_form` tool with parameters (`name`, `dob`, `symptoms`) and map `action.type === 'FILL_FORM'` to your form’s state setters.
* **Works with Streaming** – If you later switch to Server‑Sent Events (SSE) or WebSockets, just emit an action event chunk mid‑stream.

## Getting a Local LLM (Ollama) – $0 Setup

1. **Pull a Tool‑Capable Model** – e.g. `qwen2.5:7b` or `llama3.1:8b`:
   ```bash
   ollama pull qwen2.5:7b
   ```

2. **Install the Python Library** – FastAPI + Ollama client:
   ```bash
   pip install ollama fastapi uvicorn
   ```

3. **Connect Python to Your Local Model** – Replace the placeholder in the earlier FastAPI example:
   ```python
   import ollama
   from fastapi import FastAPI
   from pydantic import BaseModel

   app = FastAPI()
   # ... (tool definition remains same)

   @app.post("/chat")
   def chat_endpoint(req: ChatRequest):
       response = ollama.chat(
           model="qwen2.5:7b",
           messages=[{"role": "user", "content": req.message}],
           tools=tools
       )

       actions = []
       reply_text = response["message"].get("content", "")

       if response["message"].get("tool_calls"):
           for tool in response["message"]["tool_calls"]:
               if tool["function"]["name"] == "click_counter_button":
                   times = tool["function"]["arguments"].get("times", 1)
                   actions.append({"type": "CLICK_BUTTON", "times": times})
                   reply_text = f"Clicking the button {times} time(s)."

       return {"reply": reply_text, "actions": actions}
   ```

> **Tip** – If the model ignores your tool or hallucinated arguments, increase the context window (`num_ctx`) to avoid cutting off tool definitions.

## Next Steps

* **Cloud API Free Tiers** – If your machine struggles with local models, consider free tiers from Google Gemini API or Groq.
* **Confirm Before Executing** – You can prompt the user for confirmation before applying actions (e.g., a "Confirm Registration" popup).
* **Testing** – Run `uvicorn app:app --reload` to start the backend and test the chat flow locally.

---

> **Need more help?** Tell us which LLM provider or framework you prefer, or if you'd like a step‑by‑step test walkthrough on your local machine.