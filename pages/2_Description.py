import streamlit as st

# Fungsi untuk menampilkan deskripsi penyakit dengan gambar
def show_disease_info(title, description, image_path):
    st.subheader(title)
    st.write(description)
    st.image(image_path, use_column_width=True)

st.title("Deskripsi Penyakit")
st.sidebar.success("You're At Description Page Now")

# Deskripsi penyakit dengan gambar
show_disease_info(
    'Bacterial Blight',
    'Penyakit ini disebabkan oleh bakteri *Xanthomonas citri pv. malvacearum* yang menyebabkan bercak-bercak hitam pada daun, batang, dan buah kapas. Bakteri ini dapat menyebar melalui air hujan dan angin, serta mempengaruhi kualitas dan kuantitas hasil kapas.',
    'images/Bacterial_Blight.jpg'
)

show_disease_info(
    'Curl Virus',
    'Penyakit ini disebabkan oleh virus geminivirus yang ditularkan oleh kutu kebul (whitefly). Gejala utamanya adalah daun yang menggulung dan menguning, serta pertumbuhan tanaman yang terhambat. Infeksi parah dapat menyebabkan kerugian hasil yang signifikan.',
    'images/Curl_Virus.jpg'
)

show_disease_info(
    'Fusarium Wilt',
    'Penyakit ini disebabkan oleh jamur *Fusarium oxysporum* yang menyerang sistem vaskular tanaman. Gejalanya termasuk layu mendadak, daun yang menguning, dan kematian tanaman. Jamur ini dapat bertahan dalam tanah selama bertahun-tahun dan sulit untuk dikendalikan.',
    'images/Fussarium_Wilt.jpg'
)

show_disease_info(
    'Healthy',
    'Kategori ini merujuk pada daun kapas yang sehat tanpa gejala penyakit. Daun sehat berwarna hijau cerah, tidak ada bercak, tidak menggulung, dan tanaman tumbuh dengan normal tanpa hambatan.',
    'images/Healthy.jpg'
)