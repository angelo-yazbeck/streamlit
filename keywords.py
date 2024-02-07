import streamlit as st
from bs4 import BeautifulSoup
import requests

st.markdown("<h1 style='text-align:center;'>Audio to text </h1>" ,unsafe_allow_html=True)
st.markdown("---")
url=st.text_input("Youtube url here")
if url:
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'lxml')
    meta_tag=soup.select("meta[name='keywords']")
    tit=soup.find("title")
    keywords=meta_tag[0]["content"]
    st.title("Title")
    st.markdown(f"<h4 stle='color:#101520FF'>{tit.text}</h4>",unsafe_allow_html=True)
    st.title("tags")
    st.markdown(f"<h5 stle='color:#101520FF'>{keywords}</h5>",unsafe_allow_html=True)