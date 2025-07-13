import streamlit as st
from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
from sympy.abc import x
import hashlib

# --- Load Custom CSS ---
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Session & Auth ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

user_db = {
    "bila": hash_password("pink123")
}

if "login" not in st.session_state:
    st.session_state.login = False
if "user" not in st.session_state:
    st.session_state.user = ""

def login_form():
    st.markdown("## 💗 Login Dulu Yuk 💗")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login 🩷"):
        if username in user_db and user_db[username] == hash_password(password):
            st.success("Login berhasil, hai " + username + "!")
            st.session_state.login = True
            st.session_state.user = username
        else:
            st.error("Username / Password salah!")

# --- Kalkulator Halaman ---
def kalkulator_page():
    st.markdown("## 🧮 Kalkulator Integral & Turunan 🧮")
    fungsi_input = st.text_input("📝 Masukkan fungsi (contoh: x**2 + 2*x + 1)", value="x**2 + 2*x + 1")
    operasi = st.radio("📌 Pilih operasi yang ingin dilakukan:", ["Turunan", "Integral"])
    x_vals = np.linspace(-10, 10, 400)

    if fungsi_input:
        try:
            fungsi = sympify(fungsi_input)
            f_numeric = lambdify(x, fungsi, modules=["numpy"])
            y_asli = f_numeric(x_vals)

            if operasi == "Turunan":
                turunan = diff(fungsi, x)
                t_numeric = lambdify(x, turunan, modules=["numpy"])
                y_turun = t_numeric(x_vals)

                st.subheader("🧠 Hasil Turunan:")
                st.latex(f"\\frac{{d}}{{dx}}\\left({str(fungsi)}\\right) = {str(turunan)}")

                st.subheader("📈 Grafik Fungsi & Turunannya:")
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_asli, label="f(x)", color="#ff69b4")
                ax.plot(x_vals, y_turun, label="f'(x)", color="#d63384", linestyle="--")
                ax.legend()
                ax.grid(True)
                st.pyplot(fig)

            elif operasi == "Integral":
                integral = integrate(fungsi, x)
                st.subheader("🧠 Hasil Integral Tak Tentu:")
                st.latex(f"\\int {str(fungsi)}\,dx = {str(integral)} + C")

                st.subheader("📈 Grafik Fungsi:")
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_asli, label="f(x)", color="#ff69b4")
                ax.legend()
                ax.grid(True)
                st.pyplot(fig)

        except Exception:
            st.error("⚠️ Fungsi tidak valid. Gunakan notasi Python, contoh: x**2 + 3*x")

# --- Profil Halaman ---
def profile_page():
    st.markdown("## 👩🏻‍💻 Tentang Aplikasi")
    st.write("""
        Aplikasi ini dibuat oleh **Nabila Rahmadani** dari kelas **TI.24.C.1** untuk UAS Matematika Terapan.  
        Dibuat dengan cinta menggunakan Python dan Streamlit 💕  
        Tema: Pink-Girly ✨
    """)
    st.image("https://i.pinimg.com/564x/87/e4/53/87e453bd5809f672a6c3654a515ad91e.jpg", width=300)

# --- Menu Utama ---
def main_menu():
    menu = st.sidebar.radio("📋 Menu", ["🧮 Kalkulator", "👩🏻‍💻 Tentang", "🚪 Logout"])
    if menu == "🧮 Kalkulator":
        kalkulator_page()
    elif menu == "👩🏻‍💻 Tentang":
        profile_page()
    elif menu == "🚪 Logout":
        st.session_state.login = False
        st.session_state.user = ""
        st.experimental_rerun()

# --- App Routing ---
if st.session_state.login:
    st.sidebar.markdown(f"👤 Logged in as: `{st.session_state.user}`")
    main_menu()
else:
    login_form()

st.markdown("<div class='footer'>UAS Matematika Terapan 2025 💗 Nabila Rahmadani</div>", unsafe_allow_html=True)
