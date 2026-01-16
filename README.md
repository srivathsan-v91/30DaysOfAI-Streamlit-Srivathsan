# 30 Days of AI - Streamlit Learning Challenge

## By: Srivathsan V
## Company: EY | Role: Senior Cloud Data Engineer

My personal journey through the #30DaysOfAI challenge with Streamlit and Snowflake Cortex AI.

### Repository Structure

---

| Folder Name | Description | Contents |
|-------------|-------------|----------|
| day_1_connect_snowflake | Connect to Snowflake | streamlit_app.py, pyproject.toml, requirements.txt |
| day_2_hello_cortex | Hello Cortex AI | streamlit_app.py, pyproject.toml |
| day_3_write_streams | Write Streams | streamlit_app.py, pyproject.toml |
| day_4_caching_your_app | Caching Your App | streamlit_app.py, pyproject.toml |
| day_5_linkedin_post_generator | LinkedIn Post Generator | streamlit_app.py, pyproject.toml |
| day_6_content_summary | Content Summarization | streamlit_app.py, pyproject.toml |
| day_7_repost_generation | Repost Generation | streamlit_app.py, pyproject.toml |
| day_8_multipage_chatbot | Multipage Chatbot | streamlit_app.py, pyproject.toml |
| day_9_understanding_session_state | Session State Management | streamlit_app.py, pyproject.toml |
| day_10_enhanced_chatbot | Enhanced Chatbot | streamlit_app.py, pyproject.toml |
| day_11_streaming_responses | Streaming Responses | streamlit_app.py, pyproject.toml |

---

### Key Enhancements Made

**Days 6 & 7 (LinkedIn Post Generator)**
- ✅ Content summarization alongside post generation
- ✅ Dark mode theming via config.toml
- ✅ Sidebar layout with Material Design icons
- ✅ Real-time progress feedback with st.status()

**Days 8 & 9 (Chat Foundation)**
- ✅ Chat UI with st.chat_message() and st.chat_input()
- ✅ Session State for persistent data

**Day 10 (Enhanced Chatbot)**
- ✅ Model selector dropdown (Claude 3.5 Sonnet / Mistral Large)
- ✅ Conversation mode selector (General Chat / Code Assistant / Data Analyst / Tech Mentor)
- ✅ Auto TL;DR summary at 10+ messages using session state counter
- ✅ Sidebar organization with clear history button
- ✅ Message counter display
- ✅ Status containers for response generation

### Tech Stack

- **Streamlit** - Interactive UI framework
- **Snowflake** - Cloud data platform
- **Cortex AI** - LLM inference (Claude 3.5 Sonnet, Mistral Large)
- **Python** - Core language
- **GitHub** - Version control & sharing

### Daily Progress

- [x] Day 1-5: Foundation & LinkedIn Generator
- [x] Day 6-7: Content Summarization & Theming
- [x] Day 8-9: Chat Elements & Session State
- [x] Day 10: Enhanced Chatbot
- [x] Day 11: Streaming Responses
### How to Use

Each Python file is a standalone Streamlit app. To run:

```bash
streamlit run day_10_chatbot_enhanced.py
```

### Learning Insights

- Session State is per-user, not global (use DB for shared state)
- Streamlit reruns entire script on every interaction
- Caching (@st.cache_data) eliminates duplicate API calls
- Material Design icons enhance UX without images
- Dark mode improves professional appearance

---

**Challenge**: #30DaysOfAI  
**Author**: Srivathsan V  
**Company**: EY #EYAllIn  
**Last Updated**: January 16, 2026
