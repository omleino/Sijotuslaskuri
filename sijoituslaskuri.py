import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sijoituslaskuri", layout="centered")
st.title("Sijoituslaskuri")

kuukausisaasto = st.number_input("Kuukausisäästö (€)", min_value=0.0, value=200.0 step=10)
vuosituotto = st.slider("Tuotto-odotus (% vuodessa)", 0.0, 15.0, 5.0, step=0.1)
vuodet = st.slider("Sijoitusaika (vuotta)", 1, 50, 20)

kuukausituotto = (1 + vuosituotto / 100) ** (1 / 12) - 1
kuukaudet = vuodet * 12
ajat = np.arange(1, kuukaudet + 1)

arvo = np.zeros(kuukaudet)
pääoma = np.zeros(kuukaudet)

for i in range(kuukaudet):
    pääoma[i] = kuukausisaasto * (i + 1)
    if i == 0:
        arvo[i] = kuukausisaasto
    else:
        arvo[i] = arvo[i - 1] * (1 + kuukausituotto) + kuukausisaasto

korko = arvo - pääoma

st.subheader("Tulokset")
st.write(f"Sijoitettu pääoma: {pääoma[-1]:,.2f} €")
st.write(f"Korkotuotto: {korko[-1]:,.2f} €")
st.write(f"Yhteensä: {arvo[-1]:,.2f} €")

fig, ax = plt.subplots()
ax.plot(ajat / 12, arvo, label="Sijoituksen arvo")
ax.plot(ajat / 12, pääoma, label="Sijoitettu pääoma", linestyle='--')
ax.fill_between(ajat / 12, pääoma, arvo, alpha=0.3, color="orange", label="Korkotuotto")
ax.set_xlabel("Vuodet")
ax.set_ylabel("Euroa")
ax.set_title("Sijoituksen kehitys")
ax.legend()
ax.grid(True)
st.pyplot(fig)
