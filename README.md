# 📰 NewsGenie – AI-Powered Information & News Assistant

### Smart News. Intelligent Answers. One Platform.

NewsGenie is an AI-powered news and information assistant developed using **Python, Streamlit, LangGraph, Google Gemini AI, and NewsAPI**. It combines intelligent conversations, categorized news discovery, and web search within a unified, user-friendly application.

## 🔗 Live Project Links

🌐 **Live Application:** [Launch NewsGenie AI Assistant](https://newsgenie-ai-news-assistant-2u7hpdm6faphbtqqjhf5k7.streamlit.app/)

💻 **GitHub Repository:** [View Source Code](https://github.com/2310030022-coder/NewsGenie-AI-News-Assistant)

## 📌 Project Overview

NewsGenie addresses the challenge of accessing relevant news and reliable information across multiple platforms.

The application integrates conversational AI with news retrieval and external web search to deliver an accessible information-discovery experience.

By combining LangGraph-based workflow orchestration, Gemini-powered responses, and news APIs, NewsGenie demonstrates how generative AI can be incorporated into a practical web application.

## 🚀 Key Features

- **AI-Powered Chatbot:** Generates conversational answers to general user queries using Google Gemini.
- **News Discovery:** Retrieves news articles through NewsAPI.
- **Multiple Categories:** Provides technology, finance, and sports news.
- **Intelligent Query Routing:** Uses LangGraph to distinguish general questions from news-related requests.
- **Web Search Integration:** Uses DuckDuckGo to retrieve supplementary information.
- **News Fallback:** Supports Google News RSS when the primary news service is unavailable.
- **Conversation History:** Maintains chat context using Streamlit session state.
- **Source References:** Displays links to original news articles.
- **Error Handling:** Manages missing API keys, unsuccessful API calls, and unavailable results.
- **Interactive Interface:** Provides a responsive web application built with Streamlit.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive frontend |
| Google Gemini AI | AI-powered conversational responses |
| LangGraph | Query routing and workflow orchestration |
| NewsAPI | News retrieval |
| Google News RSS | Alternative news source |
| DuckDuckGo Search | External information retrieval |
| GitHub | Version control and project hosting |
| Streamlit Community Cloud | Web application deployment |

## ⚙️ System Architecture

**User → Streamlit Interface → LangGraph Workflow → Query Classification**

The workflow directs requests to the appropriate component:

1. **General Questions:** Gemini AI processes user queries.
2. **News Requests:** NewsAPI retrieves relevant articles.
3. **API Fallback:** Google News RSS provides an alternative news source.
4. **External Information:** DuckDuckGo search supplements information retrieval.
5. **Response Display:** Streamlit presents results and maintains conversation history.

## 📂 Project Structure

```text
NewsGenie-AI-News-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
└── secrets.example.toml
```

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/2310030022-coder/NewsGenie-AI-News-Assistant.git
cd NewsGenie-AI-News-Assistant
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

Create a `.streamlit/secrets.toml` file containing:

```toml
GEMINI_API_KEY = "your_gemini_api_key"
NEWS_API_KEY = "your_newsapi_key"
```

Keep actual API credentials private and never commit them to GitHub.

### 4. Run the Application

```bash
stream
