import streamlit as st
import pandas as pd
from main import AesEncrypt

safe = AesEncrypt()

def main():
    st.title("Recolhendo Dados:")
    uploaded_file = st.file_uploader("Escolha o arquivo .CSV:", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        column = st.selectbox(
            "Escolha a coluna a ser criptografada:",
            df.columns.tolist())

        if st.button("Criptografar"):
            encrypt = safe.show(df, column)

            st.title("Criptografia:")
            col1, col2 = st.columns(2) 
            with col1:
               st.header("Antes")
               st.write(encrypt[column])
            with col2:
               st.header("Depois")
               new_column = "AES-" + column
               st.write(encrypt[new_column].to_frame().style.set_properties(**{"background-color":"red"}))

        # AESL_COL é atributo da classe. Estou limpando ele (LISTA).
        safe.AES_COL.clear()
                
if __name__ == '__main__':
    main()