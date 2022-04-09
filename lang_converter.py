import streamlit as st

st.title('Language Converter by Abideen')
st.sidebar.write('Welcome to my page')
st.sidebar.button('click me')

from googletrans import Translator, constants
from pprint import pprint

text = st.text_input('Enter a text to translate: ')

# init the Google API translator
translator = Translator()

# translate a spanish text to english text (by default)
translation = translator.translate(text, dest='ar')
tr_ar = translation.text
translation = translator.translate(text, dest='fr')
tr_fr = translation.text
translation = translator.translate(text, dest='hi')
tr_hi = translation.text


st.write(f"Your text: {text} in arabic is: {tr_ar}")
st.write(f"Your text: {text} in  french is: {tr_fr}")
st.write(f"Your text: {text} in hindi is: {tr_hi}")

