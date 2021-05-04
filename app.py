import streamlit as st

from bbquote.quote import get_quote

quote, author = get_quote()  # assuming the function returns an author and a quote

"this is my quote:"

st.write(f"*{quote}* \n>{author}")
