import streamlit as st
import csv
from io import StringIO
from zipfile import ZipFile

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
    zipObj = ZipFile("dotfiles.zip", "w")

    for i in splitdata[1:]:
        #text_contents = i
        #st.download_button(f"{i.split()[0]}", text_contents, f"{i.split()[0]}.txt" )
        fname = f"{i.split()[0]}.txt"
        with open(fname, "w") as txtfile:
            zipObj.write(txtfile)

    zipObj.close()
    st.download_button("Download your Zipfile", zipObj, "dotfiles.zip")

st.write("Enjoy!")