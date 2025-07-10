import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import base64

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Kalkulator Integral & Turunan", page_icon="🌸", layout="centered")

# CSS tema pink cute aesthetic
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Fungsi tampilan login cute aesthetic
def login_ui():
    st.markdown("""
        <div style="text-align:center; padding:20px;">
            <img src="https://cdn-icons-png.flaticon.com/512/2922/2922561.png" width="100"/>
            <h2 style="color:#ff69b4;">Selama Datang!🌸</h2>
            <p style="color:#d63384; font-style:italic;">Login dulu yuk sebelum hitung-hitungan cantik</p>
        </div>
    """, unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="Masukkan username kamu...")
    password = st.text_input("Password", type="password", placeholder="Masukkan password lucu...")

    # Tombol masuk di kanan bawah
    st.markdown("""
        <div style='text-align: right;'>
            <button onclick="document.getElementById('submit-login').click()" style="background-color: #ffb6c1; color: white; padding: 10px 20px; border: none; border-radius: 10px; font-weight: bold;">
                Masuk
            </button>
        </div>
    """, unsafe_allow_html=True)

    if st.button("__INTERNAL_MASUK__", key="submit-login", help="", use_container_width=False):
        if username == "bila" and password == "cantik":
            st.session_state.login = True
            st.success("Yay kamu berhasil masuk!")
        else:
            st.error("Ups! Username atau password salah, coba lagi yaa")

# Fungsi tombol logout di kanan bawah
def logout_ui():
    st.markdown("""
        <div style='text-align: right; margin-top: 20px;'>
            <form action="" method="post">
                <button type="submit" name="logout" style="background-color: #ffb6c1; color: white; padding: 10px 20px; border: none; border-radius: 10px; font-weight: bold;">
                    Keluar
                </button>
            </form>
        </div>
    """, unsafe_allow_html=True)
    if st.session_state.get("logout"):
        st.session_state.login = False
        st.rerun()

# Cek status login dan tampilkan login page lebih awal
if 'login' not in st.session_state:
    st.session_state.login = False

if st.session_state.login is False:
    login_ui()
    st.stop()  # menghentikan eksekusi supaya user ga bisa lanjut sebelum login

# Judul utama
st.markdown('<div class="main-title">🌸 Kalkulator Integral & Turunan 🌸</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Masukkan fungsi matematika kamu di bawah ini!</div>', unsafe_allow_html=True)

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
    st.error("Fungsi tidak valid. Coba periksa kembali input kamu yah!")

# Tombol Logout di kanan bawah (sticky)
logout_ui()

