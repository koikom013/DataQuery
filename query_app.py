import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

def tsi_main():
    st.title("TSI Evaluation")

    uploaded_file = st.sidebar.file_uploader("Upload a TSI file", type=["xlsx","csv])

    
    if uploaded_file is not None:
        
        try:
            # Read the uploaded CSV or XLSX file into a Pandas DataFrame
            if 'df_tsi' not in st.session_state:
                if uploaded_file.endswith('xlsx'):
                    st.session_state['df_tsi'] = pd.read_excel(uploaded_file)
                else:
                    st.session_state['df_tsi'] = pd.read_csv(uploaded_file)
                    
                df = st.session_state['df_tsi']
            else:
                df = st.session_state['df_tsi']
            
            st.sidebar.success('TSI Loaded Successfully')
            

            

        except Exception as e:
            st.sidebar.error(f"An error occurred: {e}")

    else:
        df = []
        st.sidebar.error('Upload TSI File')

    return df

def query_tsi():

    report_id = st.text_input('Input TSI Number')

    tab = st.tabs(['Evaluation','TSI List'])

    with tab[0]:

        if report_id is not None:
            try:
                filtered_df = df.loc[df['Report ID']==report_id]
                filtered_df['Create Lead Time'] = filtered_df['Created On'] - filtered_df['Failure Date']
                filtered_df['Approval Lead Time'] = filtered_df['Approved Date'] - filtered_df['Created On']
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.write('__Report ID__')
                    st.write(filtered_df['Report ID'].item())
                    st.write('__Full Model__')
                    st.write(filtered_df['Full Model'].item())
                    st.write('__Serial Number__')
                    st.write(filtered_df['Serial Number'].item())
                with col2:
                    st.write('__Failure Date__')
                    st.write(filtered_df['Failure Date'].item())
                    st.write('__Failure SMR__')
                    st.write(filtered_df['Failure SMR'].item())
                    st.write('__Hours on Parts__')
                    st.write(filtered_df['Hours on Parts'].item())
                with col3:
                    st.write('__DB Contact__')
                    st.write(filtered_df['Distributor Contact'].item())
                    st.write('__TSI Creation Date__')
                    st.write(filtered_df['Created On'].item())
                    st.write('__TSI Approval Date__')
                    st.write(filtered_df['Approved Date'].item())
                with col4:
                    st.write('__Customer Name__')
                    st.write(filtered_df['Current Customer Name'].item())
                    st.write('__Create Lead Time__')
                    st.write(filtered_df['Create Lead Time'].item())
                    st.write('__Approval Lead Time__')
                    st.write(filtered_df['Approval Lead Time'].item())

                st.write('__Cause of Failure__')
                st.write(filtered_df['Cause of Failure'].item())
                st.write('__Factory Reply__')
                st.write(filtered_df['Cause of Failure.'].item())
            except Exception as e:
                # st.sidebar.error(f"An error occurred: {e}")
                st.sidebar.error('No TSI Number provided')

        else:
            st.write('Input TSI Number')

        

    with tab[1]:
        st.header('TSI Record')
        st.dataframe(df)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

if __name__ == "__main__":
    df = tsi_main()
    query_tsi()
