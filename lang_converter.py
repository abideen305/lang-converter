import streamlit as st

st.title('Language Converter by Abideen')

@st.cache
def lang_conv():
    from textblob import TextBlob

    text = input("Enter a text to translate: ")
    blob = TextBlob(text)

    print(f'''

    Your text "{text}" in Arabic is : "{blob.translate(from_lang='auto', to='ar')}"
    Your text "{text}" in China is : "{blob.translate(from_lang='auto', to='zh')}"
    Your text "{text}" in French is : '{blob.translate(from_lang='auto', to='fr')}'
    Your text "{text}" in Hindi is : '{blob.translate(from_lang='auto', to='hi')}'

    ''')
    return blob.translate(from_lang='auto', to='ar')

    que = input('Do you need more info about the word you converted?').lower()

    if que == 'y' or que == 'yes':
        count_w = blob.word_counts
        print(f'''This is your word counts:

                    {count_w}  
                ''')
        corr = blob.correct()
        print(f'''

            {blob.words}

        Polarity: {blob.sentiment.polarity}

        Subjectivity: {blob.sentiment.subjectivity}

        {blob.sentences}


        ''')
        if corr != text:
            print('I found a spelling issue in your text and I corrected it')
            print(f'''This is the correct text

                    {corr}

                ''')
    else:
        print("Thank you")

lang_conv()
st.write('Welcome')

