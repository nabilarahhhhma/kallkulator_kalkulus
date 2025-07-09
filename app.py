import streamlit as st

# Tambahin CSS lucu
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🌸 Kalkulator Kalkulus Cute 🌸")

import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Kalkulator Integral & Turunan", page_icon="🌸", layout="centered")

# CSS tema pink cute aesthetic
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background-color: #ffe6f0;
            font-family: 'Comic Sans MS', cursive;
        }
        .main-title {
            text-align: center;
            color: #e75480;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            color: #c71585;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Judul utama
st.markdown('<div class="main-title">🌸 Kalkulator Integral & Turunan Cute Edition 🌸</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Masukkan fungsi matematika kamu di bawah ini dan lihat hasilnya dengan gaya pink yang lucu~!</div>', unsafe_allow_html=True)

# Input fungsi dari user
expr_input = st.text_input("Masukkan fungsi aljabar (misalnya: x**2 + 3*x + 2)", value="x**2 + 2*x + 1")
x = sp.symbols('x')

try:
    expr = sp.sympify(expr_input)
    turunan = sp.diff(expr, x)
    integral = sp.integrate(expr, x)

    st.subheader("📄 Hasil Perhitungan")
    st.success(f"**Fungsi Asli:** {expr}")
    st.info(f"**Turunan:** {turunan}")
    st.warning(f"**Integral:** {integral} + C")

    # Grafik
    st.subheader("🌼 Grafik Fungsi dan Turunannya")
    x_vals = np.linspace(-10, 10, 400)
    f = sp.lambdify(x, expr, modules=['numpy'])
    df = sp.lambdify(x, turunan, modules=['numpy'])

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x_vals, f(x_vals), label='Fungsi Asli', color='#ff69b4')
    ax.plot(x_vals, df(x_vals), label='Turunannya', linestyle='--', color='#ff1493')
    ax.set_title("Grafik Fungsi dan Turunan", fontsize=14, color='#c71585')
    ax.grid(True, linestyle='dashed', alpha=0.3)
    ax.legend()
    st.pyplot(fig)

except Exception as e:
    st.error("Fungsi tidak valid. Coba periksa kembali input kamu ya~")
