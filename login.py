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
    st.markdown("""
        <h2 style='text-align:center;'> Hallo, Selamat Datang! </h2>
        <p style='text-align:center;'>Silakan masuk ke <b>Cute Calculus App</b> untuk memulai perhitunganmu!</p>
    """, unsafe_allow_html=True)

    # Tambahkan siluet icon pink di tengah
    st.markdown("""
    <div style='text-align: center;'>
        <img src='https://cdn-icons-png.flaticon.com/512/847/847969.png' width='80'>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("👑 Username")
    password = st.text_input("🔒 Password", type="password") 
        
    st.markdown("### 🖼️ Silakan upload gambar siluetmu (opsional)")
    uploaded_avatar = st.file_uploader("Upload gambar (PNG/JPG)", type=["png", "jpg", "jpeg"])

    if uploaded_avatar:
        st.image(uploaded_avatar, width=100, caption="Siluet kamu 💖")


    if st.button("✨ Login"):
        if username in user_db and user_db[username] == hash_password(password):
            st.success(f"Welcome back, {username}!✨💄🧁  You're fabulous!")
            st.session_state.login = True
            st.session_state.user = username
        else:
            st.error("Ooops... Username atau password salah, coba cek lagi yaa")
