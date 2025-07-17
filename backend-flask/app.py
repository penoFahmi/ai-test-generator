from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv # Untuk memuat variabel lingkungan dari .env

# Muat variabel lingkungan dari file .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# --- KONFIGURASI GEMINI ---
# Pastikan GEMINI_API_KEY sudah diatur di file .env di folder backend Anda.
# Contoh isi file .env: GEMINI_API_KEY=YOUR_API_KEY_ANDA_DI_SINI
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set. Please set your Gemini API key in a .env file or as an environment variable.")

genai.configure(api_key=GEMINI_API_KEY)

# Model Gemini yang digunakan
# PENTING: Jika 'gemini-2.0-flash' masih error 404, coba ganti ke "gemini-1.0-pro"
GEMINI_MODEL = "gemini-2.0-flash" 

@app.route('/generate-test', methods=['POST'])
def generate_test():
    data = request.json
    code_input = data.get('code')
    selected_language = data.get('language', 'en')

    if not code_input:
        error_message = "No code provided."
        if selected_language == 'id':
            error_message = "Tidak ada kode yang diberikan."
        return jsonify({"error": error_message}), 400

    # --- LOGIKA PROMPT UNTUK GEMINI ---
    # Instruksi tegas untuk Gemini agar HANYA mengeluarkan kode Python.
    if selected_language == 'id':
        prompt = f"""Hasilkan unit test Python pytest yang ringkas untuk fungsi berikut.
Sertakan setidaknya satu kasus test positif dan satu kasus test batas jika berlaku.
Berikan HANYA kode test-nya saja dalam blok kode Python (diawali ```python dan diakhiri ```),
TANPA penjelasan, narasi, atau komentar non-Python (seperti //) di luar blok kode tersebut.
Pastikan kode yang dihasilkan dapat langsung dijalankan dan tidak terpotong.

```python
{code_input}
```"""
    else: # Default ke bahasa Inggris
        prompt = f"""Generate a concise Python pytest unit test for the following function.
Include at least one positive test case and one edge case if applicable.
Provide ONLY the test code within a Python code block (starting with ```python and ending with ```),
with NO explanations, narratives, or non-Python comments (like //) outside of that code block.
Ensure the generated code is directly executable and not truncated.

```python
{code_input}
```"""

    try:
        # --- PANGGILAN KE GEMINI API ---
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(prompt)

        if not response.parts:
            raise Exception("Gemini API did not return any content parts.")
        
        gemini_output_text = response.text

        # --- PEMBESIHAN RESPON AI ---
        # Mencari dan mengekstrak blok kode Python dari respons Gemini.
        cleaned_code = ""
        code_block_start_marker = "```python"
        code_block_end_marker = "```"

        start_index = gemini_output_text.find(code_block_start_marker)
        
        if start_index != -1:
            temp_code = gemini_output_text[start_index + len(code_block_start_marker):]
            end_index = temp_code.find(code_block_end_marker)
            if end_index != -1:
                cleaned_code = temp_code[:end_index]
            else:
                cleaned_code = temp_code
        else:
            cleaned_code = gemini_output_text

        test_code = cleaned_code.strip()

        if not test_code.strip():
            error_message = "AI could not generate valid Python test code. Please try a different input or prompt."
            if selected_language == 'id':
                error_message = "AI tidak dapat membuat kode test Python yang valid. Silakan coba input atau prompt lain."
            return jsonify({"error": error_message}), 500

        return jsonify({"test_code": test_code})

    except genai.types.BlockedPromptException as e:
        error_message = f"Gemini API blocked the prompt: {e.response.prompt_feedback.block_reason.name}."
        if selected_language == 'id':
            error_message = f"Gemini API memblokir prompt: {e.response.prompt_feedback.block_reason.name}."
        return jsonify({"error": error_message}), 500
    except Exception as e:
        error_message = f"An unexpected error occurred with Gemini API: {str(e)}"
        if selected_language == 'id':
            error_message = f"Terjadi kesalahan tak terduga dengan Gemini API: {str(e)}"
        if hasattr(e, 'response') and e.response:
            print(f"Gemini raw error response: {e.response}")
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    # Pastikan Anda punya Flask dan google-generativeai terinstal:
    # pip install Flask requests flask-cors google-generativeai python-dotenv
    app.run(debug=True, port=5000)