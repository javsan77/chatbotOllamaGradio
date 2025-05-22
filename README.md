# 🤖 Chatbot with Ollama and Gradio

This is a simple AI chatbot application that integrates [Ollama](https://ollama.com) — a local LLM runner — with [Gradio](https://www.gradio.app) — a web interface framework for building ML apps.

## 🚀 Features

- Uses a local large language model (e.g., LLaMA 3) served via Ollama.
- Interactive, clean, and easy-to-use web chat interface using Gradio.
- Keeps a running conversation history.
- Fully offline and runs locally on your machine.

---

## 🧰 Requirements

- Ubuntu Linux (tested on Ubuntu 22.04)
- Python 3.8 or higher
- `pip`
- At least 8 GB of RAM (16 GB recommended for LLaMA 3)
- Ollama installed and a model available (e.g., `llama3`)

---

## ⚙️ Installation and Usage

### 1. Install Ollama

Download and install Ollama from the official site:  
👉 https://ollama.com/download

### 2. Run a model with Ollama

Open a terminal and pull the model:

```bash
ollama run llama3
````

Leave this running or ensure Ollama is running in the background.

### 3. Install Python dependencies

In the same folder as your Python script, run:

```bash
pip install gradio requests
```

### 4. Run the chatbot

Save the script as `chatbot_ollama_gradio.py`, then execute:

```bash
python3 chatbot_ollama_gradio.py
```

This will launch the Gradio web interface in your default browser.

---

## 🗂 File Structure

```
chatbot_ollama_gradio.py   # Main chatbot script
README.md                  # This documentation file
```

---

## 🧠 How It Works

* Sends user messages to the local Ollama server at `http://localhost:11434/api/chat`
* Constructs a chat history using the format expected by the OpenAI-style API.
* Displays messages in a chat UI powered by Gradio.

---

## 📝 Example Conversation

```text
User: Hello!
Assistant: Hello! How can I help you today?

User: What's the capital of France?
Assistant: The capital of France is Paris.
```

---

## 📄 License

This project is provided for educational purposes only. Please consult each model's license on the Ollama website before using in production.

