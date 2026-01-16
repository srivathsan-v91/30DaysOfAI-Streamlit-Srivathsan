import streamlit as st
from snowflake.snowpark.functions import ai_complete
import json

st.set_page_config(layout="wide")

st.title(":material/smart_toy: Hello, Cortex!")

# Connect to Snowflake
try:
    # Works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Works locally and on Streamlit Community Cloud
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

# Model selection with strengths
model_options = {
    "claude-3-5-sonnet - Best reasoning & complex tasks": "claude-3-5-sonnet",
    "mistral-7b - Fast, great for summarization": "mistral-7b",
    "llama3.1-405b - Highest accuracy, handles long documents": "llama3.1-405b",
    "mixtral-8x7b - Balanced reasoning & speed": "mixtral-8x7b",
    "gemma-7b - Cost-effective, simple tasks": "gemma-7b"
}

selected_model_text = st.selectbox("Select Model:", list(model_options.keys()), index=0)
model = model_options[selected_model_text]

prompt = st.text_input("Enter your prompt:")

# Run LLM inference
if st.button("Generate Response"):
    # Full response
    df = session.range(1).select(
        ai_complete(model=model, prompt=prompt).alias("response")
    )
    
    # Get and display response
    response_raw = df.collect()[0][0]
    response = json.loads(response_raw)
    
    st.subheader("Full Response:")
    st.write(response)
    
    # Get the actual text from the response
    if isinstance(response, dict) and "choices" in response:
        response_text = response["choices"][0]["messages"]
    else:
        response_text = str(response)
    
    # Summarize the response using AI_SUMMARIZE SQL function
    summary_sql = f"SELECT SNOWFLAKE.CORTEX.SUMMARIZE('{response_text.replace(chr(39), chr(39)+chr(39))}') as summary"
    summary_df = session.sql(summary_sql)
    
    summary_raw = summary_df.collect()[0][0]
    summary = json.loads(summary_raw) if isinstance(summary_raw, str) and summary_raw.startswith('{') else summary_raw
    
    st.subheader("Summarized Response:")
    st.write(summary)

# Footer
st.divider()
st.caption("Day 2: Hello, Cortex! | 30 Days of AI")