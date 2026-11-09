import streamlit as st
import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.chat_history import InMemoryChatMessageHistory

from langchain_core.runnables.history import RunnableWithMessageHistory



load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")



st.set_page_config(
    page_title="Chatrix",
    page_icon="🤖",
    layout="centered"
)



st.title("Chatrix")
st.subheader("Your Intelligent AI Assistant")

st.caption("An AI chatbot that remembers your conversations.")



if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}



with st.sidebar:

    st.title("Settings")

    temperature = st.slider(
        "Response Creativity",
        0.0, 1.0, 0.7
    )

    if st.button("Clear Chat"):

        st.session_state.messages = []
        st.session_state.chat_history = {}

        st.rerun()



if not API_KEY:

    st.error("API Key not found. Please check your .env file.")
    st.stop()



llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=temperature,
    api_key=API_KEY
)



prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        "You are MemoMind AI, a friendly and helpful assistant. "
        "Use previous conversation history to answer questions. "
        "Remember details shared by the user within this session."
    ),

    MessagesPlaceholder(variable_name="history"),

    ("human", "{question}")

])



chain = prompt | llm



def get_session_history(session_id):

    if session_id not in st.session_state.chat_history:

        st.session_state.chat_history[session_id] = (
            InMemoryChatMessageHistory()
        )

    return st.session_state.chat_history[session_id]



chatbot = RunnableWithMessageHistory(

    chain,

    get_session_history,

    input_messages_key="question",

    history_messages_key="history"

)



session_id = "memomind_user"



for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])



user_input = st.chat_input("Ask MemoMind anything...")


if user_input:

    st.session_state.messages.append({

        "role": "user",
        "content": user_input

    })

    with st.chat_message("user"):
        st.write(user_input)


    with st.chat_message("assistant"):

        with st.spinner("MemoMind is thinking..."):

            try:

                response = chatbot.invoke(

                    {"question": user_input},

                    config={

                        "configurable": {
                            "session_id": session_id
                        }

                    }

                )

                answer = response.content

                st.write(answer)

                st.session_state.messages.append({

                    "role": "assistant",
                    "content": answer

                })

            except Exception as e:

                st.error("Unable to generate response.")

                st.caption(str(e))


st.divider()

st.caption("MemoMind AI | Built with Python, Streamlit and LangChain")
