import streamlit as st
from PIL import Image
from model import load_model, predict_image
import io
import logging

# Konfigurasi halaman
st.set_page_config(
    page_title="Daun Kapas"
)

# Judul dan deskripsi aplikasi
st.title("Aplikasi Klasifikasi Daun Kapas")
st.write('Selamat Datang di Aplikasi Klasifikasi Daun Kapas, Muat gambar daun kapas untuk klasifikasi penyakitnya.')

# Menambahkan gambar
intro_image = Image.open("images/Cotton.jpg")  # Ganti dengan path gambar yang ingin ditambahkan
st.image(intro_image, caption='Contoh Gambar Daun Kapas', use_column_width=True)

# Menambahkan kredit gambar
st.write("Image by Rajesh Ram")

st.sidebar.success("You're At Homepage Now")

# Load model
model = load_model()

# Upload gambar
uploaded_file = st.file_uploader("Pilih gambar daun kapas...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Tampilkan gambar yang diunggah
    image = Image.open(uploaded_file)

     # Konversi PNG ke JPG jika format asli adalah PNG
    if uploaded_file.type == 'image/png':
        logging.info("Converting PNG to JPG")
        image = image.convert('RGB')
        with io.BytesIO() as output:
            image.save(output, format="JPEG")
            image = Image.open(io.BytesIO(output.getvalue()))

    st.image(image, caption='Gambar yang diunggah', use_column_width=True)
    
    # Tombol prediksi
    if st.button('Prediksi'):
        # Placeholder untuk proses prediksi
        st.write('Memproses...')
        
        # Prediksi
        label = predict_image(model, image)
        
        # Tampilkan hasil prediksi
        if label == 0:
            st.write("Klasifikasi: Bacterial Blight")
            st.write("""
            **Bacterial Blight** adalah penyakit yang disebabkan oleh bakteri _Xanthomonas campestris_. Gejala utamanya meliputi bercak hitam pada daun yang dapat membesar dan mengakibatkan kerusakan jaringan. Pencegahan melibatkan penggunaan bibit yang sehat dan pengendalian bakteri dengan fungisida atau antibiotik.
            """)
        elif label == 1:
            st.write("Klasifikasi: Curl Virus")
            st.write("""
            **Curl Virus** adalah penyakit yang disebabkan oleh virus yang menginfeksi daun kapas dan menyebabkan daunnya menggulung. Gejala ini biasanya disertai dengan pertumbuhan kerdil dan penurunan hasil. Pengendalian melibatkan pengendalian vektor dan penggunaan varietas tahan virus.
            """)
        elif label == 2:
            st.write("Klasifikasi: Fusarium Wilt")
            st.write("""
            **Fusarium Wilt** disebabkan oleh jamur _Fusarium oxysporum_, yang menyerang sistem perakaran dan menyebabkan layu pada tanaman. Gejala utama termasuk layu daun yang progresif dan kekuningan. Pencegahan melibatkan rotasi tanaman dan penggunaan varietas tahan.
            """)
        elif label == 3:
            st.write("Klasifikasi: Healthy")
            st.write("""
            **Sehat** berarti daun kapas Anda dalam kondisi baik dan tidak menunjukkan gejala penyakit. Tetap perhatikan kesehatan tanaman dengan pemeliharaan yang baik dan pencegahan penyakit untuk memastikan hasil panen yang optimal.
            """)

