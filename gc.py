import seaborn as sns
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.pyplot as plt
import altair as alt

downloads_path = str(Path.home() / "Downloads")
unlocked = False
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')


def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

def _sum(arr):
    sum = 0

    for i in arr:
        sum = sum + i
 
    return(sum)

st.title('GPA CALCULATOR')
st.info('Built With ❤️ By MacTechLoop (mactechloop@gmail.com)')

        
activities=['Casual Calculator', 'Visualised Calculator']
option=st.selectbox('Selection option:',activities)

if(option == 'Casual Calculator'):
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

elif(option == 'Visualised Calculator'):

            if(st.button('View Sample Dataset Image')):
                st.info('Number Of Columns Dosen\'t Matter')
                st.image('sampledata.PNG')
            try:
                uploaded_file = st.file_uploader("Upload Dataset", type={'csv'})
            except:
                pass

            if uploaded_file is not None:

                df = pd.read_csv(uploaded_file)
#                 st.dataframe(df)

                ccr = st.text_input('Input All Credit Accordingly Seperated By A Comma')

                if(st.button('PROCEED')):

                    cred_uni = ccr.split(',')
                    cred_uni = [ int(x) for x in cred_uni]

                
                    def returnTotalRegUnit(credit_units1):
                        dd_ar = []
                        ttp = []

                        for yy in range(len(df)):
                            ndf = df.iloc[yy]
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

                    def returnTotalPassed(credit_units1):
                        t_p_p = []

                        for xx in range(len(df)):
                            jtt = _sum(credit_units1)
                            ndfa = df.iloc[xx]
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

                    def returnTotalFailed(credit_units1):
                        t_u_f = []
                        for yy in range(len(df)):
                            sss = 0
                            ndfa1 = df.iloc[yy]
                            anpr1 = ndfa1.values
                            count = 0
                            for j in anpr1:
                                try:
                                    if(int(j) <= 39):
                                        sss += credit_units1[count]
                                except:
                                    pass
 #                                   sss += credit_units1[count]
                                count += 1

                            t_u_f.append(sss)
                            sss = 0

                        return t_u_f

                    def returnTotalPoints(credit_units1):
                        t_p_i_t = []

                        for yy in range(len(df)):
                            ndf = df.iloc[yy]
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



                    rtf = returnTotalFailed(cred_uni)
                    rtp = returnTotalPassed(cred_uni)
                    rtr = returnTotalRegUnit(cred_uni)
                    rtsp = returnTotalPoints(cred_uni)

                    df['Total Points Registered'] = rtr
                    df['Total Points Passed'] = rtp
                    df['Total Points Failed'] = rtf
                    df['Total Points Scored'] = rtsp

                    gp = []
                    for i in range(len(df['Total Points Passed'])):
                        tgp = df['Total Points Scored'][i] / df['Total Points Registered'][i]
                        tgp = round(tgp, 3)
                        gp.append(tgp)


                    df['GPA'] = gp


                    st.dataframe(df)

                    ndf = df['GPA']

                    res_ = []
                    for i in df['GPA'].values:
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
                    
                    ndf['Grade'] = res_
                    ndf['No Of Students'] = [i for i in range(len(ndf['Grade']))]

                

                    data1 = pd.DataFrame({
                        'RANKING': ndf['Grade'],
                        'No Of Students': ndf['No Of Students'],
                    })

                    chart = (alt.Chart(data1).mark_boxplot().encode(
                        x=alt.X('RANKING', sort=None),
                        y=alt.Y('No Of Students', sort=None)
                    ))

                    st.altair_chart(chart, use_container_width=True)
        
                    
                    aa = convert_df(df)

                    file_name = 'mactechloop (' + uploaded_file.name[:-4].strip()+').csv'

                    if(st.download_button(
                    label="Download CSV File",
                    data=aa,
                    file_name=file_name,
                    mime='text/csv',
                        )):
                        st.success('Downloaded Successfully')
            

    
