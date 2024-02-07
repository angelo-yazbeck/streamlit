import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
figure=plt.figure()
def date_converter(date_col):
    result=list()
    values=date_col.values
    for val in values:
        result.append(str(val).split("T")[0])
    return result



st.markdown("<h1 style='text-align:center;'>Data Visualizer </h1>" ,unsafe_allow_html=True)
st.markdown("---")
files_names=list()
files=st.file_uploader("Upload Multiple Files",type=["xlsx"],accept_multiple_files=True)
if files:
    for file in files:
        files_names.append(file.name)
    selected_files=st.multiselect("Select Files",options=files_names)
    if selected_files:
        option=st.radio("Select Entity Against Date",options=["none","Id","Date","Gpu","Cpu","Mouse","Keyboard","Casing"])
        if option !="none":
            for file in files:
                if file.name in selected_files:
                    shop_data=pd.read_excel(file, index_col=0)
                    item=list(shop_data[option])
                    dates=date_converter(shop_data["Date"])
                    index=np.arange(len(dates))
                    plt.xticks(index, dates)
                    plt.gcf().autofmt_xdate()
                    plt.plot(index, item,label=file.name,marker='o')
                    plt.xlabel("Date")
                    plt.ylabel(option)
                    plt.title(option+"Chart")
                    plt.grid(True)
                    plt.legend()
                    print(dates)
            st.write(figure)