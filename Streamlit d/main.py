import streamlit as st
import pandas as pd
import time as ts
from datetime import time

table= pd.DataFrame({"Column 1 ":[1,2,3,4,5,6,7],"Column 2 ":[11,12,13,14,15,16,17]})
def converter(value):
    m,s,mm=value.split(":")
    t_s=int(m)*60+int(s)+int(mm)/1000
    return t_s

st.markdown("---")
image =st.file_uploader("please upload an image",type="jpg")
if image is not None:
    st.image(image)
st.slider("gg")
val=st.text_input("enter your course",max_chars=10)
print(val)
val1=st.time_input("Set time ",value=time(0,0,0))
if str(val1) == "00:00:00":
    st.write("please set timer ")
else:
    sec=converter(str(val1))
    print(sec)
    bar=st.progress(0)
    per=sec/100
    progress_status=st.empty()
    for i in range(100):
      bar.progress(i+1)
      progress_status.write(str(i+1) + "%")
      ts.sleep(per)