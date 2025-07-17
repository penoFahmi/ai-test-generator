from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "deepseek-coder"

@app.route('/generate-test', methods=['POST'])
def generate_test():
    data = request.json
    code_input = data.get('code')
    # --- BARIS INI DITAMBAH ---
    selected_language = data.get('language', 'en') # Ambil bahasa dari frontend, default 'en'
    # --- AKHIR PENAMBAHAN ---

    if not code_input:
        return jsonify({"error": "No code provided"}), 400

    # --- LOGIKA PROMPT BERDASARKAN BAHASA ---
    if selected_language == 'id':
        prompt = f"""Hasilkan unit test Python pytest yang ringkas untuk fungsi berikut. Sertakan setidaknya satu kasus test positif dan satu kasus test batas jika berlaku. Berikan hanya kode test-nya saja, tanpa penjelasan tambahan atau teks boilerplate di luar blok kode test.

        ```python
        {code_input}
        ```
        """
    else: # Default ke bahasa Inggris
        prompt = f"""Generate a concise Python pytest unit test for the following function. Include at least one positive test case and one edge case if applicable. Provide only the test code, no extra explanations or boilerplate text outside the test code block.

        ```python
        {code_input}
        ```
        """
    # --- AKHIR LOGIKA PROMPT ---

    try:
        response = requests.post(OLLAMA_API_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()

        ollama_output = response.json()
        test_code_raw = ollama_output.get('response', '')

        # Membersihkan respons dari Ollama
        if test_code_raw.startswith('```python'):
            test_code_raw = test_code_raw[len('```python'):]
        if test_code_raw.endswith('```'):
            test_code_raw = test_code_raw[:-len('```')]

        test_code = test_code_raw.strip()

        if not test_code:
            # Menggunakan pesan error yang sesuai bahasa jika memungkinkan, meskipun ini dari backend
            error_message = "AI could not generate test code. Please try a different input or prompt."
            if selected_language == 'id':
                error_message = "AI tidak dapat membuat kode test. Silakan coba input atau prompt lain."
            return jsonify({"error": error_message}), 500

        return jsonify({"test_code": test_code})

    except requests.exceptions.ConnectionError:
        error_message = "Failed to connect to Ollama. Make sure Ollama server is running on http://localhost:11434."
        if selected_language == 'id':
            error_message = "Gagal terhubung ke Ollama. Pastikan server Ollama berjalan di http://localhost:11434."
        return jsonify({"error": error_message}), 500
    except requests.exceptions.HTTPError as e:
        # Bisa lebih spesifik di sini, tapi untuk cepat kita pakai default
        error_message = f"Ollama API returned an error: {e.response.text}"
        if selected_language == 'id':
            error_message = f"API Ollama mengembalikan error: {e.response.text}"
        return jsonify({"error": error_message}), 500
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        if selected_language == 'id':
            error_message = f"Terjadi kesalahan yang tidak terduga: {str(e)}"
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)