import streamlit as st
import json
from snowflake.snowpark.functions import ai_complete

# Connect to Snowflake
try:
    # Works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Works locally and on Streamlit Community Cloud
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

# Cached LLM Function with model parameter
@st.cache_data
def call_llm(prompt_text: str, model: str) -> str:
    """Call Snowflake Cortex LLM with selected model."""
    df = session.range(1).select(
        ai_complete(model=model, prompt=prompt_text).alias("response")
    )
    response_raw = df.collect()[0][0]
    response_json = json.loads(response_raw)
    
    # Extract text from response
    if isinstance(response_json, dict):
        return response_json.get("choices", [{}])[0].get("message", "")
    return str(response_json)

# Generate TL;DR Summary
@st.cache_data
def generate_summary(messages: list) -> str:
    """Generate a TL;DR summary of the conversation."""
    conversation_text = "\n".join([
        f"{msg['role']}: {msg['content']}"
        for msg in messages[-10:]
    ])
    prompt = f"""Please provide a concise TL;DR (Too Long; Didn't Read) summary of the following conversation in 2-3 bullet points:

{conversation_text}"""
    
    df = session.range(1).select(
        ai_complete(model="mistral-7b", prompt=prompt).alias("summary")
    )
    summary_raw = df.collect()[0][0]
    return summary_raw

# Mode-specific system prompts
mode_prompts = {
    "General Chat": "You are a helpful and friendly AI assistant.",
    "Code Assistant": "You are an expert code assistant. Help users with programming questions, debugging, and best practices. Provide code examples when relevant.",
    "Data Analyst": "You are a data analyst expert. Help users understand data, create queries, and provide insights. Focus on SQL and data visualization.",
    "Tech Mentor": "You are a patient technical mentor. Explain complex concepts in simple terms using analogies and examples. Help users learn and understand technology."
}

# --- Main App ---
st.title(":material/chat: Enhanced Chatbot with History")
st.success("AI-powered chatbot with model selection, conversation modes, and full conversation memory")

# --- Sidebar Configuration ---
with st.sidebar:
    st.header(":material/settings: Chatbot Settings")
    
    # Model Selection
    model = st.selectbox(
        "Select Model:",
        {
            "claude-3-5-sonnet - Best reasoning & complex tasks": "claude-3-5-sonnet",
            "mistral-7b - Fast, great for summarization": "mistral-7b",
            "llama3.1-405b - Highest accuracy, handles long documents": "llama3.1-405b",
            "mixtral-8x7b - Balanced reasoning & speed": "mixtral-8x7b",
            "gemma-7b - Cost-effective, simple tasks": "gemma-7b"
        }.values(),
        help="Choose your preferred AI model"
    )
    
    # Conversation Mode
    mode = st.selectbox(
        "Conversation Mode:",
        ["General Chat", "Code Assistant", "Data Analyst", "Tech Mentor"],
        help="Select the conversation style"
    )
    
    # Cache management: Clear cache when model changes
    if "previous_model" not in st.session_state:
        st.session_state.previous_model = None
    if st.session_state.previous_model != model:
        st.cache_data.clear()
        st.session_state.previous_model = model
    
    st.divider()
    
    # Conversation Statistics
    st.header(":material/bar_chart: Conversation Stats")
    if "messages" in st.session_state:
        user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
        assistant_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
        st.metric("Your Messages", user_msgs)
        st.metric("AI Responses", assistant_msgs)
    
    # Clear History Button
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your AI assistant. How can I help you today?"}
        ]
        st.rerun()

# Initialize messages with welcome message
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI assistant. How can I help you today?"}
    ]

# Display all messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Build the full conversation history for context
            conversation = "\n\n".join([
                f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
                for msg in st.session_state.messages
            ])
            
            # Add mode-specific system prompt
            system_prompt = mode_prompts.get(mode, mode_prompts["General Chat"])
            full_prompt = f"{system_prompt}\n\n{conversation}\n\nAssistant:"
            
            # Call LLM with full context
            response = call_llm(full_prompt, model)
            st.markdown(response)
    
    # Add assistant response to state
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

st.divider()
st.caption("Day 11: Enhanced Chatbot with History & Day 10 Features | 30 Days of AI")