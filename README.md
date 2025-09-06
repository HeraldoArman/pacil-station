# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
**Nama:** Heraldo Arman  
**NPM:** 2406420702
**Kelas:** PBP - E  

**Link Penugasan:** [Assignment 2](https://pbp-fasilkom-ui.github.io/ganjil-2026/assignments/individual/assignment-2)  
**Link Deployment:** otw

---
## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Selain mengikuti tutorial, saya juga bereksperimen dengan beberapa hal tambahan. Saya membaca [dokumentasi resmi](https://docs.djangoproject.com/en/5.2/), tutorial eksternal seperti [w3school](https://www.w3schools.com/django/), dan juga sesekali bertanya ke LLM untuk debugging error. Beberapa hal yang saya eksplorasi tambahan diluar penugasan yang saya lakukan antara lain mencoba UI library ([DaisyUI](https://daisyui.com/docs/cdn/) & [TailwindCSS](https://tailwindcss.com/docs/installation/play-cdn)) dengan [CDN](https://aws.amazon.com/id/what-is/cdn/), mencoba Django Admin, serta melakukan read database.  

Langkah yang saya lakukan secara garis besar adalah:

1. Membuat virtual environment python baru, lalu menginstall Django dan dependency yang diperlukan.  
2. Menginisialisasi project Django.  
3. Mengatur `settings.py` untuk menghubungkan project dengan database.  
4. Membuat aplikasi baru bernama **main**, kemudian membuat **template**, **URL routing**, dan konfigurasi sederhana di `views.py`.  
5. Mengintegrasikan **[TailwindCSS](https://tailwindcss.com/docs/installation/play-cdn)** dan **[DaisyUI](https://daisyui.com/docs/cdn/)** menggunakan [CDN](https://aws.amazon.com/id/what-is/cdn/) agar lebih mudah.  
6. Membuat model bernama **Product**, lalu memasukannya di `admin.py` agar bisa menambahkan data.  
7. Membuat superuser untuk mengakses admin dashboard.
8. Membuat template dan bereksperimen dengan tampilan frontend.  

---

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html.
![diagram](image/diagram.png)  
*(gambar dibuat dengan [PlantUML](https://www.plantuml.com/plantuml/uml/))*  

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
* Django relatif mudah dipelajari dibandingkan framework lainnya.
* Sudah memiliki banyak fitur bawaan yang melimpah (**ORM, autentikasi, middleware, admin panel, unit test**, dll) dan ini sangat memudahkan untuk mendevelop project fullstack dengan cepat.
* Cocok untuk **prototyping cepat** tanpa perlu memasang banyak library tambahan.
* Dokumentasi dan komunitas Django sangat lengkap dan melimpah. Ada banyak tutorial, blog, diskusi, pertanyaan di [stackoverflow](https://stackoverflow.com/questions), boilerplate, contoh, dan banyak hal lainnya.
* Django adalah framework yang kuat, cocok dijadikan fondasi sebelum mempelajari framework lain.
---

## 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tutorial seru, walaupun sayangnya harus dilaksanakan secara online. Asisten dosen ramah dan sangat membantu. Semoga kedepannya bisa segera kembali offline.

---

## Lampiran Screenshot Project
otw

```

---