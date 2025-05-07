import streamlit as st
import pandas as pd

st.title("Previsão de Queda - Aviator")

st.write("Insere os valores dos multiplicadores (ex: 1.20, 2.50, 1.75, etc.) separados por vírgula:")

entrada = st.text_input("Valores:")

if entrada:
    try:
        valores = [float(x.strip()) for x in entrada.split(',')]
        media = sum(valores) / len(valores)
        st.success(f"Média calculada: {media:.2f}")

        if media < 2:
            st.warning("Risco alto de queda em breve.")
        else:
            st.info("Tendência de voo prolongado.")
    except:
        st.error("Certifica-te de que todos os valores são números separados por vírgula.")
