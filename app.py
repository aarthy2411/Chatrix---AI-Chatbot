import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage


st.set_page_config(
    page_title="Chatrix AI",
    page_icon="🤖",
    layout="centered"
)


st.title("Chatrix AI")
st.caption("Your intelligent AI conversation partner")


llm = ChatOllama(
    model="gemma3:1b",
    temperature=0.7
)


if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.title("Chat Settings")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Chatrix, a helpful AI assistant. "
               "Answer questions clearly and naturally."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


user_input = st.chat_input("Ask me anything...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    
    history = []

    for msg in st.session_state.messages[:-1]:

        if msg["role"] == "user":
            history.append(HumanMessage(content=msg["content"]))

        else:
            history.append(AIMessage(content=msg["content"]))

    
    with st.chat_message("assistant"):

        with st.spinner("Chatrix is thinking..."):

            try:
                response = chain.invoke({
                    "history": history,
                    "input": user_input
                })

                answer = response.content

                st.write(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"Error: {e}")
