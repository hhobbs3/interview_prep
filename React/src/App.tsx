import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'

function App() {
  const [counter, setCounter] = useState(0)
  // New state for the LLM greeting
  const [hello, setHello] = useState('')
// Function to click the counter button programmatically
const handleButtonClick = (times: number = 1) => setCounter((prev) => prev + times)
const [messages, setMessages] = useState<Array<{ user: string; bot: string }>>([]);
const [input, setInput] = useState('')
const sendMessage = async () => {
    if (!input.trim()) return;
    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input })
    });
    const data = await res.json();
    // Execute any UI actions returned by the AI
    if (data.actions) {
      data.actions.forEach((action) => {
        if (action.type === 'CLICK_BUTTON') {
          handleButtonClick(action.times);
        }
      });
    }
    setMessages([...messages, { user: input, bot: data.reply }]);
    setInput('');
  };

  return (
    <>
      <section id="center">
        <div className="hero">
          <img src={heroImg} className="base" width="170" height="179" alt="" />
          <img src={reactLogo} className="framework" alt="React logo" />
          <img src={viteLogo} className="vite" alt="Vite logo" />
        </div>
        <div>
          <h1>Get started</h1>
          <p>
            Edit <code>src/App.tsx</code> and save to test <code>HMR</code>
          </p>
        </div>
        <button
          type="button"
          className="counter"
          onClick={() => handleButtonClick()}
        >
          Count is {counter}
        </button>
        {/* New button that gets counter value */}
        <button
          type="button"
          className="counter"
          onClick={async () => {
            try {
              const res = await fetch('http://localhost:8000/api/counter')
              const data = await res.json()
              setCounter(data.counter)
            } catch (e) {
              console.error(e)
              setCounter(0)
            }
          }}
        >
          Get Counter
        </button>
        {/* New button that increments counter */}
        <button
          type="button"
          className="counter"
          onClick={async () => {
            try {
              const res = await fetch('http://localhost:8000/api/counter', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ amount: 1 }),
              })
              const data = await res.json()
              setCounter(data.counter)
            } catch (e) {
              console.error(e)
              setCounter(0)
            }
          }}
        >
          Increment Counter
        </button>
        {/* Show the message returned from the backend */}
        {counter !== undefined && <p>Counter: {counter}</p>}
      </section>
        <section id="chat-ui">
          <div>
            <h2>Chat with AI</h2>
            <div style={{border:'1px solid #ccc',padding:'8px',maxHeight:'200px',overflowY:'auto'}}>
              {messages.map((m, i) => (
                <p key={i}><strong>You:</strong> {m.user} <br /><strong>AI:</strong> {m.bot}</p>
              ))}
            </div>
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type a message"
            />
            <button onClick={sendMessage}>Send</button>
          </div>
        </section>


      <div className="ticks"></div>

      <section id="next-steps">
        <div id="docs">
          <svg className="icon" role="presentation" aria-hidden="true">
            <use href="/icons.svg#documentation-icon"></use>
          </svg>
          <h2>Documentation</h2>
          <p>Your questions, answered</p>
          <ul>
            <li>
              <a href="https://vite.dev/" target="_blank">
                <img className="logo" src={viteLogo} alt="" />
                Explore Vite
              </a>
            </li>
            <li>
              <a href="https://react.dev/" target="_blank">
                <img className="button-icon" src={reactLogo} alt="" />
                Learn more
              </a>
            </li>
          </ul>
        </div>
        <div id="social">
          <svg className="icon" role="presentation" aria-hidden="true">
            <use href="/icons.svg#social-icon"></use>
          </svg>
          <h2>Connect with us</h2>
          <p>Join the Vite community</p>
          <ul>
            <li>
              <a href="https://github.com/vitejs/vite" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#github-icon"></use>
                </svg>
                GitHub
              </a>
            </li>
            <li>
              <a href="https://chat.vite.dev/" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#discord-icon"></use>
                </svg>
                Discord
              </a>
            </li>
            <li>
              <a href="https://x.com/vite_js" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#x-icon"></use>
                </svg>
                X.com
              </a>
            </li>
            <li>
              <a href="https://bsky.app/profile/vite.dev" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#bluesky-icon"></use>
                </svg>
                Bluesky
              </a>
            </li>
          </ul>
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
