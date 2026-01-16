import streamlit as st
import json
import time
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

# Cached LLM Function
@st.cache_data
def call_cortex_llm(prompt_text):
    """Makes a call to Cortex AI with the given prompt."""
    model = "claude-3-5-sonnet"
    df = session.range(1).select(
        ai_complete(model=model, prompt=prompt_text).alias("response")
    )
    
    # Get and parse response
    response_raw = df.collect()[0][0]
    response_json = json.loads(response_raw)
    return response_json

# Cached Summarize Function
@st.cache_data
def call_cortex_summarize(content_text):
    """Summarize the content from the provided URL/text."""
    model = "mistral-large"
    df = session.range(1).select(
        ai_complete(
            model=model,
            prompt=f"""Please summarize the following content in 2-3 sentences:\n{content_text}"""
        ).alias("summary")
    )
    
    summary_raw = df.collect()[0][0]
    summary_json = json.loads(summary_raw)
    return summary_json

# --- App UI ---

# Input widgets in sidebar
with st.sidebar:
    st.title(":material/post: LinkedIn Post Generator v3")
    st.success("An app for generating LinkedIn post using content from input link and summarizing content.")
    tone = st.selectbox("Tone:", ["Professional", "Casual", "Funny"])
    word_count = st.slider("Approximate word count:", 50, 300, 100)

st.subheader(":material/input: Input content")
content = st.text_input("Content URL:", "https://docs.snowflake.com/en/user-guide/views-semantic/overview")

# Generate button
if st.button("Generate Post"):
    
    # Initialize the status container
    with st.status("Starting engine...", expanded=True) as status:
        
        # Step 1: Construct Prompt
        st.write(":material/psychology: Thinking: Analyzing constraints and tone...")
        time.sleep(1)
        
        prompt = f"""
        You are an expert social media manager. Generate a LinkedIn post based on the following:

        Tone: {tone}
        Desired Length: Approximately {word_count} words
        Use content from this URL: {content}

        Generate only the LinkedIn post text. Use dash for bullet points.
        """
        
        # Step 2: Call API
        st.write(":material/flash_on: Generating: contacting Snowflake Cortex...")
        time.sleep(1)
        
        # This is the blocking call that takes time
        response = call_cortex_llm(prompt)
        
        # Step 3: Update Status to Complete
        st.write(":material/check_circle: Post generation completed!")
        status.update(label="Post Generated Successfully!", state="complete", expanded=False)

    # Display Result
    with st.container(border=True):
        st.subheader(":material/output: Generated post:")
        st.markdown(response)

# Automatically generate summary for the content
st.divider()

# Generate summary (without button - automatic like Day 6)
with st.status("Analyzing content...", expanded=True) as status:
    
    # Step 1: Start analysis
    st.write(":material/psychology: Reading: Extracting key points...")
    
    # Step 2: Call API
    st.write(":material/flash_on: Summarizing: Processing with Snowflake Cortex...")
    
    # This is the blocking call that takes time
    summary = call_cortex_summarize(content)
    
    # Step 3: Update Status to Complete
    st.write(":material/check_circle: Summarization completed!")
    status.update(label="Content Summarized Successfully!", state="complete", expanded=False)

# Display Result
with st.container(border=True):
    st.subheader(":material/summarize: Content Summary:")
    st.markdown(summary)

# Footer
st.divider()
st.caption("Day 7: Theming and Layout | Enhanced with Summarization | 30 Days of AI")