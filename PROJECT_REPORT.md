# Course End Project Report
## NewsGenie – An AI-Powered Information and News Assistant

### 1. Overview
NewsGenie is a Streamlit application that combines a conversational assistant with source-linked news retrieval. It supports technology, finance, and sports and sends user requests through a LangGraph workflow to either a news retrieval path or a general-question path.

### 2. Problem Statement
Users struggle to discover relevant and timely reports, evaluate publisher credibility, and ask general questions without switching platforms. The goal is one simple interface that helps users retrieve articles and receive concise information with transparent limitations.

### 3. Objectives
- Distinguish general questions from news-oriented queries.
- Show categorized news from external services.
- Include web search to augment general answers.
- Preserve chat context for the current session.
- Handle missing keys, API failures, and empty responses.

### 4. Tools
- **Streamlit**: interface and session state.
- **LangGraph**: explicit routing and processing nodes.
- **NewsAPI**: categorized headlines and article search.
- **Google News RSS**: fallback when NewsAPI returns errors or no articles.
- **DDGS**: external web search for general questions.
- **Gemini API**: optional text generation and summarization.
- **Python requests/feedparser**: HTTP and RSS parsing.

### 5. Chatbot Design and Query Differentiation
Input first enters a classification node. It checks for news-related expressions such as *latest*, *news*, *today*, and *headline*. If any match, the query is routed to news handling. Otherwise it is sent to general handling. The method is a baseline heuristic and is not an independently trained classifier. Both paths return an answer, source links, and optional notice.

Recent user-assistant messages (up to eight prior turns) are provided to Gemini to preserve limited conversational context. Streamlit session state stores the chat until cleared or session expiry.

### 6. Real-Time News Integration and Sample Output Format
The sidebar lets the user choose Technology, Finance, or Sports. NewsAPI's `top-headlines` endpoint is used for broad category requests; the `everything` endpoint is used when the user specifies a topic. If NewsAPI fails, the app requests a category or keyword feed from Google News RSS.

**Example display templates (illustrative, not verified live headlines):**

- Technology: `[Article headline] — [Publisher] — [Publication time] — [Read article]`
- Finance: `[Article headline] — [Publisher] — [Publication time] — [Read article]`
- Sports: `[Article headline] — [Publisher] — [Publication time] — [Read article]`

After running the app, capture genuine headline screenshots for each category and insert those in the final LMS submission. Do not label these templates as real API output.

### 7. LangGraph Workflow
`User input → classify → news OR general → output`

**News path:** retrieve headlines; fall back to RSS if necessary; send source metadata to Gemini for a careful summary; show publisher links.  
**General path:** retrieve web-search snippets; send them to Gemini with the recent chat history; display answer and relevant source links.

### 8. Error Handling and Fallback Mechanisms
- Missing `NEWS_API_KEY`: Google News RSS fallback.
- NewsAPI HTTP error or zero articles: Google News RSS fallback.
- RSS failure: show a clear no-articles message.
- Missing `GEMINI_API_KEY`: retain source browsing; inform user that AI answering requires a key.
- Gemini HTTP failure: show a temporary-unavailability message, or news source listing if news was retrieved.
- Web-search error: continue with Gemini but warn that web search is unavailable.
- Network calls use timeouts to avoid indefinite waiting.

### 9. Reliability and Misinformation Limitations
NewsGenie links to original publishers and tells the AI not to fabricate sources. These measures support transparency but **do not certify factual accuracy, detect misinformation reliably, or independently cross-check claims**. Production validation would require corroboration across independent authoritative sources, publisher evaluation, and formal quality testing. NewsAPI's free development tier has a 24-hour article delay and restrictions; the app must not claim guaranteed real-time publication coverage.

### 10. UI and Deployment
The UI contains a chatbot tab, a browse-headlines tab, category selection, and a clear-conversation action. Deployment targets Streamlit Community Cloud. Credentials are stored outside GitHub using Streamlit secrets.

### 11. Testing Checklist (to execute)
- [ ] Launch app with installed dependencies.
- [ ] Ask a general question and verify routed response.
- [ ] Ask for latest technology news.
- [ ] Fetch finance headlines in Browse tab.
- [ ] Fetch sports headlines in Browse tab.
- [ ] Remove NewsAPI key and verify RSS fallback.
- [ ] Remove Gemini key and verify key-missing message.
- [ ] Clear conversation and verify previous messages disappear.
- [ ] Test deployed URL and take actual screenshots.

### 12. Conclusion
NewsGenie demonstrates the composition of UI, external content retrieval, web search, a conversational language model, and LangGraph workflow routing. External API availability and factual verification remain essential limitations; the architecture provides understandable user-facing fallback behavior.
