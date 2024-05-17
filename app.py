import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
tabela02 = pd.read_csv("tabela.csv")

# Carregando as imagens e gráficos
velo_image = plt.imread("velo.png")
tips_image = plt.imread("tips.png")
site1_image = plt.imread("site1.png")
buyoo_image = plt.imread("buyoo.png")
buyin_field_image = plt.imread("buyin-field.png")
buy_image = plt.imread("buy.png")
image_2024 = plt.imread("2024.png")
velo_image1 = plt.imread("velo2.png")
site1_image1 = plt.imread("site.png")
buyoo_image1 = plt.imread("buyo.png")
buyin_field_image1 = plt.imread("buy-field2.png")
buy_image1 = plt.imread("buy-in2.png")
image_20241 = plt.imread("20224.png")
image_20245 = plt.imread("20242.png")

# Configurações do layout
st.set_page_config(page_title="Dashboard de Torneios de Poker", layout="wide")

# Criando o app
st.title("Dashboard CL Team Poker")
st.write("Simples porque foi feito muito rápido")

# Definindo o layout em quatro colunas
col1, col2, col3, col4 = st.columns(4)

# Exibindo as imagens e gráficos na primeira coluna
with col1:
    st.image(velo_image, caption="Velocidade", use_column_width=True)
    st.image(tips_image, caption="Tips", use_column_width=True)
    st.image(site1_image, caption="Site1", use_column_width=True)
    st.image(buyoo_image, caption="Buyoo", use_column_width=True)

# Exibindo as imagens e gráficos na segunda coluna
with col2:
    st.image(buyin_field_image, caption="Buy-in Field", use_column_width=True)
    st.image(buy_image, caption="Buy", use_column_width=True)
    st.image(image_2024, caption="2024", use_column_width=True)
    st.image(velo_image1, caption="Velocidade 2", use_column_width=True)

# Exibindo as imagens e gráficos na terceira coluna
with col3:
    st.image(site1_image1, caption="Site 2", use_column_width=True)
    st.image(buyoo_image1, caption="Buyoo 2", use_column_width=True)
    st.image(buyin_field_image1, caption="Buy-in Field 2", use_column_width=True)
    st.image(buy_image1, caption="Buy 2", use_column_width=True)

# Exibindo as imagens e gráficos na quarta coluna
with col4:
    st.image(image_20241, caption="2024 2", use_column_width=True)
    st.image(image_20245, caption="2024 3", use_column_width=True)

# Título da tabela
st.header("Tabela 2023 e 2024")

# Exibindo a tabela
st.write(tabela02)

