import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Custom CSS for animated background
st.markdown("""
    <style>
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fad0c4, #fcb69f);
        background-size: 300% 300%;
        animation: gradientBG 15s ease infinite;
    }

    .header {
        text-align: center;
        color: #ffffff;
        font-family: Arial, sans-serif;
        font-size: 36px;
        margin-bottom: 20px;
    }

    .subheader {
        color: #ffffff;
        font-family: Arial, sans-serif;
        font-size: 18px;
        margin-bottom: 15px;
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        color: #ffffff;
    }

    .result-box {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
        color: #000;
    }
    </style>
    """, unsafe_allow_html=True)

# Application Title
st.markdown('<h1 class="header">🌍 Language Translator</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subheader">Translate words or sentences easily in multiple languages</h3>', unsafe_allow_html=True)

# Split layout into two columns
col1, col2 = st.columns(2)

with col1:
    # User input for word/sentence
    word = st.text_input("Enter a word or sentence to translate:")

with col2:
    # Language search input
    search = st.text_input("Search for a language:")

    # Filter the languages based on the search term
    language_options = [language for language in LANGUAGES.values() if search.lower() in language.lower()]

    if not language_options:
        st.write("No languages match your search.")
    else:
        # Selectbox to choose the target language
        target_language = st.selectbox("Select the target language:", language_options)

# Translate button and display results
if word:
    # Detect the input language
    detected_language = translator.detect(word).lang
    detected_language_name = LANGUAGES[detected_language].capitalize()

    st.markdown(f"Detected Language: {detected_language_name}")

    # Add a button to trigger the translation
    if st.button("Translate"):
        # Get the code of the selected language
        target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]
        translated = translator.translate(word, dest=target_language_code)

        # Display detected language and translated text
        st.markdown(f'<div class="result-box">Input Language: {detected_language_name}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">Translated Text in {target_language}:{translated.text}</div>', unsafe_allow_html=True)
