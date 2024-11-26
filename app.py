import streamlit as st
import pandas as pd
import trafilatura
from trafilatura import extract
from trafilatura.settings import use_config

st.title('Web Scraping App')

def scraping(url: str):
    # Solution for signal / thread error
    config = use_config()
    config.set("DEFAULT", "EXTRACTION_TIMEOUT", "0")
    down = trafilatura.fetch_url(url)
    scraped_df = pd.DataFrame({'news': [extract(down, config=config)]})
    return scraped_df

# Create text input for URL
url = st.text_input('Enter URL to read:', )

if st.button('Read'):
    # Show loading message
    with st.spinner('Scraping content...'):
        # Get scraped content
        result = scraping(str(url))
        # Display result
        st.write('News Content:')
        st.write(result['news'][0])
