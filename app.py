import streamlit as st
from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
from sympy.abc import x
import hashlib

# --- PINK STYLE ---
st.markdown("""
    <style>
    .main {
        background-color: #ffe6f0;
    }
    .stApp {
        font-family: 'Comic Sans MS', cursive;
    }
    .title {
        color: #d63384;
        text-align: center;
    }
    .footer {
        font-size: 12px;
        color: #888;
        text-align: center;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# --- User auth (simple) ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Akun dummy
user_db = {
    "bila": hash_password("pink123")
}

# --- Session state init ---
if "login" not in st.session_state:
    st.session_state.login = False
if "user" not in st.session_state:
    st.session_state.user = ""

# --- Login Form ---
def login_form():
    st.markdown("<h2 class='title'>🎀 Login Dulu Yuk 🎀</h2>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login 🩷"):
        if username in user_db and user_db[username] == hash_password(password):
            st.success("Login berhasil, hai " + username + "!")
            st.session_state.login = True
            st.session_state.user = username
        else:
            st.error("Username / Password salah!")

# --- Halaman Kalkulator ---
def kalkulator_page():
    st.markdown("<h1 class='title'>🧮 Kalkulator Integral & Turunan 🧮</h1>", unsafe_allow_html=True)
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
                st.latex(f"\\int {str(fungsi)}\\,dx = {str(integral)} + C")

                st.subheader("📈 Grafik Fungsi:")
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_asli, label="f(x)", color="#ff69b4")
                ax.legend()
                ax.grid(True)
                st.pyplot(fig)

        except Exception:
            st.error("⚠️ Fungsi tidak valid. Gunakan notasi Python, contoh: x**2 + 3*x")

# --- Halaman Profil ---
def profile_page():
    st.markdown("<h2 class='title'>👩🏻‍💻 Tentang Aplikasi</h2>", unsafe_allow_html=True)
    st.write("""
        Aplikasi ini dibuat oleh **Nabila Rahmadani** dari kelas **TI.24.C.1** sebagai proyek UAS Matematika Terapan.  
        Dikembangkan dengan Python + Streamlit dengan tema pink-girly 💕  
        Fitur utama: Kalkulasi integral dan turunan dengan tampilan grafik dan simbolik.
    """)
    st.image("https://i.pinimg.com/564x/9d/31/98/9d3198bfb65c0f56e4a2d7f8fcd6a37a.jpg", width=250)

# --- Halaman Menu ---
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

# --- Footer ---
st.markdown("<div class='footer'>UAS Matematika Terapan 2025 💗 Nabila Rahmadani</div>", unsafe_allow_html=True)
