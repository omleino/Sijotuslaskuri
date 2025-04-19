import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Asetukset ja otsikko
st.set_page_config(page_title="Sijoituslaskuri", layout="centered")
st.title("Sijoituslaskuri")

# --- 1. Käyttäjän syötteet ---
kuukausisaasto = st.number_input("Kuukausisäästö (€)", min_value=0, value=200, step=10)
vuosituotto = st.slider("Tuotto-odotus (% vuodessa)", 0.0, 15.0, 5.0, step=0.1)
vuodet = st.slider("Sijoitusaika (vuotta)", 1, 50, 20)

# --- 2. Laskentamuuttujat ---
kuukaudet = vuodet * 12
kuukausituotto = (1 + vuosituotto / 100) ** (1 / 12) - 1
ajat = np.arange(1, kuukaudet + 1)

# --- 3. Taulukoiden alustukset ---
pääoma = np.zeros(kuukaudet)
arvo = np.zeros(kuukaudet)

# --- 4. Laskenta silmukassa ---
for i in range(kuukaudet):
    pääoma[i] = kuukausisaasto * (i + 1)
    if i == 0:
        arvo[i] = kuukausisaasto
    else:
        arvo[i] = arvo[i - 1] * (1 + kuukausituotto) + kuukausisaasto

korko = arvo - pääoma

# --- 5. Näytä tulokset ---
st.subheader("Tulokset")
st.write(f"**Sijoitettu pääoma:** {pääoma[-1]:,.2f} €")
st.write(f"**Kertynyt korkotuotto:** {korko[-1]:,.2f} €")
st.write(f"**Sijoituksen arvo yhteensä:** {arvo[-1]:,.2f} €")

# --- 6. Piirrä kuvaaja ---
fig, ax = plt.subplots()
ax.plot(ajat / 12, arvo, label="Sijoituksen arvo")
ax.plot(ajat / 12, pääoma, label="Sijoitettu pääoma", linestyle='--')
ax.fill_between(ajat / 12, pääoma, arvo, alpha=0.3, color="orange", label="Korkotuotto")
ax.set_xlabel("Aika (vuotta)")
ax.set_ylabel("Euroa (€)")
ax.set_title("Sijoituksen kehitys")
ax.legend()
ax.grid(True)
st.pyplot(fig)
