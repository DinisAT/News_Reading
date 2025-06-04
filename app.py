import streamlit as st
import pandas as pd


import trafilatura
from trafilatura import extract
from trafilatura.settings import use_config

st.title('Web Scraping App')

st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-5N0GKYX6YE"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-5N0GKYX6YE');

  // Test log to console to check script runs
  console.log("GA4 tag script loaded");
</script>
""", unsafe_allow_html=True)

st.write("If you open browser console (F12), you should see a GA4 tag log message here.")


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
