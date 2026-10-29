# NewsGenie – AI-Powered Information & News Assistant

A Streamlit chatbot that routes general questions and news requests with LangGraph, retrieves articles using NewsAPI (Google News RSS fallback), searches web results using DDGS, and summarizes with Gemini (when configured).

## Features
- Chat with session conversation history
- Automatic query differentiation (simple keyword heuristic, not an ML-trained classifier)
- Tech / finance / sports categories
- NewsAPI with RSS fallback and linked sources
- Search-assisted Gemini responses
- Missing-key, empty-results and service-error handling

## Quickstart
1. Install Python 3.11 or 3.12.
2. Run `pip install -r requirements.txt`.
3. Create `.streamlit/secrets.toml` using `secrets.example.toml` as a template.
4. Get keys from https://aistudio.google.com/apikey and https://newsapi.org/register.
5. Run `streamlit run app.py`.

## Deploy
1. Upload `app.py`, `requirements.txt`, `README.md`, `.gitignore`, and `secrets.example.toml` to a GitHub repository.
2. Visit https://share.streamlit.io and deploy the repository with main file `app.py`.
3. Under Advanced settings → Secrets, paste your actual TOML key assignments. Never upload your real `secrets.toml` or API keys to GitHub.
4. Test the deployed app. NewsAPI's free Developer tier is intended for development/testing and may restrict production deployment; the app attempts a Google News RSS fallback.

## Limitations
- Automated misinformation detection is not implemented. The app provides publisher links and a cautious summarization prompt, but it **cannot guarantee accuracy**.
- NewsAPI Developer responses may be delayed by 24 hours; RSS freshness varies. Do not present results as guaranteed instantaneous.
- Heuristic classification can misroute requests; refine using intent classification for production.
- DDGS and RSS endpoints may rate-limit or fail. Some publishers may block access.
- No persistent database: conversation history is scoped to the Streamlit session.
- API integrations require connectivity, valid keys where applicable, and external service availability.

## Architecture
`Query → LangGraph classify → news/general → NewsAPI/RSS or DDGS → optional Gemini → Streamlit display + source links`

## Demo prompts
- Latest technology news about AI
- Today's sports headlines
- Latest finance news on inflation
- Explain what machine learning is
- What are the applications of generative AI?
