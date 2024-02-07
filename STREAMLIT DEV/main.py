import streamlit as st
import pandas as pd

table= pd.DataFrame({"Column 1 ":[1,2,3,4,5,6,7],"Column 2 ":[11,12,13,14,15,16,17]})
st.markdown("""
            
            <style>
            .css-dibild.edgvbvh6
            (
            visibility:hidden;
            )
           ###########for css
            
            
            
            </style>""",unsafe_allow_html=True)
st.title("hi i am Streamlit web app ")
st.subheader("hi i am a subheader ")
st.header(' i am a header ')
st.text("hello this is like a paragraph tag")
st.markdown("**Hello use double stars for bold**<----- bold there and this is italic-----------> *use a single star instead of 2* ")
#multiple markdowns find online
st.markdown("---")
st.write("## H2")
st.metric(label="Wind speed",value="120ms⁻¹",delta="1.4ms⁻¹")
st.table(table)
st.dataframe(table)
st.image("image.jpg",caption="this is an image",width=1000)
st.audio("audio.mp3")
def change():
    print(st.session_state.checker)
state=st.checkbox("i am a checkbox",value=True,on_change=change)
if state:
    st.write("hello")
else:
    pass    
radio_btn=st.radio("where do you live?",options=("US","Portugal","Russia","UK"),on_change=change,key="checker")
print(radio_btn)
def btn_click():
    print("it was clicked")
btn=st.button("Click Me",on_click=btn_click)
select=st.selectbox("what is your favourite car?",options=("audi","BMW","Seat"))
print(select)
multi_select=st.multiselect("what is your favorite GPU",options=("nvidia","amd"))
