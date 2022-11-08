import streamlit as st
import csv
from io import StringIO
from zipfile import ZipFile
from io import BytesIO


def legalizer(s: str) -> str:
    dct = {}
    dct["<"] = "{less}"
    dct[">"] = "{greater}"
    dct[":"] = "{colon}"
    dct['""'] = "{quote}"
    dct["/"] = "{fslash}"
    dct["\\"] = "{bslash}"
    dct["|"] = "{pipe}"
    dct["?"] = "{qstmrk}"
    dct["*"] = "{star}"
    dct[";"] = "{semi}"
    for i in s:
        try:
            dct[i]
            s = s.replace(i, dct[i])
        except:
            continue
    return s


st.header("Batch Dot Phrase Wizard")

b = st.file_uploader("Upload a csv file")

if b is not None:
    bytes_data = b.getvalue()
    # To convert to a string based IO:
    stringio = StringIO(b.getvalue().decode("utf-8"))

    # To read file as string:
    st.write("The contents of your csv file are displayed below:")
    string_data = stringio.read()
    splitdata = string_data.split("\n")
    for data in splitdata:
        st.write(legalizer(data))
    with BytesIO() as buffer:
        # Write the zip file to the buffer
        with ZipFile(buffer, "w") as zip:
            for i in splitdata[1:]:
                name = f"{legalizer(i)}.tx"
                zip.writestr(name, "file contents")

        btn = st.download_button(
            label="Download ZIP", data=buffer, file_name="file.zip"  # Download buffer
        )

st.write("Enjoy!")
