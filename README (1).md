# Chatbot

A personal chatbot built with **Streamlit** and **LangChain**, powered by **Mistral AI** (`ministral-8b-latest`).

Pick a personality — Angry, Sad, Funny, or Normal — and chat with an AI agent that responds in that tone.

---

## Features

- Choose a chatbot personality before starting a conversation
- Persistent chat history within a session
- Clean, themed UI with mode-specific colors
- Type `0` to end the conversation
- Restart anytime to pick a new personality

---

## Tech stack

- [Streamlit](https://streamlit.io/) — UI
- [LangChain](https://www.langchain.com/) — message/chat orchestration
- [Mistral AI](https://mistral.ai/) — LLM (`ministral-8b-latest`)
- Python-dotenv — environment variable management

---

## Project structure

```
Chatbot/
├── chatmodels/
│   ├── chat.py
│   ├── chatbot.py
│   ├── huggingface.py
│   └── uichatbot.py            # main Streamlit app
├── embeddingmodels/
│   └── huggingfaceembedding.py
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/prajnarao24/Chatbot.git
cd Chatbot
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
Create a `.env` file in the project root:
```
MISTRAL_API_KEY=your-api-key-here
```

### 5. Run the app
```bash
streamlit run chatmodels/uichatbot.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Deployment

This app can be deployed for free on [Streamlit Community Cloud](https://share.streamlit.io/):

1. Push this repo to GitHub (already done ✅)
2. Go to share.streamlit.io and sign in with GitHub
3. Click **New app**, select this repo and branch
4. Set the main file path to `chatmodels/uichatbot.py`
5. Under **Advanced settings → Secrets**, add:
   ```
   MISTRAL_API_KEY = "your-actual-key-here"
   ```
6. Click **Deploy**

---

## License

This project is open source and available for personal or educational use.
