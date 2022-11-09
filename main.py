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
    dct["\n"] = "{newline}"
    dct["\r"] = "{return}"
    dct["\t"] = "{tab}"
    for k, v in dct.items():
        if k in s:
            s = s.replace(k, v)
    return s


st.header("Batch Dot Phrase Wizard")

b = st.file_uploader("Upload a csv file")

if b is not None:
    # To convert to a string based IO:
    stringio = StringIO(b.getvalue().decode("utf-8"))

    # To read file as string:
    st.write("The contents of your csv file are displayed below:")
    string_data = stringio.read()
    st.write(string_data)
    splitdata = [i for i in string_data.split("&&&")[:-1] if len(i) > 0]
    dispdata = [i.split(",") for i in splitdata]
    st.table(dispdata)
    with BytesIO() as buffer:
        # Write the zip file to the buffer
        with ZipFile(buffer, "w") as zip:
            for i in splitdata[1:]:
                name = f"{legalizer(i).strip()}"
                try:
                    Ldesc, Ldotphrase, Lfulltxt, Lcat, Lauthor, discard = name.split(
                        ","
                    )
                    desc, dotphrase, fulltxt, cat, author, discard = i.split(",")
                    contents = f"{desc}\n{dotphrase}\n{fulltxt}\n{cat}\n{author}\n{20220415102629}"
                    dotFilename = f"Desc = {Ldesc}; Dotphrase = {Ldotphrase}; Fulltext = {Lfulltxt}; Cat = {Lcat}; Authr = {Lauthor}.bstr"
                    st.write(dotFilename)
                    zip.writestr(dotFilename, contents)
                except:
                    st.write(f"couldn't format {i}")
                    continue

        btn = st.download_button(
            label="Download ZIP", data=buffer, file_name="file.zip"  # Download buffer
        )


st.write("Enjoy!")
