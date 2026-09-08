# AI-Chatbot-with-Streamlit (Jelajah AI ✈️)
<img width="1848" height="917" alt="Screenshot 2026-09-08 220833" src="https://github.com/user-attachments/assets/10b57d28-a9f9-45f1-a568-b4724150df68" />


> **Teman perjalananmu yang seru!** — Chatbot travel assistant berbasis AI yang siap membantu semua kebutuhan perjalananmu.

---

## 📖 Tentang Aplikasi

**Jelajah AI** adalah aplikasi chatbot travel assistant yang dibangun dengan [Streamlit](https://streamlit.io/) dan didukung oleh **Google Gemini API**. Aplikasi ini dirancang untuk menjadi teman ngobrol seputar dunia traveling, mulai dari rekomendasi destinasi, tips packing, info visa, hingga estimasi budget perjalanan.

Gaya bicaranya santai dan friendly, seperti teman yang sudah keliling banyak negara! 🌏
Kamu bisa langsung akses disini: https://travel-ai-chatbot.streamlit.app/

(Aplikasi ini merupakan demonstrasi implementasi streamlit dan API Gemini sebagai sebuah webapp chatbot. Keterbatasan aplikasi ini tergantung pada API Gemini yang digunakan, serta output yang hanya berupa teks.)
---

## ✨ Fitur Utama

- 🗺️ **Rekomendasi Destinasi** — Saran tempat wisata berdasarkan preferensi dan budget kamu
- 💬 **Memori Percakapan** — AI mengingat seluruh konteks obrolan dalam satu sesi
- 🔄 **Reset Chat** — Mulai percakapan baru kapan saja

---

## 🛠️ Teknologi yang Digunakan

| Komponen | Teknologi |
|---|---|
| Framework UI | [Streamlit](https://streamlit.io/) |
| AI Model | Google Gemini (`gemini-3.5-flash-lite`) |
| Bahasa | Python 3.8+ |
| Library AI | `google-genai` |

---

## ⚙️ Cara Instalasi & Menjalankan

### 1. Clone atau Download Proyek

```bash
git clone https://github.com/username/jelajah-ai.git
cd jelajah-ai
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependensi

```bash
pip install streamlit google-genai
```

### 4. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada alamat `http://localhost:8501`.

---

## 🔑 Mendapatkan Google Gemini API Key

1. Kunjungi [Google AI Studio](https://aistudio.google.com/)
2. Login dengan akun Google kamu
3. Klik **"Get API Key"** → **"Create API Key"**
4. Salin API key yang dihasilkan
5. Masukkan API key tersebut di kolom input pada aplikasi

> ⚠️ **Penting:** Jangan pernah membagikan atau meng-commit API key kamu ke repository publik.

---

## 🚀 Cara Menggunakan

1. **Masukkan API Key** — Ketikkan Google Gemini API Key kamu di kolom yang tersedia, lalu klik **Submit**
2. **Mulai Mengobrol** — Ketik pertanyaan atau kebutuhan travelmu di kolom chat di bagian bawah
3. **Eksplorasi Topik** — Tanyakan apa saja seputar traveling: destinasi, visa, budget, kuliner, dll.
4. **Reset Jika Perlu** — Klik tombol **Reset Chat 🔄** untuk memulai percakapan baru dari awal

### Contoh Pertanyaan

```
"Rekomendasiin destinasi Asia Tenggara yang budget-friendly dong!"
"Apa aja dokumen yang diperlukan untuk bikin visa Schengen?"
"Tips packing buat trip 2 minggu ke Eropa musim dingin?"
"Berapa estimasi budget untuk liburan 5 hari ke Jepang?"
"Makanan apa yang wajib dicoba di Thailand?"
```

---

## 📁 Struktur Proyek

```
jelajah-ai/
│
├── app.py          # File utama aplikasi Streamlit
├── requirements.txt          # File requirement aplikasi Streamlit
└── README.md       # Dokumentasi proyek ini
```

---

## 🔧 Konfigurasi & Kustomisasi

### Mengubah System Prompt

Kepribadian dan kemampuan AI dapat dikustomisasi dengan mengubah variabel `SYSTEM_PROMPT` di dalam `app.py`:

```python
SYSTEM_PROMPT = """
Kamu adalah "Jelajah AI", travel assistant yang asyik dan seru!
...
"""
```

### Mengganti Model Gemini

Model yang digunakan dapat diubah pada bagian inisialisasi chat session:

```python
st.session_state.chat = st.session_state.genai_client.chats.create(
    model="gemini-3.5-flash-lite",  # Ganti dengan model lain di sini
    config={"system_instruction": SYSTEM_PROMPT},
)
```

Model lain yang tersedia: `gemini-2.0-flash`, `gemini-1.5-pro`, dll. Cek [dokumentasi resmi](https://ai.google.dev/gemini-api/docs/models/gemini) untuk daftar lengkap.

---

## ⚠️ Catatan Penting

- **API Key tersimpan di session** — API key hanya disimpan selama sesi browser aktif dan tidak dikirim ke mana pun selain Google API.
- **Riwayat chat tidak persisten** — Percakapan akan hilang ketika halaman di-refresh atau browser ditutup.
- **Batas penggunaan** — Penggunaan API tunduk pada kuota dan batas yang ditetapkan oleh Google AI Studio.

---
