    st.caption('YOUR AI NEWSROOM')
    st.divider()
    st.markdown('### 🎛️ Preferences')
    category = st.selectbox('Choose your category', list(CATEGORY_QUERIES), label_visibility='visible')
    st.markdown('**Explore:** Technology · Finance · Sports')
    if st.button('🧹 Clear chat history', use_container_width=True):
        st.session_state.history = []
        st.session_state.chat = []
        st.rerun()
    st.divider()
    st.markdown('**🔒 Responsible news browsing**')
    st.caption('Articles come from external publishers. Open original links to confirm important claims. NewsAPI developer tiers may have delays or hosting restrictions; RSS fallback is available.')
    st.caption('Built with Streamlit · LangGraph · Gemini')

st.markdown('''<div class="hero"><div class="eyebrow">INTELLIGENT NEWS DISCOVERY PLATFORM</div>
<h1>📰 NewsGenie <span style="color:#83e6ff">AI</span></h1>
<p>Stay informed without the noise. Explore the latest available headlines, discover trusted sources, and ask your AI assistant questions—all in one modern newsroom.</p>
<span class="pill">✨ AI-powered answers</span><span class="pill">🌍 Source-linked headlines</span>
<span class="pill">🔀 LangGraph workflows</span><span class="pill">🛡️ RSS fallback</span></div>''', unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)
with m1: st.metric('🗂️ News categories', '3', 'Technology · Finance · Sports')
with m2: st.metric('📰 Articles in current feed', str(len(st.session_state.feed)), 'Refresh to update')
with m3: st.metric('💬 Conversation messages', str(len(st.session_state.chat)), 'Current session')

tab_news, tab_chat, tab_about = st.tabs(['🌎 News Explorer', '🤖 AI News Assistant', 'ℹ️ About NewsGenie'])
with tab_news:
    st.markdown('<div class="section-label">DISCOVER THE STORIES THAT MATTER</div>', unsafe_allow_html=True)
    st.subheader('Explore the headlines')
    a, b, c = st.columns([1.2, 2.4, 1])
    with a:
        feed_category = st.selectbox('News desk', list(CATEGORY_QUERIES), index=list(CATEGORY_QUERIES).index(st.session_state.feed_category))
    with b:
        keyword = st.text_input('Search for a topic', placeholder='e.g. generative AI, stock market, cricket', key='news_keyword')
    with c:
        st.write('')
        st.write('')
        load = st.button('🔄 Load news', type='primary', use_container_width=True)
    if load:
        with st.spinner('Collecting the latest available articles...'):
            articles, provider, notice = get_news(feed_category, keyword.strip())
        st.session_state.feed = articles
        st.session_state.feed_info = (provider, notice)
        st.session_state.feed_category = feed_category
    if st.session_state.feed:
        provider, notice = st.session_state.feed_info
        st.info(f'News source: {provider}. {notice}' if notice else f'News source: {provider}. Showing the latest articles available from this provider.')
        st.caption('News results may be delayed by provider plan or publication availability. Source content is not independently fact-checked by NewsGenie.')
        news = st.session_state.feed
        for index in range(0, len(news), 3):
            columns = st.columns(3, gap='medium')
            for col, article in zip(columns, news[index:index+3]):
                with col:
                    st.markdown(news_card(article, st.session_state.feed_category), unsafe_allow_html=True)
    else:
        st.info('👆 Select a category and click **Load news** to explore up to 18 articles, with publisher details and original source links.')
    st.divider()
    st.markdown('#### 🔎 Trending topics to explore')
    st.caption('Try: artificial intelligence · startups · cybersecurity · inflation · global markets · football · cricket')

with tab_chat:
    st.markdown('<div class="section-label">YOUR PERSONAL AI RESEARCH ASSISTANT</div>', unsafe_allow_html=True)
    st.subheader('Ask NewsGenie anything')
    st.caption('Ask a general question or request news. LangGraph routes requests to news retrieval or AI-assisted web information.')
    for msg in st.session_state.chat:
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])
            if msg.get('notice'):
                st.caption(msg['notice'])
            for source in msg.get('sources', [])[:6]:
                url = safe_url(source.get('url', ''))
                if url:
                    st.markdown(f"- [{source['title']}]({url})")
    question = st.chat_input('Ask a question or request recent headlines...')
    if question:
        with st.chat_message('user'):
            st.markdown(question)
        with st.chat_message('assistant'):
            with st.spinner('NewsGenie is researching your question...'):
                result = workflow.invoke({'question': question, 'category': category, 'history': st.session_state.history})
            st.markdown(result.get('answer', 'No response available.'))
            if result.get('notice'):
                st.caption(result['notice'])
            for item in result.get('sources', [])[:6]:
                url = safe_url(item.get('url', ''))
                if url:
                    st.markdown(f"- [{item['title']}]({url})")
        st.session_state.chat += [
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': result.get('answer', ''),
             'sources': result.get('sources', []), 'notice': result.get('notice', '')}]
        st.session_state.history += [
            {'role': 'user', 'content': question},
            {'role': 'assistant', 'content': result.get('answer', '')}]

with tab_about:
    st.subheader('A smarter way to follow the world')
    st.write('NewsGenie brings news discovery, external web search, and AI-assisted conversation into one Streamlit application. Its LangGraph workflow differentiates news questions from general requests, with source-linked articles and graceful fallback handling.')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('**🧠 AI & orchestration**')
        st.write('Google Gemini · LangGraph · Streamlit session state')
    with col2:
        st.markdown('**🌐 Information sources**')
        st.write('NewsAPI · Google News RSS fallback · DuckDuckGo search')
    st.link_button('💻 View GitHub source code', 'https://github.com/2310030022-coder/NewsGenie-AI-News-Assistant')

st.divider()
st.caption(f'© NewsGenie AI · Updated {datetime.now(timezone.utc):%d %b %Y} (UTC) · For information discovery, not guaranteed real-time or independently verified reporting.')
