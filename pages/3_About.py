import streamlit as st

st.title("Tentang Aplikasi")
st.write("""
Aplikasi ini dirancang untuk kebutuhan penulisan ilmiah dan bertujuan untuk membantu dalam klasifikasi penyakit daun kapas. 
Aplikasi ini menggunakan model pembelajaran mendalam yang telah dilatih untuk mengenali berbagai penyakit pada daun kapas berdasarkan gambar yang diunggah oleh pengguna.

**Fitur Utama:**
- **Klasifikasi Penyakit Daun Kapas**: Aplikasi ini mampu mengklasifikasikan empat kategori utama penyakit daun kapas:
  1. Bacterial Blight
  2. Curl Virus
  3. Fusarium Wilt
  4. Healthy

- **Deskripsi Penyakit**: Aplikasi ini juga menyediakan deskripsi rinci mengenai setiap penyakit, termasuk penyebab, gejala, dan metode pengendalian.

**Cara Menggunakan Aplikasi:**
1. **Halaman Utama**: 
   - Muat gambar daun kapas melalui fungsi unggah gambar.
   - Aplikasi akan memproses gambar dan memberikan prediksi mengenai penyakit yang mungkin ada pada daun tersebut.
   - Deskripsi singkat mengenai penyakit yang terdeteksi akan ditampilkan.

2. **Halaman Deskripsi**:
   - Pengguna dapat membaca deskripsi lebih rinci mengenai setiap penyakit.
   - Deskripsi termasuk gambar contoh, penyebab, gejala, dan metode pengendalian.

**Informasi Tambahan:**
- **Ferdiansyah Haryadi**
- **Universitas Gunadarma**

Untuk informasi lebih lanjut, kunjungi tautan di bawah ini:

Kunjungi GitHub: [https://github.com/Frdyan](https://github.com/Frdyan)

Dataset Daun Kapas: [https://www.kaggle.com/datasets/seroshkarim/cotton-leaf-disease-dataset](https://www.kaggle.com/datasets/seroshkarim/cotton-leaf-disease-dataset)
""")

st.sidebar.success("You're At About Page Now")
