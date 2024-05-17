import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
tabela02 = pd.read_csv("tabela.csv")

# Carregando as imagens
velo_image = plt.imread("velo.png")
tips_image = plt.imread("tips.png")
site1_image = plt.imread("site1.png")
buyoo_image = plt.imread("buyoo.png")
buyin_field_image = plt.imread("buyin-field.png")
buy_image = plt.imread("buy.png")
image_2024 = plt.imread("2024.png")



# Configurações do layout
st.set_page_config(page_title="Dashboard de Torneios de Poker", layout="wide")

# Criando o app
st.title("Dashboard CL Team Poker")
st.write("Simples porque foi feito muito rapido")

# Definindo o layout em colunas
col1, col2 = st.columns(2)

# Exibindo as imagens na primeira coluna
with col1:
    st.image(velo_image, caption="Velocidade", use_column_width=True)
    st.image(tips_image, caption="Tips", use_column_width=True)
    st.image(site1_image, caption="Site1", use_column_width=True)

# Exibindo as imagens na segunda coluna
with col2:
    st.image(buyoo_image, caption="Buyoo", use_column_width=True)
    st.image(buyin_field_image, caption="Buy-in Field", use_column_width=True)
    st.image(buy_image, caption="Buy", use_column_width=True)
    st.image(image_2024, caption="2024", use_column_width=True)

# Título da tabela
st.header("Tabela 2023 e 2024")

# Exibindo a tabela
st.write(tabela02)
