import streamlit as st
import pandas as pd
from main import AesEncrypt

safe = AesEncrypt()
uploaded_file = st.file_uploader("Escolha o arquivo .CSV:", type=["csv"])

def main():
    with st.form("my_form"):
        st.title("Recolhendo Dados:")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            columns = st.multiselect(
                "Escolha as colunas a serem encriptografadas:",
                 df.columns.tolist(),
                 df.columns.tolist())
       
        
        if st.form_submit_button("Criptografar") and uploaded_file:
        
            #df = pd.read_csv(uploaded_file)
            columns = df.columns.tolist()
 
            encrypt = safe.show(df, columns)
            st.write(encrypt)

if __name__ == '__main__':
    main()