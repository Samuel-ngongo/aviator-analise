import streamlit as st

st.set_page_config(page_title="Previsão de Queda - Aviator", layout="centered")

# Título com estilo
st.markdown("<h1 style='text-align: center; color: darkred;'>Previsão de Queda - Aviator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Insere os valores dos multiplicadores (ex: 1.20, 2.50, 1.75, etc.) separados por vírgula:</p>", unsafe_allow_html=True)

# Caixa de entrada com borda e dica
valores_input = st.text_input("Insere os multiplicadores aqui:", placeholder="Exemplo: 1.20, 2.50, 3.75")

if valores_input:
    try:
        valores = [float(x.strip()) for x in valores_input.split(",") if x.strip()]
        media = sum(valores) / len(valores)

        # Resultado com estilo
        st.success(f"Média calculada: {media:.2f}")

        # Tendência com base na média
        if media < 2:
            st.error("Tendência de queda repentina.")
        elif 2 <= media <= 3:
            st.warning("Tendência de voo moderado.")
        else:
            st.info("Tendência de voo prolongado.")

    except ValueError:
        st.error("Por favor, insere apenas números válidos separados por vírgula.")
else:
    st.markdown("<p style='color: gray;'>Aguardando dados...</p>", unsafe_allow_html=True)

# Rodapé estilizado
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px;'>Desenvolvido por Samuel Ngongo</p>", unsafe_allow_html=True)
