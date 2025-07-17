# AI-Driven Test Case Generator

Sebuah aplikasi web yang membantu pengembang secara otomatis membuat unit test Python menggunakan kecerdasan buatan lokal (Ollama). Proyek ini dibuat sebagai bagian dari tugas akhir mata kuliah (UAS).

---

## Fitur Utama

* **Generasi Unit Test Otomatis:** Memasukkan fungsi Python dan menghasilkan kode unit test Pytest yang relevan.
* **Dukungan Multi-Bahasa:** Memilih antara prompt berbahasa Inggris atau Indonesia untuk AI.
* **Antarmuka Pengguna Intuitif:** UI modern dan responsif yang dibangun dengan Next.js dan Shadcn UI.
* **Integrasi Ollama:** Memanfaatkan model AI lokal `deepseek-coder` (atau model sejenis) untuk proses generasi test.

---

## Tampilan Aplikasi

![Screenshot Aplikasi AI Test Generator](link_gambar_screenshot_anda.png)
*(Ganti `link_gambar_screenshot_anda.png` dengan URL gambar screenshot aplikasi Anda. Anda bisa mengunggahnya ke GitHub atau layanan lain.)*

---

## Persyaratan Sistem

Pastikan sistem Anda memenuhi persyaratan berikut sebelum menjalankan aplikasi:

* **Python 3.x:** Untuk menjalankan backend Flask.
* **Node.js & npm/yarn:** Untuk menjalankan frontend Next.js.
* **Ollama:** Server Ollama harus terinstal dan berjalan.
    * Pastikan Anda telah mengunduh dan menjalankan model AI yang kompatibel, misalnya:
        ```bash
        ollama run deepseek-coder # atau model lain yang Anda gunakan
        ```
    * Server Ollama secara default berjalan di `http://localhost:11434`.

---

## Cara Menjalankan Proyek

Ikuti langkah-langkah di bawah ini untuk menginstal dan menjalankan aplikasi secara lokal.

### 1. Setup Backend (Flask)

1.  **Navigasi ke Direktori Backend:**
    ```bash
    cd nama_folder_proyek_anda/backend # Ganti dengan path folder backend Anda
    ```
2.  **Instal Dependensi Python:**
    ```bash
    pip install Flask requests flask-cors
    ```
3.  **Jalankan Server Backend:**
    ```bash
    python app.py # Ganti app.py jika nama file Flask Anda berbeda
    ```
    Server backend akan berjalan di `http://localhost:5000`.

### 2. Setup Frontend (Next.js)

1.  **Navigasi ke Direktori Frontend:**
    ```bash
    cd nama_folder_proyek_anda/frontend # Ganti dengan path folder frontend Anda
    ```
2.  **Instal Dependensi Node.js:**
    ```bash
    npm install # atau yarn install
    ```
3.  **Jalankan Aplikasi Frontend:**
    ```bash
    npm run dev # atau yarn dev
    ```
    Aplikasi frontend akan berjalan di `http://localhost:3000` (atau port default Next.js).

---

## Cara Menggunakan Aplikasi

1.  Pastikan server Ollama, backend Flask, dan frontend Next.js semuanya berjalan.
2.  Buka browser Anda dan akses `http://localhost:3000`.
3.  Pilih bahasa yang Anda inginkan (Indonesia/English).
4.  Masukkan fungsi Python Anda ke dalam kotak teks yang tersedia.
5.  Klik tombol "Buat Test" / "Generate Tests".
6.  Kode unit test Pytest yang dihasilkan akan muncul di bagian bawah. Anda dapat menyalinnya dengan tombol "Salin Kode Test".

---

## Manfaat Aplikasi

Aplikasi ini sangat bermanfaat bagi pengembang karena:
* **Meningkatkan Efisiensi:** Mengurangi waktu dan usaha yang dibutuhkan untuk menulis test awal secara manual.
* **Memastikan Kualitas Kode:** Membantu memastikan fungsionalitas kode bekerja sesuai harapan dengan menyediakan dasar test otomatis.
* **Mempercepat Proses Pengembangan:** Memungkinkan siklus pengembangan yang lebih cepat dengan otomatisasi test.

---

## Dikembangkan Oleh

[Peno] - [NIM 221220095]

---