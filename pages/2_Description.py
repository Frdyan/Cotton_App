import streamlit as st
from PIL import Image

def show_disease_info(disease_name, description, image_path):
    st.subheader(disease_name)
    st.write(description)
    st.image(image_path, use_column_width=True)

st.title("Deskripsi Penyakit")
st.sidebar.success("You're At Description Page Now")

# Deskripsi penyakit dengan gambar
show_disease_info(
    'Bacterial Blight',
    '''
    **Bacterial Blight** adalah penyakit yang disebabkan oleh bakteri *Xanthomonas citri pv. malvacearum*. 
    Penyakit ini sering kali mengakibatkan bercak-bercak hitam pada daun, batang, dan buah kapas. Gejala pada daun dapat berupa bercak berbentuk bulat yang berkembang menjadi bercak yang lebih besar dengan tepi hitam yang jelas. 
    Infeksi dapat menyebar melalui air hujan, angin, dan kontak fisik antar tanaman. Bakteri ini dapat mempengaruhi kualitas dan kuantitas hasil kapas, mengakibatkan penurunan hasil panen secara signifikan.
    
    **Pencegahan dan Pengendalian**: Untuk mengendalikan Bacterial Blight, penting untuk menggunakan bibit yang sehat dan melakukan pemangkasan bagian tanaman yang terinfeksi. Penggunaan fungisida berbasis tembaga atau antibiotik juga dapat membantu mengendalikan penyebaran bakteri. Selain itu, pengaturan jarak tanam yang baik dan pengelolaan kelembaban dapat mengurangi risiko infeksi.
    ''',
    'images/Bacterial_Blight.jpg'
)

show_disease_info(
    'Curl Virus',
    '''
    **Curl Virus** adalah penyakit yang disebabkan oleh virus geminivirus, yang ditularkan oleh kutu kebul (whitefly). Gejala utama dari penyakit ini termasuk daun yang menggulung dan menguning secara tidak merata. Daun yang terinfeksi biasanya menunjukkan pertumbuhan yang terhambat dan pertumbuhan tanaman yang terhambat secara keseluruhan. Infeksi parah dapat mengakibatkan penurunan hasil panen yang signifikan.

    **Pencegahan dan Pengendalian**: Pencegahan infeksi Curl Virus dapat dilakukan dengan mengendalikan populasi kutu kebul melalui aplikasi pestisida yang sesuai dan pemantauan rutin. Selain itu, penanaman varietas kapas yang tahan terhadap virus juga dapat mengurangi risiko infeksi. Penting untuk menjaga kebersihan kebun dan menghilangkan tanaman yang terinfeksi untuk mencegah penyebaran virus lebih lanjut.
    ''',
    'images/Curl_Virus.jpg'
)

show_disease_info(
    'Fusarium Wilt',
    '''
    **Fusarium Wilt** disebabkan oleh jamur *Fusarium oxysporum* yang menyerang sistem vaskular tanaman kapas. Gejala dari penyakit ini termasuk layu mendadak pada daun yang biasanya dimulai dari bagian bawah tanaman dan menyebar ke bagian atas. Daun yang terkena biasanya menguning, kering, dan akhirnya mati. Tanaman yang terinfeksi dapat menunjukkan pertumbuhan yang terhambat dan penurunan hasil panen yang signifikan.

    **Pencegahan dan Pengendalian**: Pengendalian Fusarium Wilt melibatkan beberapa langkah penting, seperti rotasi tanaman dengan spesies non-rentan untuk mengurangi keberadaan jamur di tanah. Penggunaan varietas kapas yang tahan terhadap Fusarium juga dapat membantu mengurangi dampak penyakit. Selain itu, menjaga kondisi tanah yang baik dan menghindari genangan air juga dapat mengurangi risiko infeksi.
    ''',
    'images/Fussarium_Wilt.jpg'
)

show_disease_info(
    'Healthy',
    '''
    **Sehat** merujuk pada daun kapas yang dalam kondisi optimal tanpa menunjukkan gejala penyakit. Daun sehat biasanya memiliki warna hijau cerah, tidak ada bercak atau perubahan warna, dan tidak menunjukkan tanda-tanda penggulingan atau pertumbuhan abnormal. Tanaman kapas yang sehat menunjukkan pertumbuhan yang baik dan berproduksi dengan hasil yang optimal.

    **Pemeliharaan**: Untuk mempertahankan kesehatan tanaman kapas, penting untuk melakukan pemeliharaan yang baik termasuk penyiraman yang cukup, pemupukan yang tepat, dan pengendalian hama serta penyakit secara rutin. Juga, pastikan untuk mengelola lingkungan tanaman dengan baik untuk mencegah kondisi yang dapat mendukung pertumbuhan patogen.
    ''',
    'images/Healthy.jpg'
)
