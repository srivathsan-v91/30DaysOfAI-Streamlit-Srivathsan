# 30 Days of AI - Streamlit Learning Challenge

## By: Srivathsan V
## Company: EY | Role: Senior Cloud Data Engineer

My personal journey through the #30DaysOfAI challenge with Streamlit and Snowflake Cortex AI.

### Repository Structure

```
./
├── day_01_connect_snowflake.py    # Day 1: Connect to Snowflake
├── day_02_fetch_data.py            # Day 2: Fetch & Display Data
├── day_03_dataframe_interaction.py # Day 3: DataFrame Interaction
├── day_04_plot_chart.py            # Day 4: Plotting Charts
├── day_05_linkedin_generator.py    # Day 5: LinkedIn Post Generator (Core)
├── day_06_linkedin_summarizer.py   # Day 6: Content Summarization
├── day_07_theming_layout.py        # Day 7: Dark Mode Theming
├── day_08_chat_elements.py         # Day 8: Chat UI Foundation
├── day_09_session_state.py         # Day 9: Understanding Session State
├── day_10_chatbot_enhanced.py      # Day 10: Full Chatbot (Enhanced)
└── README.md                        # This file
```

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
