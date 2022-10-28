import streamlit as st
import csv
from io import StringIO
from zipfile import ZipFile
from io import BytesIO

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
    with BytesIO() as buffer:
    # Write the zip file to the buffer
        with ZipFile(buffer, "w") as zip:
            for i in splitdata[1:]:
                name = f"{i.split()[0]}.txt"
                zip.writestr(name, "file contents")

        btn = st.download_button(
        label="Download ZIP",
        data=buffer,  # Download buffer
        file_name="file.zip"
        )

st.write("Enjoy!")