import streamlit as st
import pandas as pd

def tsi_main():
    st.title("TSI Evaluation")

    uploaded_file = st.sidebar.file_uploader("Upload a TSI file", type=["csv"])

    if uploaded_file is not None:
        
        try:
            # Read the uploaded CSV file into a Pandas DataFrame
            df = pd.read_csv(uploaded_file)
            st.sidebar.success('TSI Loaded Successfully')

        except Exception as e:
            st.sidebar.error(f"An error occurred: {e}")

    else:
        df = []
        st.sidebar.error('Upload TSI File')

    return df

def query_tsi():

    report_id = st.text_input('Input TSI Number')

    if report_id is not None:
        try:
            filtered_df = df.loc[df['Report ID']==report_id]
            
            col1, col2 = st.columns(2)
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

            st.write('__Cause of Failure__')
            st.write(filtered_df['Cause of Failure'].item())
            st.write('__Factory Reply__')
            st.write(filtered_df['Cause of Failure.'].item())
        except Exception as e:
            # st.sidebar.error(f"An error occurred: {e}")
            st.sidebar.error('No TSI Number provided')

    else:
        st.write('Input TSI Number')


if __name__ == "__main__":
    df = tsi_main()
    query_tsi()