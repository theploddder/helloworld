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
def returnOutstandingCoursesSummary(sheet_names, uploaded_file):
    out_cors = []
    for sn in range(len(sheet_names)-2):
        df = pd.read_excel(uploaded_file, sheet_name=sheet_names[sn])

        eac_out_cors = []
        for i in df['Outstanding Courses']:    
            eac_out_cors.append(i)
       
        out_cors.append(eac_out_cors)

    df1 = pd.DataFrame()

    for idx, value in enumerate(out_cors):
        df1[str(idx)] = value

    t_df = df1[df1.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)

    return t_df

@st.cache_data
def returnCoursesFailedSummary(sheet_names, uploaded_file):
    out_cors = []
    for sn in sheet_names[-2:]:
        df = pd.read_excel(uploaded_file, sheet_name=sn)

        eac_out_cors = []
        for i in df['Outstanding Courses']:    
            eac_out_cors.append(i)
       
        out_cors.append(eac_out_cors)

    df1 = pd.DataFrame()

    for idx, value in enumerate(out_cors):
        df1[str(idx)] = value

    t_df = df1[df1.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)

    return t_df

@st.cache_data
def returnTotalUnitsTakenSummary(sheet_names, uploaded_file):
    out_cors = []
    for sn in sheet_names[-2:]:
        df = pd.read_excel(uploaded_file, sheet_name=sn)

        eac_out_cors = []
        for i in df['Total Points Registered']:    
            eac_out_cors.append(i)
       
        out_cors.append(eac_out_cors)

    df1 = pd.DataFrame()

    for idx, value in enumerate(out_cors):
        df1[str(idx)] = value

    df1 = df1.astype('int64')
    t_df = df1.sum(axis=1, numeric_only= True)

    return t_df

@st.cache_data
def returnTotalUnitsPassedSummary(sheet_names, uploaded_file):
    out_cors = []
    for sn in sheet_names[-2:]:
        df = pd.read_excel(uploaded_file, sheet_name=sn)

        eac_out_cors = []
        for i in df['Total Points Passed']:    
            eac_out_cors.append(i)
       
        out_cors.append(eac_out_cors)

    df1 = pd.DataFrame()

    for idx, value in enumerate(out_cors):
        df1[str(idx)] = value

    df1 = df1.astype('int64')
    t_df = df1.sum(axis=1, numeric_only= True)

    return t_df

@st.cache_data
def returnSessionalGPASummary(sheet_names, uploaded_file):
    out_cors = []
    for sn in sheet_names[-2:]:
        df = pd.read_excel(uploaded_file, sheet_name=sn)

        eac_out_cors = []
        for i in df['Total Points Scored']:    
            eac_out_cors.append(i)
       
        out_cors.append(eac_out_cors)

    df1 = pd.DataFrame()

    for idx, value in enumerate(out_cors):
        df1[str(idx)] = value

    df1 = df1.astype('int64')
    t_df = df1.sum(axis=1, numeric_only= True)

    t_df = round(t_df, 3)
        

    ss = returnTotalUnitsTakenSummary(sheet_names, uploaded_file)

    new_arr = []

    for idx, val in enumerate(ss):
        aa = t_df[idx] / val
        aa = round(aa, 2)
        new_arr.append(aa)

    return new_arr

@st.cache_data
def returnCummulativeUnitsTakenSummary(sheet_names, uploaded_file):
    out_cors = []
    for sn in sheet_names:
        df = pd.read_excel(uploaded_file, sheet_name=sn)

        eac_out_cors = []
        for i in df['Total Points Registered']:    
            eac_out_cors.append(i)
       
        out_cors.append(eac_out_cors)

    df1 = pd.DataFrame()

    for idx, value in enumerate(out_cors):
        df1[str(idx)] = value

    df1 = df1.astype('int64')
    t_df = df1.sum(axis=1, numeric_only= True)


    return t_df

@st.cache_data
def returnCummulativeUnitsPassedSummary(sheet_names, uploaded_file):
    out_cors = []
    for sn in sheet_names:
        df = pd.read_excel(uploaded_file, sheet_name=sn)

        eac_out_cors = []
        for i in df['Total Points Passed']:    
            eac_out_cors.append(i)
       
        out_cors.append(eac_out_cors)

    df1 = pd.DataFrame()

    for idx, value in enumerate(out_cors):
        df1[str(idx)] = value

    df1 = df1.astype('int64')
    t_df = df1.sum(axis=1, numeric_only= True)

    return t_df

