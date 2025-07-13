import streamlit as st
from sympy import symbols, diff, integrate, limit, sympify
from sympy.abc import x, y

# --- Sidebar & Header ---
st.sidebar.title("⚙️ Menu Kalkulus")
menu = st.sidebar.radio("Pilih jenis operasi:", ["Turunan", "Integral", "Limit", "Turunan Parsial"])

st.title("🧮 Smart Kalkulus Calculator")
st.markdown("Selamat datang di Kalkulator Kalkulus berbasis Python dan Streamlit.\
            Silakan pilih jenis operasi di sidebar dan masukkan fungsi matematikamu di bawah.")

# --- Input Fungsi Umum ---
fungsi_input = st.text_input("📝 Masukkan fungsi matematika (contoh: x**2 + 3*x + 1)", value="x**2 + 3*x + 1")

# --- Operasi: TURUNAN ---
if menu == "Turunan":
    st.info("🔍 Menghitung turunan pertama dari fungsi terhadap x.")
    try:
        fungsi = sympify(fungsi_input)
        hasil = diff(fungsi, x)
        st.latex(f"\\frac{{d}}{{dx}}\\left({str(fungsi)}\\right) = {str(hasil)}")
    except Exception as e:
        st.error("❗ Fungsi tidak valid. Gunakan notasi Python, contoh: x**2 + 3*x")

# --- Operasi: INTEGRAL ---
elif menu == "Integral":
    st.info("🧮 Menghitung integral tak tentu dari fungsi terhadap x.")
    try:
        fungsi = sympify(fungsi_input)
        hasil = integrate(fungsi, x)
        st.latex(f"\\int {str(fungsi)}\,dx = {str(hasil)} + C")
    except Exception:
        st.error("❗ Fungsi tidak valid. Gunakan notasi Python.")

# --- Operasi: LIMIT ---
elif menu == "Limit":
    st.info("📉 Menghitung limit fungsi terhadap x.")
    titik = st.number_input("Masukkan titik limit (contoh: 0):", value=0.0)
    arah = st.radio("Arah limit:", ["Kiri (-)", "Kanan (+)", "Tidak ditentukan"])
    try:
        fungsi = sympify(fungsi_input)
        if arah == "Kiri (-)":
            hasil = limit(fungsi, x, titik, dir='-')
        elif arah == "Kanan (+)":
            hasil = limit(fungsi, x, titik, dir='+')
        else:
            hasil = limit(fungsi, x, titik)
        st.latex(f"\\lim_{{x \\to {titik}}} {str(fungsi)} = {str(hasil)}")
    except:
        st.error("❗ Input limit tidak valid.")

# --- Operasi: TURUNAN PARSIAL ---
elif menu == "Turunan Parsial":
    st.info("🔢 Menghitung turunan parsial terhadap x dan y.")
    try:
        fungsi = sympify(fungsi_input)
        dx = diff(fungsi, x)
        dy = diff(fungsi, y)
        st.latex(f"\\frac{{\\partial}}{{\\partial x}}\\left({str(fungsi)}\\right) = {str(dx)}")
        st.latex(f"\\frac{{\\partial}}{{\\partial y}}\\left({str(fungsi)}\\right) = {str(dy)}")
    except:
        st.error("❗ Fungsi tidak valid. Contoh input: x**2*y + y**2")

# --- Footer ---
st.markdown("---")
st.caption("Dibuat oleh Nabila Rahmadani | TI.24.C1 | Universitas Pelita Bangsa")
