'use client';

import { useState } from 'react';
import { Textarea } from '@/components/ui/textarea';
import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';
import { Card, CardHeader, CardContent, CardTitle, CardDescription, CardFooter } from '@/components/ui/card';
import { Separator } from '@/components/ui/separator';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

export default function Home() {
  const [code, setCode] = useState('');
  const [testCode, setTestCode] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [language, setLanguage] = useState('en');

  const translations = {
    en: {
      title: "AI-Driven Test Case Generator",
      description: "Generate Python unit tests automatically using the power of local AI (Gemini).",
      inputLabel: "Enter Your Python Function:",
      placeholder: "Example:\ndef add(a, b):\n  return a + b\n\ndef is_prime(num):\n  if num < 2: return False\n  for i in range(2, int(num**0.5) + 1):\n    if num % i == 0: return False\n  return True",
      buttonGenerating: "Generating Tests...",
      buttonGenerate: "Generate Tests",
      generatedTestLabel: "Generated Test Code:",
      copyHint: "Copy this code and save it as a Python test file (e.g., `test_your_function.py`) in your project.",
      copyButton: "Copy Test Code",
      footer: "Built with ❤️ using Flask, Next.js, Shadcn UI, and Gemini.",
      languageSelectLabel: "Select Language:",
      errorNoCode: "No code provided. Please enter your Python function.",
      errorConnection: "Failed to connect to the backend server. Make sure your Flask server is running.",
      errorAIResponse: "AI could not generate test code. Please try a different input or prompt.",
      errorGeneric: "An unexpected error occurred. Please try again."
    },
    id: {
      title: "Pembuat Test Case Otomatis Berbasis AI",
      description: "Buat unit test Python secara otomatis menggunakan kekuatan AI lokal (Gemini).",
      inputLabel: "Masukkan Fungsi Python Anda:",
      placeholder: "Contoh:\ndef tambah(a, b):\n  return a + b\n\ndef adalah_prima(num):\n  if num < 2: return False\n  for i in range(2, int(num**0.5) + 1):\n    if num % i == 0: return False\n  return True",
      buttonGenerating: "Membuat Test...",
      buttonGenerate: "Buat Test",
      generatedTestLabel: "Kode Test yang Dihasilkan:",
      copyHint: "Salin kode ini dan simpan sebagai file test Python (misal: `test_fungsi_anda.py`) di proyek Anda.",
      copyButton: "Salin Kode Test",
      footer: "Dibangun dengan ❤️ menggunakan Flask, Next.js, Shadcn UI, dan Gemini.",
      languageSelectLabel: "Pilih Bahasa:",
      errorNoCode: "Tidak ada kode yang diberikan. Harap masukkan fungsi Python Anda.",
      errorConnection: "Gagal terhubung ke server backend. Pastikan server Flask Anda berjalan.",
      errorAIResponse: "AI tidak dapat membuat kode test. Silakan coba input atau prompt lain.",
      errorGeneric: "Terjadi kesalahan yang tidak terduga. Silakan coba lagi."
    }
  };

  const t = translations[language];

  const handleGenerateTest = async () => {
    setIsLoading(true);
    setError('');
    setTestCode('');

    if (!code.trim()) {
      setError(t.errorNoCode);
      setIsLoading(false);
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/generate-test', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code, language }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || t.errorGeneric);
      }

      const data = await response.json();
      setTestCode(data.test_code);
    } catch (err) {
      if (err instanceof Error) {
        if (err.message.includes("Failed to fetch") || err.message.includes("NetworkError")) {
          setError(t.errorConnection);
        } else if (err.message.includes("AI could not generate test code")) {
          setError(t.errorAIResponse);
        } else {
          setError(err.message);
        }
      } else {
        setError(t.errorGeneric);
      }
      console.error('Error generating test:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 to-indigo-100 flex items-center justify-center p-4">
      <Card className="w-full max-w-3xl shadow-xl border border-gray-200">
        <CardHeader className="p-6 pb-4">
          <CardTitle className="text-3xl font-extrabold text-center text-gray-900">{t.title}</CardTitle>
          <CardDescription className="text-center mt-2 text-gray-600">
            {t.description}
          </CardDescription>
        </CardHeader>
        <CardContent className="p-6 space-y-6">
          <div className="flex justify-end mb-4 items-center">
            <Label htmlFor="language-select" className="mr-2 self-center">{t.languageSelectLabel}</Label>
            <Select value={language} onValueChange={setLanguage}>
              <SelectTrigger id="language-select" className="w-[120px]">
                <SelectValue placeholder="Select a language" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="en">English</SelectItem>
                <SelectItem value="id">Indonesia</SelectItem>
              </SelectContent>
            </Select>
          </div>

          <div>
            <Label htmlFor="code-input" className="mb-2 block text-lg font-medium text-gray-800">{t.inputLabel}</Label>
            <Textarea
              id="code-input"
              placeholder={t.placeholder}
              value={code}
              onChange={(e) => setCode(e.target.value)}
              rows={12}
              className="font-mono text-base p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-indigo-500"
            />
          </div>
          <Button
            onClick={handleGenerateTest}
            disabled={isLoading || !code.trim()}
            className="w-full py-3 text-lg font-semibold bg-indigo-600 hover:bg-indigo-700 text-white transition-colors duration-200"
          >
            {isLoading ? t.buttonGenerating : t.buttonGenerate}
          </Button>

          {error && (
            <div className="text-red-600 bg-red-50 p-3 rounded-md text-center border border-red-200">{error}</div>
          )}

          {testCode && (
            <>
              <Separator className="my-6 bg-gray-300" />
              <div>
                <Label className="mb-2 block text-lg font-medium text-gray-800">{t.generatedTestLabel}</Label>
                <pre className="bg-gray-800 text-green-300 p-4 rounded-lg overflow-auto font-mono text-sm shadow-inner max-h-[400px]">
                  <code>{testCode}</code>
                </pre>
                <p className="text-sm text-gray-500 mt-3 text-center">
                  {t.copyHint}
                </p>
                <Button
                  onClick={() => navigator.clipboard.writeText(testCode)}
                  className="mt-4 w-full py-3 text-lg font-semibold bg-blue-600 hover:bg-blue-700 text-white transition-colors duration-200"
                >
                  {t.copyButton}
                </Button>
              </div>
            </>
          )}
        </CardContent>
        <CardFooter className="p-6 pt-4 text-center text-sm text-gray-500">
          {t.footer}
        </CardFooter>
      </Card>
    </div>
  );
}