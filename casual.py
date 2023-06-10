import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

downloads_path = str(Path.home() / "Downloads")
unlocked = False

@st.cache(allow_output_mutation=True)
def persistdata():
    return {}

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')



def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]


st.title('CASUAL CALCULATOR')
tcu = None

credit_units = st.text_input('All Credit Accordingly Seperated By A Comma')
grades = st.text_input('All Grades Accordingly Seperated By A Comma')

if(st.button('Calculate')):
    st.info('Please Wait.....')

    cu = credit_units.split(',')
    sum = 0
    for i in cu:
        sum = sum + int(i)
        tcu = i
    
    st.text('Total Credit Unit --> ' + str(sum))

    grds = grades.split(',')
    grades_dict = {}

    total_a = []
    total_b = []
    total_c = []
    total_d = []
    total_e = []
    total_f = []

    for i in grds:
        if int(i) >= 70 and int(i) <= 100:
            total_a.append(i)
        elif int(i) >= 60 and int(i) <= 69:
            total_b.append(i)
        elif int(i) >= 50 and int(i) <= 59:
            total_c.append(i)
        elif int(i) >= 45 and int(i) <= 49:
            total_d.append(i)
        elif int(i) >= 40 and int(i) <= 44:
            total_e.append(i)
        elif int(i) >= 0 and int(i) <= 39:
            total_f.append(i)

    grades_dict.update({
        "A" : total_a,
        "B" : total_b,
        "C" : total_c,
        "D" : total_d,
        "E" : total_e,
        "F" : total_f
    })

    tps = 0

    aas = grades_dict.get('A')
    bbs = grades_dict.get('B')
    ccs = grades_dict.get('C')
    dds = grades_dict.get('D')
    ees = grades_dict.get('E')
    ffs = grades_dict.get('F')
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    for i, value in enumerate(cu):
        if grds[int(i)] in (aas):
            a += int(value) * 5
        elif grds[int(i)] in bbs:
            b += int(value) * 4
        elif grds[int(i)] in ccs:
            c += int(value) * 3
        elif grds[int(i)] in dds:
            d += int(value) * 2
        elif grds[int(i)] in ees:
            e += int(value) * 1
        elif grds[int(i)] in ffs:
            f += int(value) * 0

    tps = a + b + c + d + e + f
    
    gpa = tps / sum

    st.text('Total Points Scored --> ' + str(tps))

    st.text('G.P --> ' + str(gpa))
