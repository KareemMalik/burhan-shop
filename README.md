# Burhan Shop — Football Shop

No. 1 Football Shop in FASILKOM UI

### 🪁 Deployment 
Click Here: [Burhan Shop](https://malik-alifan-burhanshop.pbp.cs.ui.ac.id/)

### 📚 Assignment Archive
* [Tugas 2: Implementasi Model-View-Template (MVT) pada Django](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-2:-Implementasi-Model%E2%80%90View%E2%80%90Template-(MVT)-pada-Django)
* [Tugas 3: Implementasi Form dan Data Delivery pada Django](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-3:-Implementasi-Form-dan-Data-Delivery-pada-Django)
* [Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-4:-Implementasi-Autentikasi,-Session,-dan-Cookies-pada-Django)
* [Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS](https://github.com/KareemMalik/burhan-shop/wiki/Tugas-5:-Desain-Web-menggunakan-HTML,-CSS-dan-Framework-CSS)



***

## Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS

### Langkah - langkah implementasi
**1. Membuat Fungsi dan Tombol untuk Edit & Delete Produk**

Langkah pertama yang saya lakukan adalah membuat function `edit_product` pada `views.py` dengan parameter `request` dan `id`.

```
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)
```

Selanjutnya, saya membuat file html baru dengan nama `edit_product.html` yang gunanya untuk memberikan interface kepada pengguna yang ingin meng-edit produknya.

```
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Terakhir, saya menambahkan path url ke `urls.py` dengan mengimport `edit_product` dan menambahkannya ke `urlpatterns`. Terakhir, saya menambahkan tombol edit product di `main.html`.

Saya melakukan hal yang sama untuk menambahkan fungsi delete produk. Saya membuat fungsi `delete_product`, menambahkan path url ke `urls.py` dan membuat tombol di halaman utama untuk menghapus produk.
```
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

**2. Set-up Tailwind**
Selanjutnya disini saya memilih untuk menggunakan salah satu framework CSS yaitu Tailwind. Saya memilih framework ini dikarenakan dengan Tailwind, saya bisa memberikan styling langsung di html tag seperti `<div>`, dan lain-lain. Sehingga menjadi lebih mudah dan tidak harus bolak-balik berganti file. Untuk instalasinya, saya menambahkan kode di bawah ini ke `base.html`
```
<script src="https://cdn.tailwindcss.com">
</script>
```

**3. Membuat Navigation Bar**
Selanjutnya saya membuat navigation bar yang memungkinkan pengguna untuk berpindah page, log out, dan membuat produk baru dengan lebih mudah. Saya juga memberikan styling pada navigation bar tersebut. Tidak lupa, saya juga membuat navigation bar untuk versi mobile agar desain menjadi lebih responsif. Saya menggunakan javascript agar navigation bar versi mobile dapat bekerja dengan baik.

**4. Melakukan Styling untuk Seluruh Halaman**
Terakhir, saya membuat styling untuk halaman `main.html`, `create_product.html`, `edit_product.html`, `login,html`, dan `register.html`. Saya membuat styling pada setiap halaman tersebut menggunakan Tailwind. Untuk melakukan styling pada forms, saya menggunakan CSS secara langsung. Saya juga menambahkan direktori static yang berisi folder css dan gambar-gambar yang digunakan di website ini. Saya menambahkan gambar ketika tidak ada produk yang dibuat oleh user.


### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas selector CSS ditentukan oleh sebuah konsep yang disebut spesifisitas (specificity). Ketika ada beberapa aturan CSS yang menargetkan elemen HTML yang sama, browser akan menerapkan gaya dari selector yang paling spesifik. Urutan prioritas dari yang tertinggi hingga terendah adalah: style inline (yang ditulis langsung pada atribut `style` elemen), diikuti oleh ID selector (contoh: `#nama-id`), lalu class selector (contoh: `.nama-kelas`), attribute selector (contoh: `[type="text"]`), dan pseudo-class (contoh: `:hover`). Prioritas terendah dimiliki oleh element selector (contoh: `div`, `p`) dan pseudo-element (contoh: `::before`). Jika dua selector memiliki nilai spesifisitas yang sama, maka aturan yang didefinisikan paling akhir di dalam file CSS akan menjadi pemenangnya. Selain itu, terdapat deklarasi `!important` yang akan mengalahkan semua aturan spesifisitas lainnya.


### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design sangat penting karena memastikan aplikasi web dapat memberikan pengalaman pengguna (UX) yang optimal di berbagai ukuran layar perangkat, mulai dari ponsel, tablet, hingga monitor desktop. Tanpa desain yang responsif, pengguna perangkat seluler akan kesulitan menavigasi situs, yang pada akhirnya dapat menurunkan trafik dan konversi. Contoh aplikasi yang sudah menerapkan responsive design adalah tokopedia. Karena ketika dikases menggunakan device dengan layar lebih kecil, tampilan webnya akan menyesuaikan. Sedangkan yang belum menerapkan adalah web https://www.spacejam.com/1996/. Web tersebut tidak responsif karena ketika diakses menggunakan layar yang lebih kecil, konten web ikut mengecil dan tidak menyesuaikan display pengguna sehingga tidak responsif.


### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
* Padding:  Ruang di dalam border, yang memberi jarak antara konten (teks/gambar) dengan garis border.(Cth Implementasi: `padding: 15px;` (padding 15px untuk ke-4 sisi))
* Border: Garis yang mengelilingi padding dan konten sebuah elemen. (Cth Implementasi: `border: 2px solid black;`)
* Margin: Ruang di luar border, yang menciptakan jarak antara elemen tersebut dengan elemen lain di sekitarnya. (Cth Implementasi: `margin: 25px;`)


### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
* CSS Flexbox adalah model tata letak (layout) satu dimensi yang dirancang untuk mengatur, mensejajarkan, dan mendistribusikan ruang di antara item dalam sebuah wadah (container), baik secara horizontal (baris) maupun vertikal (kolom).
* CSS Grid Layout adalah model tata letak dua dimensi yang memungkinkan Anda untuk mengatur konten dalam baris dan kolom secara bersamaan, mirip seperti membuat tabel atau spreadsheet.