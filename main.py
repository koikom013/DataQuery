import streamlit as st
import pandas as pd



# import sys
# from path import Path

# dir = path.Path(__file__).abspath()
# sys.append.path(dir.parent.parent)


#Functions
def load_data():
    filename = './data/Claim_Record_Query.csv'
    data = pd.read_csv(filename,header=1)
    data = data.replace(',','', regex=True)
    return data

def query_by_claim_number(clm_num):
    df = data.loc[data['CTL_CLAIM_NO']==clm_num].reset_index()
    return df

#------------------------------------------------------------------

data = load_data()

tab = st.tabs(['Claims','TSI'])

#--------------Claims---------------------------------------

with tab[0]:
    claim_number = st.text_input('Input Claim Number',placeholder='00000')
    
    if st.button('Search') or claim_number!='':
        st.markdown('---')
        df = query_by_claim_number(int(claim_number))

        parts_cost = float(df['BASE_APP_PARTS_AMOUNT'][0])
        labor_cost = float(df['BASE_APP_LABOR_AMOUNT'][0])
        mile_cost = float(df['BASE_APP_MILEAGE_AMOUNT'][0])
        other_cost = float(df['BASE_APP_OTHER_AMOUNT'][0])
        total_cost = float(df['BASE_APP_TOTAL_AMOUNT'][0])
        tsi_num = df['CTL_ETSI'][0]
        
        claim_date = pd.to_datetime(df['CTL_CLAIM_DATE'][0],format='%Y%m%d').strftime("%d %b %Y")
        delivery_date = pd.to_datetime(df['CTL_DELIVERY_DATE'][0],format='%Y%m%d').strftime("%d %b %Y")
        failure_date = pd.to_datetime(df['CTL_FAILURE_DATE'][0],format='%Y%m%d').strftime("%d %b %Y")
        corrected_date = pd.to_datetime(df['CTL_CORRECTED_DATE'][0],format='%Y%m%d').strftime("%d %b %Y")
        
        mch_model = str(df['CTL_MACHINE_MODEL'][0])+'-'+str(df['CTL_MACHINE_TYPE'][0])+str(df['CTL_MACHINE_SUBTYPE'][0])
        mch_serial = df['CTL_MACHINE_SERIAL'][0]

        parts_name = df['PARTS_NAME']
        parts_num = df['PARTS_NBR']
        parts_qty = df['PARTS_QTY']
        parts_uprice = df['PARTS_UNIT_PRICE']

        
        col1,col2,col3 = st.columns([1,1,3])

        with col1:
            st.markdown('**Claim Number**')
            st.write(claim_number)
            
            st.markdown('__Model__')
            st.write(mch_model)

            st.markdown('__Serial__')
            st.write(mch_serial)

            st.markdown('__TSI/ETSI No.__')
            st.write(tsi_num)

        with col2:
            st.markdown('**Delivery Date**')
            st.write(delivery_date)

            st.markdown('__Failure Date__')
            st.write(failure_date)

            st.markdown('__Corrected Date__')
            st.write(corrected_date)
        
            st.markdown('__Claim Date__')
            st.write(claim_date)

        with col3:
            
            st.subheader('Parts List')

            st.table(df[['PARTS_NBR','PARTS_NAME','PARTS_QTY','PARTS_UNIT_PRICE']])

            
        st.markdown('---')

        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.markdown('__Parts Cost__')
            st.subheader(parts_cost)

        with col2:
            st.markdown('__Labor Cost__')
            st.subheader(labor_cost)
        with col3:
            st.markdown('__Other Cost__')
            st.subheader(other_cost)

        with col4:
            st.markdown('__Total Cost__')
            st.subheader(total_cost)

        st.markdown('---')

#--------------TSI--------------------------------------        

df_tsi = pd.read_csv('./data/tsi_list.csv')


with tab[1]:
    st.subheader('TSI Query here ->')

    col1,col2 = st.columns(2)

    with col1:

        rep_id = st.text_input('Input TSI Number')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        if st.button('Search by TSI Number'):
            df_id = df_tsi.loc[df_tsi['Report ID']==rep_id].reset_index(drop=True)
            st.subheader('TSI Details')
            st.write('TSI Number:',rep_id)
            st.write('Model:',df_id['Full Model'][0])
            st.write('Failure Date:',df_id['Failure Date'][0])
            st.write('Failure SMR:',df_id['Failure SMR'][0])
            st.write('Failed Part Number:', df_id['Failed Part Number'][0])
            
            st.markdown('__Cause of Failure__')
            st.write(df_id['Cause of Failure'][0])
            st.markdown('__Factory Reply__')
            st.write(df_id['Cause of Failure.'][0])

    with col2:
    
        pn_query = st.text_input('Input Part Number')
        wc_query = st.text_input('Wild Card Term Query')
        

    
        

        if st.button('Search by Part Number'):
            df_pn = df_tsi.loc[(df_tsi['Failed Part Number']==pn_query) & \
                            (df_tsi['Cause of Failure'].str.contains(wc_query,case=False,na=False))
                            ].reset_index(drop=True)



            st.subheader(f'Total TSI Count: {len(df_pn)} related failure')
            for i in range(len(df_pn)):
                st.markdown('__TSI Details__')
                st.write(i,df_pn['Report ID'][i],'|',df_pn['Full Model'][i],'|',df_pn['Failed Part Number'][i],'|',
                        df_pn['Failure Date'][i],'|',df_pn['Failure SMR'][i],'|',df_pn['Working Country'][i])
                st.markdown('__Cause of Failure__')
                st.write(df_pn['Cause of Failure'][i])
                st.write('__Factory Reply__')
                st.write(df_pn['Cause of Failure.'][i])
                st.markdown('---')

        
        

if __name__=='__main__':
    data = load_data()