@st.cache_data
def returnCGPASummary(sheet_names, uploaded_file):
    out_cors = []
    for sn in sheet_names:
        df = pd.read_excel(uploaded_file, sheet_name=sn)

        eac_out_cors = []
        for i in df['Total Points Scored']:    
            eac_out_cors.append(i)
       
        out_cors.append(eac_out_cors)

    df1 = pd.DataFrame()

    for idx, value in enumerate(out_cors):
        df1[str(idx)] = value

    df1 = df1.astype('int64')
    t_df = df1.sum(axis=1, numeric_only= True)


    ss = returnCummulativeUnitsTakenSummary(sheet_names, uploaded_file)

    new_arr = []

    for idx, val in enumerate(ss):
        aa = t_df[idx] / val
        aa = round(aa, 2)
        new_arr.append(aa)

    return new_arr


st.title('Data Summary')
st.info('Upload The Dataset Downloaded From The Multiple Sheet Calculator To Get The Summary')
try:
    uploaded_file = st.file_uploader("Upload Dataset", type=['csv', 'xlsx'])
except:
    pass

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)
    except:
        wb = openpyxl.load_workbook(uploaded_file) 
        sheet_names = wb.sheetnames

    new_df = pd.DataFrame()
    

    
    new_df['Outstanding Courses'] = returnOutstandingCoursesSummary(sheet_names, uploaded_file)
    new_df['Courses Failed'] = returnCoursesFailedSummary(sheet_names, uploaded_file)
    new_df['Total Units Taken'] = returnTotalUnitsTakenSummary(sheet_names, uploaded_file)
    new_df['Total Units Passed'] = returnTotalUnitsPassedSummary(sheet_names, uploaded_file)
    new_df['Sessional GPA'] = returnSessionalGPASummary(sheet_names, uploaded_file)
    new_df['Cummulative Units Taken'] = returnCummulativeUnitsTakenSummary(sheet_names, uploaded_file)
    new_df['Cummulative Units Passed'] = returnCummulativeUnitsPassedSummary(sheet_names, uploaded_file)
    new_df['CGPA'] = returnCGPASummary(sheet_names, uploaded_file)

    res_ = []

    for i in new_df['CGPA'].values:
        ss = ''
        if float(i) <= 4.5 and float(i) >= 5.0:
            ss = ('First Class')
        elif float(i) <= 4.49 and float(i) >= 3.50:
            ss = ('Second Class Upper')
        elif float(i) <= 3.49 and float(i) >= 2.40:
            ss = ('Second Class Lower')
        elif float(i) <= 2.39 and float(i) >= 1.50:
            ss = ('Third Class')
        elif float(i) <= 1.49 and float(i) >= 1.0:
            ss = ('Pass')

        res_.append(ss)

    new_df['Class Of Degree'] = res_

    rmk = []

    for idx, val in enumerate(new_df['Outstanding Courses']):
        if not len(val) == 0:
            rmk.append('FRNS')
        elif not len(new_df['Courses Failed'].iloc[idx]) == 0:
            rmk.append('FRNS')
        else:
            rmk.append('GRADUATING')

    new_df['Remark'] = rmk

    st.info('Select Other Columns To Make Up The Dataset (Example Name and Reg Number)')

    sht_nm = st.selectbox("Which Sheet Do You Want To Select From?", sheet_names)
    temp_df = pd.read_excel(uploaded_file, sheet_name=sht_nm)

    tr = list(temp_df.columns)
    tr.append('NO OTHER COLUMN NEEDED')

    name_temp_ = st.multiselect("Select Columns", tr)

    if(st.button('Continue')):
        st.dataframe(new_df)

        aa = convert_df(new_df)

        file_name = 'mactechloop (' + uploaded_file.name[:-4].strip()+').csv'

        if(name_temp_[0] == 'NO OTHER COLUMN NEEDED'):
            
            if(st.download_button(
            label="Download CSV File",
            data=aa,
            file_name=file_name,
            mime='text/csv',
                )):
                st.success('Downloaded Successfully')

        else:
            new_df[name_temp_] = temp_df[name_temp_]

            if(st.download_button(
            label="Download CSV File",
            data=aa,
            file_name=file_name,
            mime='text/csv',
                )):
                st.success('Downloaded Successfully')