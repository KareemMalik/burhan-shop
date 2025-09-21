# Burhan Shop — Football Shop

No. 1 Football Shop in FASILKOM UI

### 🪁 Deployment 
Click Here: [Burhan Shop](https://malik-alifan-burhanshop.pbp.cs.ui.ac.id/)

### 📚 Assignment Archive
* [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-2:-Implementasi-Model%E2%80%90View%E2%80%90Template-(MVT)-pada-Django)
* [Tugas 3: Implementasi Form dan Data Delivery pada Django](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-3:-Implementasi-Form-dan-Data-Delivery-pada-Django)
* [Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django]


***

## Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

### Langkah - langkah implementasi
**1. Membuat Fungsi dan Form untuk Registrasi**

Langkah pertama yang saya lakukan adalah mengimport library yang dibutuhkan kemudian membuat fungsi untuk melakukan registrasi. Library yang saya import antara lain 

```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
Lalu saya membuat tampilan (view) untuk registrasi dengan memanfaatkan `UserCreationForm`. Ketika permintaan POST masuk dan form valid program akan menyimpan user baru dan tampilkan pesan sukses kemudian pengguna diarahkan ke halaman login. Berikut ini merupakan potongan kode yang saya masukan.
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Setelah itu, saya membuat template `register.html` untuk merender form dan menggunakan `{% csrf_token %}` agar form terlindung dari serangan csrf. Saya juga mengimport fungsi `register` di atas ke `urls.py` dan menambahkan path url ke dalam `urlpatterns` agar fungsi yang sudah diimpor bisa di akses.

**2. Membuat Fungsi Login**

Selanjutnya disini saya kembali mengimport library-library di bawah ini. `AuthenticationForm` akan digunakan untuk melakukan validasi kredensial. Lalu saya juga mengimport fungsi-fungsi bawaan django yaitu `authenticate` dan `login` untuk melakukan autentikasi dan login. Setelah autentikasi berhasil, program akan memanggil fungsi `login` agar django membuat sesi login.
```
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
```
Lalu saya membuat fungsi `login_user` untuk autentikasi pengguna yang ingin login kemudian membuat file `login.html` untuk memberikan interface kepada pengguna yang ingin login. Sama seperti sebelumnya, saya kemudian mengimport fungsi `login_user` ke `urls.py` dan menambahkan path url ke dalam `urlpatterns`.

**3. Membuat Fungsi Logout**

Saya membuat fungsi `logout_user` agar pengguna yang sedang login dapat logout dari akun tersebut dan mengakhiri sesi loginnya. 
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Lalu, saya membuat tombol Logout di file `main.html`, melakukan impor pada fungsi ini pada `urls.py` dan menambahkan path url kedalam `urlpatterns`

**4. Membatasi Akses Halaman `main` dan `product detail`**

Agar hanya user yang sedang login yang dapat mengakses halaman `main` dan `product_detail`, saya melakukan import `login_requires` yang merupakan sistem autentikasi bawaan dari django. Untuk menggunakannya, saya menambahkan `@login_required(login_url='/login')` yang menampilkan `main` dan `product_detail` yaitu `show_main` dan `show_product`. Dengan menambahkan potongan kode tersebut, `main` dan `product_detail` hanya bisa di akses oleh pengguna yang sudah login.

**5. Menggunakan Data Cookies**

Disini saya akan mengambil data dari cookies untuk mengetahui kapan terakhir kali user melakukan login. Saya melakukan import `datetime`, `HttpResponseRedirect`, dan `reverse` pada file `views.py`. Kemudian saya mengubah bagian kode `login_user` agar dapat menyimpan timestamp kapan pengguna terakhir kali login. 

```
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
Setelah itu, menambahkan `'last_login': request.COOKIES.get('last_login', 'Never')` pada fungsi `show_main` yang fungsinya untuk mengambil suatu nilai dari cookie. Setelah itu, saya juga memodifikasi fungsi `logout_user` agar setelah user logout, cookie dihapus.
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Saya juga menambahkan `{{ last_login }}` di `main.html` yang fungsinya untuk menampilkan kapan terakhir kali user login.

**5. Menghubungkan model `Product` dengan `User`**

Terakhir, saya menghubungkan model saya dengan user. Tujuannya adalah agar pengguna yang sedang login dapat melihat product yang dibuat oleh user itu sendiri. Saya mengimpor library yang dibutuhkan kemudian menambahkan potongan kode ini di models Product.
```
user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
```
Tujuannya adalah agar menghubungkan suatu news dengan suatu user. Setelah itu, saya mengupdate function `create_product` yang ada di `views.py` agar setiap objek produk terhubung ke satu pengguna. Terakhir, saya menambahkan tombol di halaman utama untuk memfilter produk yang diupload oleh pengguna yang sedang login.
```
<a href="?filter=all">
    <button type="button">All Products</button>
</a>
<a href="?filter=my">
    <button type="button">My Products</button>
</a> 
```
Terakhir, saya mengupdate `product_detail.html` untuk menampilkan nama user yang mengupload produk di bagian bawah.


### Apa itu Django `AuthenticationForm?` Jelaskan juga kelebihan dan kekurangannya.
`AuthenticationForm` adalah form bawaan Django untuk login yang dapat memvalidasi kredensial (username & password) terhadap backend autentikasi, dan menyediakan error handling standar.

**Kelebihan**
* Kita tidak perlu membuat form validasi login dari nol.
* Terintegrasi dengan sistem auth & session Django (cukup menggunakan `authenticate()` + `login()`).
* Menyediakan pesan error standar dan perlindungan CSRF jika dipakai di template dengan `{% csrf_token %}`.
* Tidak mengekspos password ke template, validasi dilakukan di server.

**Kekurangan**
* Kustomisasi tampilan/field lanjutan memerlukan pembuatan subclass.
* Tidak mendukung email login secara default (perlu backend/override).
* Tidak ada fitur “remember me” bawaannya (perlu atur expiry session sendiri).


### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi merupaka proses verifikasi identitas dari user tersebut dengan memeriksa kredensial yang sudah terdaftar (username dan password). Sedangkan, otorisasi adalah penentuan hak akses dari suatu user. Sebagai contoh, terdapat dua user. Yang satu merupakan admin dan satu lagi hanya member. Admin memiliki kemampuan menambahkan produk dan lain-lain sedangkan member hanya bisa melihat produk.



### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

**Cookies**
* \+ Ringan, sederhana, tak perlu penyimpanan server.
* \+ Bisa dibaca banyak tab & berlaku lintas request.
* − Kapasitas kecil (±4KB), rawan manipulasi client, terekspos risiko XSS kalau tidak HttpOnly.
* − Tidak ideal menyimpan data sensitif.

**Session**
* \+ Lebih aman, data state disimpan di server.
* \+ Kapasitas praktis lebih besar & fleksibel (bergantung backend session).
* − Membebani penyimpanan server.
* − Butuh manajemen masa aktif/cleanup.



### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Tidak, cookies tidak aman secara default karena rentan terhadap risiko seperti pencurian melalui Cross-Site Scripting (XSS), pemalsuan permintaan lintas situs (CSRF), dan penyadapan sesi pada koneksi HTTP. Namun, Django secara proaktif mengatasi kerentanan ini dengan menyediakan lapisan keamanan yang kuat. Django melindungi dari CSRF dengan sistem token bawaan, menggunakan flag HttpOnly pada cookie sesi untuk memblokir akses dari JavaScript dan mencegah pencurian via XSS, serta secara kriptografis menandatangani data cookie untuk mencegah manipulasi. 