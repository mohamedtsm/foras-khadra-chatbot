# 🌿 Foras Khadra - AI Chatbot

An AI-powered chatbot for the **Foras Khadra** platform that helps users find opportunities (scholarships, internships, volunteering, competitions) through natural language conversation.

## 💡 Idea

Users ask in Arabic, French, or English — the chatbot understands the intent and recommends the most relevant opportunities from the database.

**Example questions:**
- "أريد منحة لدراسة الهندسة في أوروبا"
- "What volunteering opportunities are available in Tunisia?"
- "Je cherche un stage en technologie"

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + FastAPI |
| AI Model | LLaMA 3.3 70B via Groq API |
| Frontend | HTML / CSS / Vanilla JS |
| Data | Mock JSON (12 opportunities) |

## ⚙️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/foras-khadra-chatbot
cd foras-khadra-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
```bash
cp .env.example .env
# Edit .env and add your Groq API key
```

Get a free Groq API key at: https://console.groq.com

### 4. Run the server
```bash
uvicorn main:app --reload
```

### 5. Open in browser
```
http://localhost:8000
```

## 🧠 How It Works

1. User sends a message via the chat interface
2. FastAPI backend receives the message + conversation history
3. The full opportunities database (JSON) is injected into the system prompt
4. Groq API (LLaMA 3.3 70B) processes the query with full context
5. The model returns a personalized recommendation
6. Response is streamed back to the frontend

## 📁 Project Structure

```
foras-khadra-chatbot/
├── main.py                  # FastAPI backend + API routes
├── data/
│   └── opportunities.json   # Mock opportunities database (12 entries)
├── static/
│   └── index.html           # Frontend (RTL Arabic UI)
├── requirements.txt
├── .env.example
└── README.md
```

## ✨ Features

- Multilingual support (Arabic / French / English)
- RTL Arabic interface
- Conversation memory (last 6 exchanges)
- Quick suggestion buttons
- Typing indicator
- Mobile responsive

---

Built for **Foras Khadra AI Team Task** — 2026
