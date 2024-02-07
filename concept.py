import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie


with st.sidebar:
    selected=option_menu(
        menu_title="main menu",
        options=["home","proj","contact"],
    )
if selected =="home":
        st.title("welcome home")
com.iframe("https://lottie.host/embed/155643f7-4a5e-4da8-b336-0d20eb8b8c44/WFTa1dMIJY.json")






















#st.cache_data
#def printer():
 #   time.sleep(3)
  #  return"Message"
#st.write(printer())

























#text = "🐶"

#if "click" not in st.session_state:
 #   st.session_state.click = False
#else:
 #   if st.session_state.click == False:
  #      text = "🐱"
   #     st.session_state.click = True
    #else:
     #   text = "🐶"
      #  st.session_state.click = False

#st.button(text)










#def printer(name):
 #   print(name)
#input=st.text_input("Enter Your Name:")
#s_btn=st.button("submit")
#if s_btn:
 #   opt=st.checkbox("Want to display your name?",on_change=printer, args=(input,))
