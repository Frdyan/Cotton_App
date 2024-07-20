import streamlit as st

st.title("Tentang Kami")
st.write("""
Selamat datang di halaman Tentang Kami! 
Untuk informasi lebih lanjut, kunjungi GitHub kami dengan mengklik tautan di bawah ini.
""")
st.sidebar.success("You're At About Us Page Now")

# Tombol untuk membuka halaman GitHub
if st.button('Kunjungi GitHub'):
    st.write("Mengalihkan ke GitHub...")
    js = "window.open('https://github.com/Frdyan')" 
    html = '<script>{}</script>'.format(js)
    st.markdown(html, unsafe_allow_html=True)

# Tombol untuk membuka halaman GitHub
# st.markdown("[Kunjungi GitHub](https://github.com/USERNAME)", unsafe_allow_html=True)