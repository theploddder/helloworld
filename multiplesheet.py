import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import openpyxl


downloads_path = str(Path.home() / "Downloads")
unlocked = False

@st.cache(allow_output_mutation=True)
def persistdata():
    return {}

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

@st.cache_data
def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

@st.cache_data
def _sum(arr):
    sum = 0

    for i in arr:
        sum = sum + i
 
    return(sum)

@st.cache_data
def returnTotalRegUnit(credit_units1, edited_df):
    dd_ar = []
    ttp = []

    for yy in range(len(edited_df)):
        ndf = edited_df.iloc[yy]
        cc = 0
        my_ntar = ndf.values
        dd = 0

        for i in my_ntar:
            try:
                if i == 'ABS':
                    dd + 0
                else:
                    dd += credit_units1[cc]
            except:
                pass
            cc += 1
        
        ttp.append(dd)
        dd = 0

    return ttp

@st.cache_data
def returnTotalPassed(credit_units1, edited_df):
    t_p_p = []

    for xx in range(len(edited_df)):
        jtt = _sum(credit_units1)
        ndfa = edited_df.iloc[xx]
        anpr = ndfa.values
        count = 0
        for i in anpr:
            try:
                if(int(i) >= 0 and int(i) <= 39):
                    jtt -= credit_units1[count]
            except:
                jtt -= credit_units1[count]
            count += 1

        t_p_p.append(jtt)
        jtt = 0

    return t_p_p

@st.cache_data
def returnTotalFailed(credit_units1, edited_df):
    t_u_f = []
    for yy in range(len(edited_df)):
        sss = 0
        ndfa1 = edited_df.iloc[yy]
        anpr1 = ndfa1.values
        count = 0
        for j in anpr1:
            try:
                if(int(j) <= 39):
                    sss += credit_units1[count]
            except:
                pass
            count += 1

        t_u_f.append(sss)
        sss = 0

    return t_u_f


@st.cache_data
def returnOutstandingCourses(credit_units1, edited_df):
    cols = edited_df.columns
    t_p_i_t = []

    for yy in range(len(edited_df)):
        sss = ""
        ndfa1 = edited_df.iloc[yy]
        anpr1 = ndfa1.values
        count = 0
        for idx, j in enumerate(anpr1):
            try:
                if(int(j) <= 39):
                    sss += cols[idx] + ','
            except:
                sss += cols[idx] + ','
            count += 1

        t_p_i_t.append(sss)
    return t_p_i_t


@st.cache_data
def returnTotalPoints(credit_units1, edited_df):
    t_p_i_t = []

    for yy in range(len(edited_df)):
        ndf = edited_df.iloc[yy]
        cc = 0
        my_ntar = ndf.values
        dd = 0

        for i in my_ntar:
            try:
                if(int(i) <= 100 and int(i) >= 70):
                    dd += credit_units1[cc] * 5
                elif(int(i) <= 69 and int(i) >= 60):
                    dd += credit_units1[cc] * 4
                elif(int(i) <= 59 and int(i) >= 50):
                    dd += credit_units1[cc] * 3
                elif(int(i) <= 49 and int(i) >= 45):
                    dd += credit_units1[cc] * 2
                elif(int(i) <= 44 and int(i) >= 40):
                    dd += credit_units1[cc] * 1
                elif(int(i) <= 39 and int(i) >= 0):
                    dd += credit_units1[cc] * 0
            except:
                dd += credit_units1[cc] * 0
            cc += 1

        
        t_p_i_t.append(dd)
        dd = 0
    return t_p_i_t





st.title('MULTIPLE SHEET CALCULATOR')
    

if(st.button('View Sample Dataset Image')):
    st.info('Number Of Columns Dosen\'t Matter')
    st.image('sampledata.PNG')
try:
    uploaded_file = st.file_uploader("Upload Dataset", type=['xlsx'])
except:
    pass

dataframe_collection = persistdata()


if uploaded_file is not None:

    all_excel_data = pd.ExcelWriter('a1.xlsx', engine='xlsxwriter')
    
    widget_id = (id for id in range(1, 100_00))

    wb = openpyxl.load_workbook(uploaded_file) 
    sheet_names = wb.sheetnames


    # select_sheet = st.selectbox('Select Sheet:',sheet_names)
    # df = pd.read_excel(uploaded_file, sheet_name=select_sheet)

    tdf = pd.DataFrame()
    
        
    sht_nms = st.selectbox('Select Sheet', sheet_names)

    writer = pd.ExcelWriter('multiple.xlsx', engine='xlsxwriter')

    df = pd.read_excel(uploaded_file, sheet_name=sht_nms)

    columns = st.multiselect("Columns_Excel:",df.columns, key=next(widget_id))

    df1 = pd.DataFrame()
    for i in columns:
        df1[i] = df[i]

    edited_df = st.experimental_data_editor(df1, key=next(widget_id))
    
    ccr = st.text_input('Input All Credit Accordingly Seperated By A Comma', key=next(widget_id))

    
    if(st.button('PROCEED', key=next(widget_id))):

        cred_uni = ccr.split(',')
        cred_uni = [ int(x) for x in cred_uni]



        rtf = returnTotalFailed(cred_uni, edited_df)
        rtp = returnTotalPassed(cred_uni, edited_df)
        rtr = returnTotalRegUnit(cred_uni, edited_df)
        rotc = returnOutstandingCourses(cred_uni, edited_df)
        rtsp = returnTotalPoints(cred_uni, edited_df)

        df['Total Points Registered'] = rtr
        df['Total Points Passed'] = rtp
        df['Total Points Failed'] = rtf
        df['Outstanding Courses'] = rotc
        df['Total Points Scored'] = rtsp

        gp = []
        for i in range(len(df['Total Points Passed'])):
            tgp = df['Total Points Scored'][i] / df['Total Points Registered'][i]
            tgp = round(tgp, 3)
            gp.append(tgp)


        df['GPA'] = gp

        for i in edited_df.columns:
            df[i] = edited_df[i]

        # st.dataframe(df)

        dic1 = {sht_nms : df}
        dataframe_collection.update(dic1)
        
    
    st.write('Solved Sheets --> ' + str(dataframe_collection.keys()))
        
    
    if(st.button('Download With Current Sheets', key=next(widget_id))):
        for key in dataframe_collection.keys():
            dataframe_collection[key].to_excel(all_excel_data, index=False, sheet_name=key)

        all_excel_data.save()

        with open('a1.xlsx', "rb") as template_file:
            template_byte = template_file.read()

            st.download_button(label="Click To Download",
                                data=template_byte,
                                file_name="template.xlsx",
                                mime='application/octet-stream')
    if(st.button('Clear Cache', key=next(widget_id))):
        dataframe_collection.clear()