# Chatrix – AI Chatbot

Chatrix is an AI-powered chatbot developed using Python and Streamlit. It uses LangChain to manage conversations and Ollama to generate intelligent responses through a locally running AI model.

## Features

- AI-powered conversations
- Context-aware responses
- Conversation memory
- Interactive chat interface
- Clear chat functionality
- Local AI model integration


## Technologies Used

- Python
- Streamlit
- LangChain
- Ollama
- Gemma 3 (1B)


## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/aarthy2411/Chatrix-AI-Chatbot.git
```

**2. Navigate to the project folder**

```bash
cd Chatrix-AI-Chatbot
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Download the Ollama model**

```bash
ollama pull gemma3:1b
```

**5. Run the application**

Chatrix AI runs locally using Streamlit and Ollama.

```bash
streamlit run app.py
```

Open your browser at:

http://localhost:8501/

## How It Works

Chatrix uses Ollama to run the Gemma 3 language model locally. LangChain manages conversation prompts and previous messages, while Streamlit provides an interactive interface for users to communicate with the AI assistant.

## Future Enhancements

- Multiple chat sessions
- Permanent conversation storage
- Improved user interface
- Customizable AI responses
- Chat export functionality

## Author

**Aarthy V**
