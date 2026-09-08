import streamlit as st
from google import genai

# ── Konfigurasi Halaman ──────────────────────────────────────────────────────
st.set_page_config(page_title="Jelajah AI", page_icon="✈️", layout="centered")

# ── Judul ────────────────────────────────────────────────────────────────────
st.title("Jelajah AI ✈️")
st.caption("Teman perjalananmu yang seru!")

# ── System Prompt ────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """
Kamu adalah "Jelajah AI", travel assistant yang asyik dan seru!
Kamu punya pengetahuan mendalam tentang dunia traveling: destinasi wisata,
tips packing, budget trip, kuliner lokal, transportasi, visa & dokumen perjalanan,
hotel & akomodasi, aktivitas seru di berbagai kota, dan cuaca/musim terbaik untuk berkunjung.

Gaya bicaramu santai, friendly, dan semangat — seperti teman yang udah keliling
banyak negara. Pakai bahasa Indonesia campuran yang natural (boleh sisip kata
bahasa Inggris yang lazim di dunia travel). Sesekali tambahkan emoji yang relevan
biar lebih hidup ✈️🌏🗺️🏖️.

Kalau ditanya sesuatu di luar topik travel, dengan sopan arahkan balik ke topik travel.
Selalu ingat konteks percakapan sebelumnya — jangan pernah lupa apa yang sudah dibahas
dengan user di chat yang sama.

Contoh gaya jawaban:
- "Wah, Bali tuh emang juara sih! Kalau lo mau ke sana bulan Juli, siapin budget
  minimal Rp 1,5 juta per hari ya buat akomodasi yang decent..."
- "Visa Schengen itu memang agak ribet, tapi tenang aja! Dokumen utama yang lo
  butuhin itu: paspor valid minimal 6 bulan, bukti keuangan, itinerary, sama
  asuransi perjalanan..."
"""

# ── Input API Key ─────────────────────────────────────────────────────────────
col1, col2 = st.columns([5, 1])
with col1:
    api_key_input = st.text_input(
        "API Key",
        type="password",
        label_visibility="collapsed",
        placeholder="Masukkan Google Gemini API Key kamu di sini...",
    )
with col2:
    submit = st.button("Submit")

# Simpan API key ke session_state saat Submit diklik
if submit and api_key_input:
    st.session_state.api_key = api_key_input

# ── Validasi API Key ──────────────────────────────────────────────────────────
if "api_key" not in st.session_state or not st.session_state.api_key:
    st.info("🗝️ Masukkan Google Gemini API Key di atas untuk mulai ngobrol!", icon="✈️")
    st.stop()

# ── Inisialisasi Client & Chat Session ───────────────────────────────────────
# Hanya buat client baru jika belum ada, atau jika API key berubah.
# Ini PENTING: jika client sudah ada, jangan buat baru agar chat session
# dan seluruh riwayat percakapan di dalamnya tetap terjaga.
if ("genai_client" not in st.session_state) or (
    st.session_state.get("_last_key") != st.session_state.api_key
):
    try:
        client = genai.Client(api_key=st.session_state.api_key)
        st.session_state.genai_client = client
        st.session_state._last_key = st.session_state.api_key
        # Reset chat dan messages jika key berubah
        st.session_state.pop("chat", None)
        st.session_state.pop("messages", None)
    except Exception as e:
        st.error(f"❌ API Key tidak valid: {e}")
        st.stop()

# Buat chat session baru hanya jika belum ada.
# Objek 'chat' ini menyimpan seluruh konteks percakapan di sisi Gemini API.
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.genai_client.chats.create(
        model="gemini-3.5-flash-lite",
        config={"system_instruction": SYSTEM_PROMPT},
    )

# Inisialisasi list riwayat pesan untuk keperluan render UI
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Render Riwayat Percakapan ─────────────────────────────────────────────────
# Setiap kali Streamlit rerun, semua pesan dari session_state ditampilkan kembali.
# Inilah yang membuat chat history tetap terlihat di layar.
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Tombol Reset ──────────────────────────────────────────────────────────────
# Tombol ini menghapus SELURUH riwayat percakapan — baik di UI maupun di Gemini session.
if st.button("Reset Chat 🔄", help="Hapus semua pesan dan mulai percakapan baru"):
    st.session_state.pop("chat", None)
    st.session_state.pop("messages", None)
    st.rerun()

# ── Input & Respons ───────────────────────────────────────────────────────────
prompt = st.chat_input("Ask AI")

if prompt:
    # 1. Simpan dan tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Kirim ke Gemini dan tampilkan respons
    with st.chat_message("assistant"):
        with st.spinner("Lagi mikirin rute terbaik buat kamu... 🗺️"):
            try:
                # send_message() secara otomatis menyertakan seluruh riwayat
                # percakapan yang tersimpan di dalam objek chat session Gemini.
                response = st.session_state.chat.send_message(prompt)
                answer = response.text if hasattr(response, "text") else str(response)
            except Exception as e:
                answer = f"❌ Ups, ada error nih: {e}\n\nCoba cek API key kamu atau coba lagi ya!"
        st.markdown(answer)

    # 3. Simpan respons ke riwayat UI
    st.session_state.messages.append({"role": "assistant", "content": answer})