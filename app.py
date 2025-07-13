import streamlit as st
from sympy import diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
from sympy.abc import x
import hashlib

# --- Load CSS Girly ---
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Auth (Mini versi) ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

user_db = {
    "bila": hash_password("cantik")
}

if "login" not in st.session_state:
    st.session_state.login = False
if "user" not in st.session_state:
    st.session_state.user = ""

# --- Login ---
def login_form():
    st.markdown("<h2>🎀 Welcome Queen 🎀</h2>", unsafe_allow_html=True)
    username = st.text_input("👛 Username")
    password = st.text_input("🔒 Password", type="password")
    if st.button("Login"):
        if username in user_db and user_db[username] == hash_password(password):
            st.success(f"Hi {username}, kamu masuk dengan sukses! 💫")
            st.session_state.login = True
            st.session_state.user = username
        else:
            st.error("Oops! Username atau Password salah")

# --- Kalkulator Function ---
def kalkulator():
    st.markdown("### 🧮 Kalkulator Integral & Turunan")
    fungsi_input = st.text_input("📌 Masukkan fungsi (contoh: x**2 + 2*x)", value="x**2 + 2*x")
    operasi = st.radio("✨ Pilih Operasi", ["Turunan", "Integral"])
    x_vals = np.linspace(-10, 10, 400)

    if fungsi_input:
        try:
            fungsi = sympify(fungsi_input)
            f_numeric = lambdify(x, fungsi, modules=["numpy"])
            y_asli = f_numeric(x_vals)

            if operasi == "Turunan":
                turun = diff(fungsi, x)
                turun_numeric = lambdify(x, turun, modules=["numpy"])
                y_turun = turun_numeric(x_vals)

                st.latex(f"\\frac{{d}}{{dx}}\\left({str(fungsi)}\\right) = {str(turun)}")
                st.markdown("#### 📉 Grafik")
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_asli, label="f(x)", color="#ff69b4")
                ax.plot(x_vals, y_turun, label="f'(x)", color="#d63384", linestyle="--")
                ax.legend()
                st.pyplot(fig)

            elif operasi == "Integral":
                hasil = integrate(fungsi, x)
                st.latex(f"\\int {str(fungsi)}\,dx = {str(hasil)} + C")
                st.markdown("#### 📉 Grafik")
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_asli, label="f(x)", color="#ff69b4")
                ax.legend()
                st.pyplot(fig)

        except Exception:
            st.error("🌧️ Fungsi tidak valid. Contoh valid: x**2 + 2*x")

# --- Profil Page ---
def about():
    st.markdown("### 👑 Tentang Aplikasi Queqet Ini")
    st.write("""
        Aplikasi lucu ini dibuat oleh **Nabila Rahmadani** dari kelas **TI.24.C.1**.  

    """)
    st.image("https://i.pinimg.com/564x/f1/1d/b2/f11db2b76fef26795a27d0212041a203.jpg", width=250)

# --- Main Menu Tabs ---
def menu_tabs():
    tab1, tab2, tab3 = st.tabs(["🧮 Kalkulator", "🎀 Tentang", "🚪 Logout"])
    with tab1:
        kalkulator()
    with tab2:
        about()
    with tab3:
        st.session_state.login = False
        st.session_state.user = ""
        st.success("Kamu sudah logout~ Bye bye~ 🐣")
        st.experimental_rerun()

# --- App Routing ---
if st.session_state.login:
    st.markdown(f"<div style='text-align:right;'>👑 Logged in as: <b>{st.session_state.user}</b></div>", unsafe_allow_html=True)
    st.markdown("<h1>🎀 Cute Calculus App 🎀</h1>", unsafe_allow_html=True)
    menu_tabs()
else:
    login_form()
