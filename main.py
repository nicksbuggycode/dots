import streamlit as st
import csv
from io import StringIO

st.header("Batch Dot Phrase Wizard")

b = st.file_uploader("Upload a csv file")

if b is not None:
    bytes_data = b.getvalue()
   # To convert to a string based IO:
    stringio = StringIO(b.getvalue().decode("utf-8"))

    #To read file as string:
    st.write("The contents of your csv file are displayed below:")
    string_data = stringio.read()
    splitdata = string_data.split()
    st.write(splitdata)

    for i in splitdata[1:]:
        text_contents = i
        st.download_button(f"{i.split()[0]}", text_contents)

st.write("Enjoy!")