Nama : Chelsea Stania Passikha

NPM : 2506587876

Kelas : PBP F

### Tugas 1

1. Pada tugas ini, saya tidak menambahkan elemen semantik HTML baru, namun saya menggunakan elemen <section> yang sudah tersedia dari tutorial 1. Elemen tersebut membantu dalam membuat web dengan mengelompokkan elemen di dalamnya. Akibatnya, elemen-elemen tersebut dapat diletakkan di sisi kiri foto.
2. Saat menambahkan elemen baru, saya merasa kesulitan mengatur layout dari grid dan teksnya. Misalnya, pada awal, menurut saya gridnya terletak terlalu dekat dengan bagian links.
Untuk mengevaluasi elemen yang perlu diubah, saya melihat apakah elemen tersebut tetap mudah dibaca saat berpindah ke elemen mobile.
3. Batasan yang saya rasakan adalah kurangnya elemen interaktif, sehingga penyajian informasi kurang menarik. Fungsionalitas dinamis yang ingin saya tambahkan pada iterasi proyek selanjutnya adalah fitur interaktif seperti sebuah kolom komentar.

Saya tidak menggunakan AI.
Refleksi: Saat membuat section baru, saya dapat memilih antara flexbox dan grid. Saya memilih untuk menggunakan grid karena lebih mudah untuk disesuaikan dengan tampilan browser. Saya menghadapi masalah saat membuatnya karena saya belum sepenuhnya memahami cara mengedit grid. Agar saya lebih mengerti penggunaan grid, saya mencari tutorial pada situs Youtube.


### Tugas 2
1. Ketika pengguna membuka halaman portofolio, permintaan diterima urls.py proyek. Kemudian, permintaan tersebut dapat dikirimkan ke urls.py aplikasi. Aplikasi menyesuaikan url dengan views.py, yang berperan dalam mengambil data dari model. Setelah itu, data tersebut diterima oleh template dan ditampilkan pada browser.
2. Data sebaiknya disimpan pada model agar data tersebut terpisah dari template yang mengatur tampilan. Akibatnya, data dapat diubah atau dihapus dengan mudah, tanpa perlu mengganti layout yang terdapat pada template.
3. Fungsi makemigrations bertujuan untuk mendeteksi perubahan saat mengubah model, sedangkan fungsi migrate bertujuan untuk menmperbarui database agar perubahan tersebut tersimpan. Saat mengerjakan tugas ini, saya harus menjalankan kedua perintah tersebut ketika membuat class Education.

AI Declaration: Saya menggunakan AI dengan platform ChatGPT saat mengerjakan tugas ini. Bagian yang dibantu adalah pembuatan class baru pada models.py.

Log AI: https://chatgpt.com/share/6aa8143e-3ae8-83ec-a023-33fe65401a5e

### Tugas 3
1. ModelForm digunakan agar field dari model langsung terintergrasi dengan form. Akibatnya, kode yang perlu ditulis berkurang.

{% csrf_token %} harus ditambahkan untuk mengurangi risiko Cross Site Request Forgery (CSRF). CSRF adalah serangan yang terjadi ketika server menerima request yang kelihatannya berasal dari pengguna, namun sebenarnya berasal dari sumber lain seperti website berbahaya.

2. JSON memiliki struktur yang lebih ringkas dibandingkan XML. Selain itu, JSON lebih cocok digunakan dengan JavaScript karena strukturnya yang serupa.

3. Saat view dijalankan, view mengambil data dari database. Data tersebut belum berupa JSON ketika diambil. Jadi, data tersebut diubah menjadi JSON dengan serialization. Serialization perlu terjadi sebelum data dikembalikan agar data tersebut dapat disajikan dalam format yang diperlukan sistem.

AI declaration: Saya tidak menggunakan AI.
Refleksi: Saat membuat class dan form baru, saya mendapatkan beberapa error. Ketika mendapatkan error tersebut, saya dapat menyelesaikannya dengan mencari solusi di Stack Overflow dan situs serupa.