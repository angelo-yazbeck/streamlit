
import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser
import time 
st.set_page_config("Web Scrapper",page_icon="💯",layout="wide")
st.markdown("<h1 'text-align: center;'>Web Scraper </h1>" ,unsafe_allow_html=True)

with st.form("Search"):
    keyword=st.text_input("Enter Your Keyword")
    search=st.form_submit_button("Search")
placeholder=st.empty()
if keyword:
    page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup=BeautifulSoup(page.content)
    rows=soup.find_all("div", class_="ripi6" )
    col1,col2=placeholder.columns(2)
    for index,row in enumerate(rows):
        figures=row.find_all("figure")
        for i in range(2):
            img=figures[i].find("img",class_="tB6UZ a5VGX")
            list=img["srcset"].split("?")
            anchor=figures[i].find("a",class_="rEAWd")
            print(anchor["href"])
            if i==0:
                col1.image(list[0])
                btn=col1.button("Download",key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])

        else:
            col2.image(list[0]) 
            btn=col2.button("Download",key=str(index)+str(i))
            if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])


#st.image("https://images.unsplash.com/photo-1518531933037-91b2f5f229cc")