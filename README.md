# 30 Days of AI - Streamlit Learning Challenge

## By: Srivathsan V
## Company: EY | Role: Senior Cloud Data Engineer

My personal journey through the #30DaysOfAI challenge with Streamlit and Snowflake Cortex AI.

### Repository Structure

---

| Day | Folder ID | Description | Features |
|-----|-----------|-------------|----------|
| Day 1 | E_DI78OMJ_6B_C_U | Connect to Snowflake | Basic Snowflake connection setup |
| Day 2 | H8S2FMNWC_WT8BKF | Hello, Cortex! | Cortex AI model interaction |
| Day 3 | I3B6H1A2Y6PRO6SI | Write Streams | Streaming text output with st.write_stream() |
| Day 4 | DU3ZZADCHB7853E1 | Caching Your App | App performance optimization with @st.cache_data |
| Day 5 | KNT4E1J6VY9GMVPW | LinkedIn Post Generator | Generate social media content using AI |
| Day 6 | G1LJFY3IQ2IQQVPM | Content Summarization | Summarize text content with Cortex Complete |
| Day 7 | DFQ70MYH9EQVDP1Z | Repost Generation | Create reposts from original content |
| Day 8 | YLK1V7VO2CX8A3MV | Multipage Chatbot | Multi-page Streamlit app with chat UI |
| Day 9 | NI_BJHCMI1GVAWBS | Custom Chatbot | Chat application with session state management |
| Day 10 | ZVV08FJGLA7QOF7G | Enhanced Chatbot | Advanced chatbot with model selection & TL;DR |
| Day 11 | M9U8S4CCJRFIY2E0 | Streaming Responses | Real-time streaming chatbot responses |

---
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

**Day 1: Connect to Snowflake**
- ✅ Basic Snowflake connection setup
- ✅ Authentication handling
- ✅ Session state initialization

**Day 2: Hello, Cortex!**
- ✅ Cortex AI model API integration
- ✅ LLM inference (Claude 3.5 Sonnet)
- ✅ Text generation capability

**Day 3: Write Streams**
- ✅ Streaming text output with st.write_stream()
- ✅ Real-time data display
- ✅ Text processing and output

**Day 4: Caching Your App**
- ✅ App performance optimization with @st.cache_data
- ✅ Duplicate API call elimination
- ✅ Improved user experience with faster responses

**Day 5: LinkedIn Post Generator**
- ✅ Generate social media content using AI
- ✅ Content customization for platforms
- ✅ Post formatting and display

**Day 6: Content Summarization**
- ✅ Summarize text content with Cortex Complete
- ✅ Content summarization alongside post generation
- ✅ Dynamic content processing

**Day 7: Repost Generation**
- ✅ Create reposts from original content
- ✅ Dark mode theming via config.toml
- ✅ Sidebar layout with Material Design icons
- ✅ Real-time progress feedback with st.status()

**Day 8: Multipage Chatbot**
- ✅ Multi-page Streamlit app structure
- ✅ Chat UI with st.chat_message() and st.chat_input()
- ✅ Message display and input handling

**Day 9: Custom Chatbot with Session State**
- ✅ Chat application with session state management
- ✅ Session State for persistent data
- ✅ Conversation history tracking

**Day 10: Enhanced Chatbot**
- ✅ Model selector dropdown (Claude 3.5 Sonnet / Mistral Large)
- ✅ Conversation mode selector (General Chat / Code Assistant / Data Analyst / Tech Mentor)
- ✅ Auto TL;DR summary at 10+ messages using session state counter
- ✅ Sidebar organization with clear history button
- ✅ Message counter display
- ✅ Status containers for response generation

**Day 11: Streaming Responses**
- ✅ Real-time streaming chatbot responses
- ✅ Word-by-word streaming effect
- ✅ Smooth, dynamic response display
- ✅ Live conversation updates


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
