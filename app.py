import streamlit as st
from sympy import diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
from sympy.abc import x
from login import login_form, user_db

# --- Load QUEQET CSS ---
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Session Init ---
if "login" not in st.session_state:
    st.session_state.login = False
if "user" not in st.session_state:
    st.session_state.user = ""

# --- Kalkulator Cute ---
def kalkulator():
    st.markdown("<h2>🐰 Kalkulator Integral & Turunan 🐰</h2>", unsafe_allow_html=True)
    fungsi_input = st.text_input("📌 Masukkan fungsi (contoh: x**2 + 2*x)", value="x**2 + 2*x")
    operasi = st.radio("✨ Pilih Operasi yang ingin dihitung:", ["Turunan", "Integral"])
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
                st.markdown("#### 📉 Grafik f(x) dan f'(x)")
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_asli, label="f(x)", color="#ffb6c1")
                ax.plot(x_vals, y_turun, label="f'(x)", color="#ff69b4", linestyle="--")
                ax.legend()
                st.pyplot(fig)

            elif operasi == "Integral":
                hasil = integrate(fungsi, x)
                st.latex(f"\\int {str(fungsi)}\\,dx = {str(hasil)} + C")
                st.markdown("#### 📉 Grafik f(x)")
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_asli, label="f(x)", color="#ff69b4")
                ax.legend()
                st.pyplot(fig)

        except Exception:
            st.error("🌧️ Fungsi tidak valid. Contoh valid: x**2 + 2*x")

# --- Tentang Page ---
def about():
    st.markdown("### 🧸 Tentang Aplikasi Ini 🧸")

    st.write("""
    Aplikasi ini dibuat oleh **Nabila Rahmadani** dari kelas **TI.24.C.1** 🩷  
    Menggunakan Python + Streamlit, aplikasi ini dirancang untuk menghitung turunan dan integral dengan cara **cepat, visual, dan pastinya cute!**

    📌 Fitur aplikasi:
    – Menghitung turunan otomatis  
    – Menghitung integral tak tentu  
    – Menampilkan grafik interaktif  
    – Tampilan pink pastel & aesthetic

    Dibangun dengan:
    – Python 🐍  
    – Streamlit 🚀  
    – SymPy & Matplotlib 📊

    _“Math feels easier when it’s pretty! especially when there’s Jaehyun”_ 💅✨
    """)


# --- Menu Tabs + Logout Sidebar ---
def menu_tabs():
    tab1, tab2 = st.tabs(["🧮 Kalkulator", "🦩 Tentang"])
    with tab1:
        kalkulator()
    with tab2:
        about()

    # Logout Sidebar (benar indentasinya!)
    st.sidebar.markdown("## 🚪 Logout")
    if st.sidebar.button("Logout ✨"):
        st.session_state.login = False
        st.session_state.user = ""
        st.rerun()

# --- App Routing ---
if st.session_state.login:
    st.markdown(f"<div style='text-align:right;'>👑 Logged in as: <b>{st.session_state.user}</b></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 36px;'>🧁✨ kalkulator kalkulus ✨🧁</h1>", unsafe_allow_html=True)
    menu_tabs()
else:
    login_form()
