import streamlit as st
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

user_db = {
    "bila": hash_password("cantik")
}

def login_form():
    st.markdown("""
    <div style='text-align: center;'>
        <img src='https://cdn-icons-png.flaticon.com/512/847/847969.png' width='80'>
    </div>
    <h2 style='text-align:center;'>🎀 Hallo, Selamat Datang! 🎀</h2>
    <p style='text-align:center;'>Silakan masuk ke <b>Cute Calculus App</b> untuk memulai perhitunganmu!</p>
    """, unsafe_allow_html=True)

    username = st.text_input("👑 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("✨ Login"):
        if username in user_db and user_db[username] == hash_password(password):
            st.success(f"Welcome back, {username}!✨💄🧁  You're fabulous!")
            st.session_state.login = True
            st.session_state.user = username
        else:
            st.error("Ooops... Username atau password salah, coba cek lagi yaa")
