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
    conversation_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages[-10:]])
    prompt = f"""Please provide a concise TL;DR (To Long; Didn't Read) summary of the following conversation in 2-3 sentences:

{conversation_text}"""
    
    df = session.range(1).select(
        ai_complete(model="mistral-large", prompt=prompt).alias("summary")
    )
    
    summary_raw = df.collect()[0][0]
    summary_json = json.loads(summary_raw)

    return summary_raw

# --- Sidebar Configuration ---
with st.sidebar:
    st.title(":material/chat: Enhanced Chatbot")
    st.success("AI-powered chatbot with model selection and conversation modes")
    
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
        st.cache_data.clear()  # Clear all cached data
        st.session_state.previous_model = model
    
    # Mode-specific system prompts
    mode_prompts = {
        "General Chat": "You are a helpful and friendly AI assistant.",
        "Code Assistant": "You are an expert programming assistant. Provide code examples and explanations.",
        "Data Analyst": "You are a data analysis expert. Help with data insights and patterns.",
        "Tech Mentor": "You are a patient tech mentor. Explain concepts in simple terms."
    }
    
    st.divider()
    
    # Message Counter
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    message_count = len([m for m in st.session_state.messages if m["role"] == "user"])
    st.metric("Messages", message_count)
    
    # Clear History Button
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.caption("Day 10: Enhanced Chatbot | 30 Days of AI")

# --- Main Chat Interface ---
st.title(":material/chat: My First Chatbot")
st.subheader(f"Mode: {mode} | Model: {model}")

# Initialize messages list in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Auto-generate TL;DR at 10 messages
if len(st.session_state.messages) >= 10 and len(st.session_state.messages) % 10 == 0:
    st.divider()
    st.subheader(":material/summarize: Conversation Summary")
    summary = generate_summary(st.session_state.messages)
    st.info(summary)
    st.divider()

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Generate and display assistant response with status
    with st.chat_message("assistant"):
        with st.status(f"Generating response using {model}...", expanded=True):
            st.write(":material/psychology: Thinking...")
            full_prompt = f"{mode_prompts[mode]}\n\nUser: {prompt}"
            response = call_llm(full_prompt, model)
            st.write(":material/check_circle: Response ready!")
        
        st.write(response)
    
    # Add assistant response to state
    st.session_state.messages.append({"role": "assistant", "content": response})

st.divider()
st.caption("Day 10: Enhanced Chatbot with Model Selection & TL;DR | 30 Days of AI")