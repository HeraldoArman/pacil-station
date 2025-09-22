# Tugas 2: Implementasi Model-View-Template (MVT) pada Django

**Nama:** Heraldo Arman  
**NPM:** 2406420702  
**Kelas:** PBP - E  
**Link Penugasan:** [Tugas 2](https://pbp-fasilkom-ui.github.io/ganjil-2026/assignments/individual/assignment-2)  
**Link Deployment:** [heraldo-arman-pacilstation.pbp.cs.ui.ac.id](https://heraldo-arman-pacilstation.pbp.cs.ui.ac.id/)

---

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Selain mengikuti tutorial, saya juga bereksperimen dengan beberapa hal tambahan. Saya membaca [dokumentasi resmi](https://docs.djangoproject.com/en/5.2/), tutorial eksternal seperti [w3school](https://www.w3schools.com/django/), dan juga sesekali bertanya ke LLM untuk debugging error. Beberapa hal yang saya eksplorasi tambahan diluar penugasan yang saya lakukan antara lain mencoba UI library ([DaisyUI](https://daisyui.com/docs/cdn/) dan [TailwindCSS](https://tailwindcss.com/docs/installation/play-cdn)) dengan [CDN](https://aws.amazon.com/id/what-is/cdn/), mencoba Django Admin, serta melakukan read database.

Langkah yang saya lakukan secara garis besar adalah:

1. Membuat virtual environment python baru, lalu menginstall Django dan dependency yang diperlukan.
2. Menginisialisasi project Django.
3. Mengatur `settings.py` untuk menghubungkan project dengan database.
4. Membuat aplikasi baru bernama **main**, kemudian membuat **template**, **URL routing**, dan konfigurasi sederhana di `views.py`.
5. Mengintegrasikan **[TailwindCSS](https://tailwindcss.com/docs/installation/play-cdn)** dan **[DaisyUI](https://daisyui.com/docs/cdn/)** menggunakan [CDN](https://aws.amazon.com/id/what-is/cdn/) agar lebih mudah.
6. Membuat model bernama **Product**, lalu memasukannya di `admin.py` agar bisa menambahkan data.
7. Membuat superuser untuk mengakses admin dashboard.
8. Membuat template dan bereksperimen dengan tampilan frontend.
9. Melakukan deployment ke [PWS](https://pbp.cs.ui.ac.id/web)

---

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html.

![diagram](image/diagram.png)  
_(gambar dibuat dengan [PlantUML](https://www.plantuml.com/plantuml/uml/))_

**Penjelasan Singkat:**

1. Client mengirim request ke server lalu masuk ke `urls.py`.
2. `urls.py` memeriksa pola URL, jika valid maka request diteruskan ke `views.py`. Namun jika tak valid maka akan mereturn error 404.
3. di `views.py` kita bisa melakukan beberapa fungsi seperti melakukan query ke `models.py` bila diperlukan.
4. Data dari `models.py` dikembalikan ke `views.py`.
5. `views.py` merender template HTML menggunakan data tersebut.
6. Hasil render dikemas dalam `HttpResponse` dan dikirim ke browser sebagai response.

---

## 3. Jelaskan peran `settings.py` dalam proyek Django!

Sederhananya, file `settings.py` berfungsi sebagai pusat konfigurasi proyek Django.  
Hal yang bisa dilakukan seperti

- Konfigurasi database.
- Environment variable.
- Allowed hosts.
- Direktori static files.
- Middleware.
- Installed apps.
- Keamanan & autentikasi.
- Dan masih banyak lagi.
  Singkatnya, `settings.py` adalah tempat mengatur semua konfigurasi inti dalam proyek Django.

---

## 4. Bagaimana cara kerja migrasi database di Django?

1. Melakukan definisi database di `models.py` menggunakan class Python.
2. Jalankan command:
   ```bash
   python manage.py makemigrations
   ```
   Disini Django akan membuat file di folder `migrations/` berisi instruksi Python yang merepresentasikan perubahan tabel.
3. Jalankan command:
   ```bash
   python manage.py migrate
   ```
   Django mengeksekusi file migrasi tersebut menjadi query SQL lalu model berhasil diterapkan di database.

---

## 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya pribadi:

- Django relatif mudah dipelajari dibandingkan framework lainnya.
- Sudah memiliki banyak fitur bawaan yang melimpah (**ORM, autentikasi, middleware, admin panel, unit test**, dll) dan ini sangat memudahkan untuk mendevelop project fullstack dengan cepat.
- Cocok untuk **prototyping cepat** tanpa perlu memasang banyak library tambahan.
- Dokumentasi dan komunitas Django sangat lengkap dan melimpah. Ada banyak tutorial, blog, diskusi, pertanyaan di [stackoverflow](https://stackoverflow.com/questions), boilerplate, contoh, dan banyak hal lainnya.
- Django adalah framework yang kuat, cocok dijadikan fondasi sebelum mempelajari framework lain.

---

## 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tutorial seru, walaupun sayangnya harus dilaksanakan secara online. Asisten dosen ramah dan sangat membantu. Semoga kedepannya bisa segera kembali offline.

---

## Credit

- logo: [logoipsum.com](https://logoipsum.com/artwork/389)

---

## Lampiran Screenshot Project

![main page](image/main-page.png)  
![product page](image/product-page.png)

# Tugas 3: Implementasi Form dan Data Delivery pada Django

**Nama:** Heraldo Arman  
**NPM:** 2406420702  
**Kelas:** PBP - E  
**Link Penugasan:** [Tugas 3](https://pbp-fasilkom-ui.github.io/ganjil-2026/assignments/individual/assignment-3)  
**Link Deployment:** [heraldo-arman-pacilstation.pbp.cs.ui.ac.id](https://heraldo-arman-pacilstation.pbp.cs.ui.ac.id/)

---

## 1. Jelaskan mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?

Data delivery itu sangat penting karena berhubungan dengan bagaimana data tersebut berpindah. kebanyakan platform modern biasanya terdiri dari banyak bagan (backend, frontend, database, API eksternal, dll). Tanpa data delivery, informasi yang ada bisa menjadi tidak sinkron, sulit diakses real-time, dan rawan kehilangan data. Contoh sederhananya adalah ketika pengguna melakukan checkout, sistem perlu mengirim data ke database, menampilkan status pesanan ke pengguna, sekaligus mengirim notifikasi. Semua ini hanya mungkin dengan adanya data delivery yang baik.

---

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya pribadi, JSON lebih baik dibandingkan dengan XML karena lebih mudah dibaca oleh manusia. XML dan JSON sendiri merupakan sama sama format pertukaran data. Namun JSON lebih populer karena ia lebih sederhana dan mudah dipahami. Ditambah lagi, kebanyakan library pemrograman modern (seperti JavaScript, Python, dan banyak framework web lainnya) sudah menyediakan dukungan native untuk JSON, sehingga parsing dan manipulasi data menjadi lebih mudah dan efisien. Selain itu, JSON memiliki struktur yang lebih ringkas, tidak memerlukan tag penutup seperti XML, dan lebih hemat bandwidth. Oleh karena itu, JSON lebih banyak digunakan dalam pengembangan aplikasi web dan API saat ini.

---

## 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` digunakan untuk melakukan validasi data yang dimasukkan oleh user ke dalam form. Fungsi ini nantinya akan melakukan:

- Pengecekan apakah semua field sudah sesuai aturan (tipe data benar atau tidak, kolom yang wajib di isi terisi atau tidak, dll).
- Mereturn `True` jika data valid dan `False` jika terdapat error.

Tanpa `is_valid()`, terdapat risiko dimana terdapat data yang salah atau tak sesuai ke dalam database.

---

## 3. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`CSRF` (Cross Site Request Forgery) adalah jenis serangan di mana situs jahat membuat link, form, atau kode JavaScript yang memicu aksi di situs lain (situs target) menggunakan kredensial pengguna yang sedang login pada situs target. Jadi pengguna tanpa sadar melakukan aksi yang merugikan. Jika form di template tidak menyertakan `csrf_token`, maka penyerang bisa membuat sebuah halaman di situs jahat yang mengirim request POST ke situs target (di mana user sedang login) tanpa sepengetahuan user.

**Sumber:** [Django CSRF Documentation](https://docs.djangoproject.com/en/5.2/ref/csrf/)

---

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Selain mengikuti tutorial, saya juga bereksperimen dengan beberapa hal tambahan. Saya membaca [dokumentasi resmi](https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/#overriding-the-default-fields), tutorial eksternal seperti [w3school](https://www.w3schools.com/django/) dan [GeeksForGeeks](https://www.geeksforgeeks.org/python/django-forms/), dan juga sesekali bertanya ke LLM untuk debugging error.

Langkah yang saya lakukan secara garis besar adalah:

1. Membuat views baru.
2. Membuat `forms.py` dan mengisi kodenya.
3. Membuat file html baru dan mengisinya.
4. Lalu menambahkan sedikit styling untuk mempercantik
5. Lalu menambah button add product pada navbat.

Sisanya seperti `serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.` dan `Membuat halaman yang menampilkan detail dari setiap data objek model.` tak saya kerjakan di sesi ini karena saya sudah mengerjakannya di tugas sebelumnya.

---

## Lampiran Screenshot Postman Untuk Mendapatkan data JSON dan XML

### Get All Product JSON

![Get All Product JSON](image/json.png)

### Get All Product XML

![Get All Product XML](image/xml.png)

### Get Product By Id JSON

![Get Product by Id JSON](image/json-id.png)

### Get Product By Id XML

![Get Product by Id XML](image/xml-id.png)

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

**Nama:** Heraldo Arman  
**NPM:** 2406420702  
**Kelas:** PBP - E  
**Link Penugasan:** [Tugas 4](https://pbp-fasilkom-ui.github.io/ganjil-2026/assignments/individual/assignment-4)  
**Link Deployment:** [heraldo-arman-pacilstation.pbp.cs.ui.ac.id](https://heraldo-arman-pacilstation.pbp.cs.ui.ac.id/)

---

## 1. Apa itu Django `AuthenticationForm`? Jelaskan juga kelebihan dan kekurangannya.

Django `AuthenticationForm` adalah salah satu form bawaan dari Django yang digunakan untuk proses autentikasi pengguna, biasanya saat login. Form ini memiliki 2 field utama, yakni `username` dan `password`. Fungsi utamanya adalah untuk melakukan validasi kredensial, menyediakan error handling otomatis (credential salah atau lainnya), dan integrasi dengan django `login()` yang mana bisa langsung dipakai untuk login user.

### Contoh penggunaan dasar

```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

```

### Kelebihan `AuthenticationForm`

1. Mudah digunakan, bisa langsung dipakai dan sudah memiliki cukup banyak fitur.
2. Keamanan yang terjaga karena memang sudah dioptimisasi untuk proyek Django.
3. Integrasi penuh dengan Django Auth yang mana kompatibel dengan middleware, session, dan decorators seperti `@login_required`.
4. Error handling otomatis yang bisa langsung memberikan feedback error jika gagal login.

### Kekurangan `AuthenticationForm`

1. Agak kurang fleksibel untuk di kustomisasi.
2. Tampilan default tidak memiliki styling, harus di styling sendiri _(cek `forms.py` untuk contoh lebih lanjut)_
3. Hanya menyediakan autentikasi dasar, jika ingin mengimplementasikan fitur yang lebih advanced seperti `2FA` atau semacamnya harus implementasi sendiri

---

## 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?

### Definisi autentikasi vs otorisasi

Autentikasi adalah proses untuk memverifikasi identitas pengguna atau sistem guna memastikan bahwa mereka adalah siapa yang mereka klaim.
Sedangkan Otorisasi adalah proses untuk menentukan dan memberikan hak akses kepada pengguna atau sistem yang telah diautentikasi.

### Contoh kasus

![alt text](image/auth.png)

**Sumber:** [Geeks for Geeks](https://www.geeksforgeeks.org/computer-networks/difference-between-authentication-and-authorization/)

| Aspek          | Autentikasi                             | Otorisasi                                 |
| -------------- | --------------------------------------- | ----------------------------------------- |
| **Tujuan**     | Melakukan verifikasi identitas pengguna | Menentukan hak akses pengguna             |
| **Pertanyaan** | "Who are you?"                          | "What permission do you have?"            |
| **Urutan**     | Dilakukan sebelum otorisasi             | Dilakukan setelah autentikasi             |
| **Contoh**     | Login dengan username dan password      | Mengakses data berdasarkan peran pengguna |

### Bagaimana Django handle kedua konsep tersebut

- Authentication: Django menyediakan `django.contrib.auth` untuk autentikasi serta form bawaan `AuthenticationForm`
- Authorization: Django menggunakan decorator seperti `@login_required()`

---

## 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
### Cookies
Kelebihan:
- 