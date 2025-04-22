import streamlit as st
from utils.feature_extractor import BookFeatureExtractor, load_book

st.set_page_config(page_title='Book Analysis', layout='wide')
st.title('📚 Book Feature Extraction')

uploaded = st.file_uploader('Upload a text or PDF file', type=['txt','pdf'])
if uploaded:
    # save to temp
    temp = f"/tmp/{uploaded.name}"
    with open(temp, 'wb') as f:
        f.write(uploaded.getbuffer())
    text = load_book(temp)

    with st.spinner('Analyzing...'):
        extractor = BookFeatureExtractor()
        profile = extractor.extract_book_profile(text)

    st.subheader('Overview')
    st.json(profile)