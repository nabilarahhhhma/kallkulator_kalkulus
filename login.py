import streamlit as st
import hashlib

# --- Hash password ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- User database dummy ---
user_db = {
    "bila": hash_password("cantik")
}

# --- Login Form ---
def login_form():
    st.markdown("<h2>🎀 Hallo, Selamat Datang! 🎀</h2>", unsafe_allow_html=True)
    username = st.text_input("👑 Username")
    password = st.text_input("🔒 Password", type="password")
    if st.button("✨ Login"):
        if username in user_db and user_db[username] == hash_password(password):
            st.success(f"Welcome back, {username}!✨💄🧁  You're fabulous!")
            st.session_state.login = True
            st.session_state.user = username
        else:
            st.error("Ooops... Username atau password salah, coba cek lagi yaa")
