import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import base64

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Kalkulator Integral & Turunan", page_icon="🧸", layout="centered")

# Panggil file CSS girly soft
with open("style_girly_soft.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Tambahkan background dengan CSS khusus
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://i.pinimg.com/originals/9d/52/3e/9d523e7cfd3821b3bbd4528f20664a8d.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

# Fungsi tampilan login cute aesthetic

def login_ui():
    st.markdown("""
        <div style="text-align:center; padding:20px;">
            <img src="https://cdn-icons-png.flaticon.com/512/847/847969.png" width="100"/>
            <h2 style="color:#ff69b4;">Welcome! 🍓</h2>
            <p style="color:#b56f77; font-style:italic;">Login dulu yuk sebelum hitung-hitungan 🧸</p>
        </div>
    """, unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input("Username", placeholder="Masukkan username")
        password = st.text_input("Password", type="password", placeholder="Masukkan password")
        masuk = st.form_submit_button("Masuk")

        if masuk:
            if username == "bila" and password == "cantik":
                st.session_state.login = True
                st.success("Yay kamu berhasil masuk!")
            else:
                st.error("Ups! Username atau password salah, coba lagi yaa 🙈")

# Fungsi tombol logout di kiri bawah sejajar konten

def logout_ui():
    if st.button("Keluar", key="logout", help="Keluar dari aplikasi"):
        st.session_state.clear()
        st.experimental_rerun()

# Cek status login dan tampilkan login page lebih awal
if 'login' not in st.session_state:
    st.session_state.login = False

if st.session_state.login is False:
    login_ui()
    st.stop()

# Judul utama
st.markdown('<div class="main-title">🧸 Kalkulator Integral & Turunan 🧸</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Masukkan fungsi matematikanya!🍓</div>', unsafe_allow_html=True)

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
    st.subheader("🎀 Grafik Fungsi dan Turunannya")
    x_vals = np.linspace(-10, 10, 400)
    f = sp.lambdify(x, expr, modules=['numpy'])
    df = sp.lambdify(x, turunan, modules=['numpy'])

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x_vals, f(x_vals), label='Fungsi Asli', color='#ff9aa2')
    ax.plot(x_vals, df(x_vals), label='Turunannya', linestyle='--', color='#d28e8e')
    ax.set_title("Grafik Fungsi dan Turunan", fontsize=14, color='#b56f77')
    ax.grid(True, linestyle='dashed', alpha=0.3)
    ax.legend()
    st.pyplot(fig)

except Exception as e:
    st.error("Fungsi tidak valid. Coba periksa kembali input kamu yaa")

# Tombol Logout
logout_ui()
