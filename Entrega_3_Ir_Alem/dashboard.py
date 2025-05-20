
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Conectar ao banco de dados
conn = sqlite3.connect('sensor_data.db')
df = pd.read_sql_query("SELECT * FROM sensores", conn)

st.title("Dashboard - Sistema de Irrigação FarmTech Solutions")

# Mostrar dados em tabela
st.subheader("📊 Dados Coletados")
st.dataframe(df)

# Gráfico de umidade
st.subheader("💧 Umidade do Solo")
fig, ax = plt.subplots()
ax.plot(df["id"], df["umidade"], marker='o', label="Umidade")
ax.set_xlabel("ID da Leitura")
ax.set_ylabel("Umidade (%)")
ax.legend()
st.pyplot(fig)

# Gráfico de status da irrigação
st.subheader("🚿 Status da Irrigação (Relé)")
status = df["irrigacao_ativa"].value_counts().rename({1: "Ativa", 0: "Inativa"})
st.bar_chart(status)

# Gráfico de pH
st.subheader("🧪 Nível de pH")
fig2, ax2 = plt.subplots()
ax2.plot(df["id"], df["ph"], color='green', marker='x', label="pH")
ax2.set_xlabel("ID da Leitura")
ax2.set_ylabel("pH")
ax2.legend()
st.pyplot(fig2)

conn.close()
