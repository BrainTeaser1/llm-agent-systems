import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

## Page Configuration
st.set_page_config(
    page_title="Langchain QA Chatbot",
    page_icon=":robot_face:",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Title
st.title("Langchain QA Chatbot")
st.markdown("Ask anything.")

with st.sidebar:
    st.header("Settings")

    model_name = st.selectbox(
        "Select Model",
        options=["gpt-4o", "gpt-4.1-mini"],  # ✅ fixed names
        index=0
    )

    if st.button("Clear Conversation"):
        st.session_state["conversation"] = []
        st.rerun()

# Initialize Chat History
if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

# Model Deployment Mapping
MODEL_DEPLOYMENTS = {
    "gpt-4o": "gpt-4o",
    "gpt-4.1-mini": "gpt-4.1-mini"
}

# Initialize Chain
@st.cache_resource
def get_chain(model_name):
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

    if not api_key or not endpoint:
        st.error("Missing API key or endpoint in .env")
        return None

    deployment_name = MODEL_DEPLOYMENTS.get(model_name)

    if not deployment_name:
        st.error(f"Model {model_name} not configured")
        return None

    try:
        model = AzureChatOpenAI(
            azure_endpoint=endpoint,
            deployment_name=deployment_name,
            api_key=api_key,
            api_version="2024-12-01-preview",
            temperature=0.7,
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant."),
            ("user", "{question}")
        ])

        return prompt_template | model | StrOutputParser()

    except Exception as e:
        st.error(f"Deployment error: {e}")
        return None

chain = get_chain(model_name)

if not chain:
    st.warning("Enter API key to use chatbot")

else:
    # Display Conversation
    for message in st.session_state["conversation"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if question := st.chat_input("Ask a question..."):

        # Add user message
        st.session_state["conversation"].append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.write(question)

        # Assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            try:
                for chunk in chain.stream({"question": question}):  # ✅ fixed variable
                    if chunk:
                        full_response += chunk
                        message_placeholder.markdown(full_response + "▌")

                message_placeholder.markdown(full_response)

            except Exception as e:
                 st.error("Model not available / deployment issue")
                 full_response = "Please select a valid deployed model."

        # Store assistant response
        st.session_state["conversation"].append(
            {"role": "assistant", "content": full_response}  # ✅ fixed variable
        )
