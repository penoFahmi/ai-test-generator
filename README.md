# AI-Driven Automated Test Case Generator

Proyek ini adalah sebuah aplikasi *full-stack* yang memanfaatkan AI lokal (Ollama) untuk secara otomatis menghasilkan *unit test cases* untuk berbagai bahasa pemrograman. Ini dirancang untuk mempercepat proses *white-box testing* dan membantu *developer* menulis *test* yang lebih komprehensif.

## Fitur Utama

* **Generasi Test Otomatis:** Masukkan potongan kode (fungsi/metode), dan AI akan menghasilkan *unit test* yang relevan.
* **Dukungan Multi-Bahasa Kode:** Meskipun fokus awal Python (Pytest), arsitekturnya siap untuk menghasilkan *test* untuk PHP (PHPUnit) dan JavaScript (Jest) (membutuhkan input bahasa pemrograman dari UI).
* **Antarmuka Pengguna Intuitif:** Dibangun dengan Next.js dan Shadcn UI untuk pengalaman pengguna yang bersih dan responsif.
* **Lokal AI Inference:** Menggunakan Ollama untuk menjalankan model AI (seperti Deepseek Coder) secara *offline* di mesin lokal Anda.
* **Dukungan Multi-Bahasa UI:** Antarmuka aplikasi tersedia dalam Bahasa Indonesia dan Bahasa Inggris.

## Stack Teknologi

* **Backend:** Python (Flask)
* **Frontend:** Next.js, React, Shadcn UI, Tailwind CSS
* **AI Inference:** Ollama dengan model Deepseek Coder
* **Testing Frameworks yang Ditargetkan (contoh):** Pytest (Python), PHPUnit (PHP), Jest (JavaScript)

## Struktur Proyek# ai-test-generator
