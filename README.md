# Burhan Shop — Football Shop

No. 1 Football Shop in FASILKOM UI

### 🪁 Deployment 
Click Here: [Burhan Shop](https://malik-alifan-burhanshop.pbp.cs.ui.ac.id/)

### 📚 Assignment Archive
* [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-2:-Implementasi-Model%E2%80%90View%E2%80%90Template-(MVT)-pada-Django)
* [Tugas 3: Implementasi Form dan Data Delivery pada Django](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-3:-Implementasi-Form-dan-Data-Delivery-pada-Django)


***

## Tugas 3: Implementasi Form dan Data Delivery pada Django

### Langkah - langkah implementasi
1. Membuat file `base.html` sebagai template dasar untuk menjaga konsistensi tampilan dan menghindari pengulangan kode
2. Menyiapkan form input data barang (`forms.py`) agar pengguna dapat menambahkan konten baru ke dalam aplikasi melalui halaman web.
3. Mengambil semua data produk dari database dan menampilkannya di halaman utama. Setiap produk memiliki tombol "Read More" untuk melihat detail lengkapnya di halaman terpisah (`product_detail`).
4. Membuat fungsi dan URL khusus untuk mengubah data produk dari database menjadi format XML dan JSON (`show_xml` dan `show_json`). 
5. Menambahkan fungsi untuk mengambil dan menampilkan satu data produk spesifik dalam format XML atau JSON berdasarkan ID uniknya (`show_xml_by_id` dan `show_json_by_id`).
6. Membuat routing url dengan menambahkan 4 path fungsi pada `urls.py` di direktori `main`. 


### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena data yang disediakan backend tidak hanya digunakan oleh satu interface saja, melainkan harus bisa diakses oleh berbagai macam klien seperti web, mobile, atau layanan pihak ketiga. Dengan adanya data delivery menggunakan format standar seperti JSON atau XML, platform menjadi lebih fleksibel serta mudah diintegrasikan. Selain itu, data delivery memungkinkan pemisahan antara logika bisnis dan tampilan, sehingga kode lebih rapi dan mudah dimaintain. Dari sisi pengembangan, mekanisme ini juga memudahkan proses debugging, pengujian dengan tools seperti Postman, serta mendukung skalabilitas melalui caching, pagination, atau filtering.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik dibandingkan XML terutama dalam konteks pengembangan web modern karena formatnya lebih ringkas, mudah dibaca manusia, dan langsung dapat diproses oleh JavaScript tanpa perlu parsing yang rumit. JSON juga menggunakan struktur data berupa objek dan array yang sangat sesuai dengan gaya pemrograman berorientasi objek maupun pemrograman berbasis data saat ini. Di sisi lain, XML memang memiliki kelebihan seperti dukungan untuk skema dan validasi data yang lebih kompleks, tetapi kelemahannya adalah banyak tag pembuka dan penutup sehingga ukuran data menjadi lebih besar dan sulit dibaca.

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dikirim melalui form sudah sesuai dengan aturan validasi yang didefinisikan, baik dari sisi tipe data, panjang input, maupun constraint lain. Kita membutuhkan method ini agar data yang masuk ke database terjamin kebersihannya, mencegah error, serta menghindari potensi celah keamanan akibat input yang tidak valid.

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan `csrf_token` karena ia mencegah serangan CSRF (Cross-Site Request Forgery) yaitu ketika penyerang membuat halaman/skrip di domain lain yang secara otomatis mengirim permintaan (misal POST) ke situs kita memakai kredensial korban (cookie/session) sehingga korban tanpa sadar melakukan aksi seperti mengubah data atau transaksi; tanpa `csrf_token` server tidak bisa membedakan permintaan sah dari permintaan palsu. `csrf_token` bekerja sebagai nilai acak yang diikat ke sesi/ cookie dan harus dikirim ulang di form (hidden input) atau header; server memverifikasi kecocokan token itu sebelum memproses aksi yang mengubah state.

### Feedback Asdos
Asdos sangat membantu ketika selama berjalannya tutorial. Asdos mampu menjawab semua pertanyaan yang saya miliki dan sangat membantu ketika terjadi error di kode saya.

### Screenshot Hasil Akses URL pada Postman

XML & JSON
[![XML](https://i.gyazo.com/f636de9bdcd585f7a0e49935bbceb0b9.png)](https://gyazo.com/f636de9bdcd585f7a0e49935bbceb0b9)

[![JSON](https://i.gyazo.com/833ac3864409e1ac2e056c3206fc27e6.png)](https://gyazo.com/833ac3864409e1ac2e056c3206fc27e6)

XML & JSON by ID
[![XML by ID](https://i.gyazo.com/021f759548ffcf805c88e05c5f7fd29b.png)](https://gyazo.com/021f759548ffcf805c88e05c5f7fd29b)

[![JSON by ID](https://i.gyazo.com/a8697f4ff404fe1ec202a613943b7efb.png)](https://gyazo.com/a8697f4ff404fe1ec202a613943b7efb)