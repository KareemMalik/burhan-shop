# Burhan Shop — Football Shop

No. 1 Football Shop in FASILKOM UI

### 🪁 Deployment
Click Here: [Burhan Shop](https://malik-alifan-burhanshop.pbp.cs.ui.ac.id/)

### 📚 Assignment Archive
* [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-2:-Implementasi-Model%E2%80%90View%E2%80%90Template-(MVT)-pada-Django)
* [Tugas 3: Implementasi Form dan Data Delivery pada Django](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-3:-Implementasi-Form-dan-Data-Delivery-pada-Django)
* [Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-4:-Implementasi-Autentikasi,-Session,-dan-Cookies-pada-Django)
* [Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-5:-Desain-Web-menggunakan-HTML,-CSS-dan-Framework-CSS)
* [Tugas 6: Javascript dan AJAX](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-6:-Javascript-dan-AJAX)


***

## Tugas 6: Javascript dan AJAX

### Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous request adalah permintaan dari client ke server yang diproses secara berurutan, artinya client harus menunggu hingga server selesai memproses dan mengembalikan respons sebelum dapat melanjutkan proses lainnya. Dalam konteks web, permintaan sinkron biasanya menyebabkan halaman web melakukan reload penuh setiap kali data dikirim, seperti pada form HTML tradisional. Sebaliknya, asynchronous request adalah permintaan yang dikirim ke server tanpa menghentikan aktivitas lain di sisi client. Proses ini memungkinkan halaman tetap interaktif karena JavaScript dapat mengirim dan menerima data di latar belakang melalui teknologi seperti AJAX atau Fetch API tanpa melakukan reload halaman. Dengan asynchronous request, user dapat melihat perubahan data secara langsung (misalnya menampilkan notifikasi sukses atau memperbarui elemen halaman) tanpa menunggu seluruh halaman dimuat ulang. Secara sederhana, synchronous membuat proses lebih lambat dan kaku karena menunggu respons penuh dari server, sedangkan asynchronous membuat interaksi web lebih cepat, dinamis, dan responsif.

###  Bagaimana AJAX bekerja di Django (alur request–response)?
AJAX (Asynchronous JavaScript and XML) bekerja di Django sebagai jembatan komunikasi antara browser dan server yang memungkinkan pembaruan data pada halaman web tanpa perlu melakukan reload secara keseluruhan. Prosesnya diawali oleh aksi pengguna di browser, seperti mengklik tombol, yang memicu fungsi JavaScript. Fungsi ini kemudian mengirimkan sebuah HTTP request secara asinkron ke URL spesifik yang telah disiapkan di urls.py Django. Request ini dapat membawa data dan wajib menyertakan CSRF token untuk keamanan saat menggunakan metode POST. Di sisi server, Django akan mengarahkan request tersebut ke sebuah view yang telah ditunjuk. Berbeda dengan view biasa yang merender template HTML, view untuk AJAX ini akan memproses logika yang dibutuhkan misalnya mengambil atau mengubah data di database lalu mengemas hasilnya ke dalam format data, umumnya menggunakan JsonResponse untuk mengirimkan objek JSON. Setelah response JSON ini diterima kembali oleh JavaScript di browser, skrip tersebut akan mengolah data yang ada di dalamnya untuk memanipulasi DOM (Document Object Model) secara langsung, seperti mengubah teks, mengganti gambar, atau menampilkan notifikasi. 

### Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Keuntungan utama menggunakan AJAX dibandingkan render biasa di Django adalah untuk menciptakan User Experience (UX) yang jauh lebih cepat, mulus, dan interaktif, mirip seperti menggunakan aplikasi desktop.

Render biasa mengharuskan browser memuat ulang seluruh halaman setiap kali ada permintaan data baru, yang terasa lambat dan mengganggu. Sebaliknya, AJAX hanya meminta dan memperbarui bagian-bagian kecil dari halaman yang diperlukan tanpa reload.


###  Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Untuk mengamankan fitur login dan registrasi AJAX di Django, perlakukan endpoint Anda dengan keamanan setara halaman biasa. Wajibkan HTTPS untuk mengenkripsi semua data. Manfaatkan perlindungan CSRF bawaan Django dengan selalu mengirimkan token dalam header request AJAX Anda.

Di sisi server, lakukan validasi data yang sangat ketat menggunakan Django Forms atau Serializer untuk mencegah serangan seperti SQL Injection dan XSS. Terapkan juga Rate Limiting untuk membatasi jumlah percobaan login dari satu IP guna mencegah serangan brute-force. Terakhir, jangan pernah mengirim informasi sensitif seperti password dalam respons JSON; cukup kembalikan status berhasil atau gagal.


### Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX secara fundamental mengubah pengalaman pengguna (UX) dengan membuat website terasa jauh lebih cepat, responsif, dan interaktif. Dengan menghilangkan kebutuhan untuk memuat ulang seluruh halaman, AJAX memungkinkan pembaruan konten secara parsial di latar belakang, sehingga interaksi terasa instan dan tanpa gangguan. Hal ini memungkinkan fitur-fitur dinamis seperti live search, notifikasi real-time, dan validasi formulir yang mulus. Hasilnya, pengguna mendapatkan pengalaman yang lebih mirip aplikasi desktop yang hidup dan efisien daripada sekadar menavigasi halaman web statis.