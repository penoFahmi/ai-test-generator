# AI-Driven Test Case Generator

This web application helps developers automatically create **Python unit tests** using the power of **Artificial Intelligence (Google Gemini)**. This project was developed as part of a final academic assignment (UAS).

---

## Key Features

* **Automated Unit Test Generation:** Input your Python functions, and the application will generate relevant **pytest** code.
* **Multi-Language Support:** Choose between English or Indonesian prompts for the AI, which also reflects in the application's interface.
* **Intuitive User Interface:** A modern and responsive UI, built with Next.js and Shadcn UI.
* **Google Gemini Integration:** Leverages Google's advanced AI models for fast and accurate test generation.
* **"Copy Test Code" Feature:** Easily copy the generated test code to your clipboard with a single click.

---

## Application View

![Screenshot of the AI Test Generator Application](link_gambar_screenshot_anda.png)
*(Replace `link_gambar_screenshot_anda.png` with the URL of your application's screenshot. You can upload it to GitHub or another online service.)*

---

## System Requirements

Make sure your system meets the following requirements before running the application:

* **Python 3.x:** To run the Flask backend.
* **Node.js & npm/yarn:** To run the Next.js frontend.
* **Google Gemini API Key:** Obtain your API key from [Google AI Studio](https://aistudio.google.com/app/apikey). This is **essential** for the application to function.

---

## How to Run the Project

Follow these steps to set up and run the application locally.

### 1. Backend Setup (Flask)

1.  **Navigate to the Backend Directory:**
    ```bash
    cd your_project_folder/backend # Replace with the actual path to your backend folder
    ```
2.  **Install Python Dependencies:**
    ```bash
    pip install Flask requests flask-cors google-generativeai python-dotenv
    ```
3.  **Configure Gemini API Key (`.env`):**
    * In your `backend/` folder, create a new file named **`.env`**.
    * Add the following line to it, replacing `YOUR_API_KEY_HERE` with your actual Google Gemini API key:
        ```
        GEMINI_API_KEY=YOUR_API_KEY_HERE
        ```
    * **Important:** Do not include quotes around your API key. Ensure the `.env` file is in the same `backend/` folder as `app.py`.
4.  **Run the Backend Server:**
    ```bash
    python app.py # Replace app.py if your Flask file has a different name
    ```
    The backend server will run on `http://localhost:5000`.

### 2. Frontend Setup (Next.js)

1.  **Navigate to the Frontend Directory:**
    ```bash
    cd your_project_folder/frontend # Replace with the actual path to your frontend folder
    ```
2.  **Install Node.js Dependencies:**
    ```bash
    npm install # or yarn install
    ```
3.  **Run the Frontend Application:**
    ```bash
    npm run dev # or yarn dev
    ```
    The frontend application will run on `http://localhost:3000` (or your default Next.js port).

---

## How to Use the Application

1.  Ensure both your Flask backend and Next.js frontend servers are running.
2.  Open your browser and access `http://localhost:3000`.
3.  Select your preferred language (English/Indonesia) from the dropdown.
4.  Enter your Python function(s) into the text input area.
5.  Click the **"Generate Tests" / "Buat Test"** button.
6.  The generated Pytest unit code will appear below. You can copy it directly using the **"Copy Test Code" / "Salin Kode Test"** button.

---

## Benefits of the Application

The **"AI-Driven Test Case Generator"** application is highly beneficial for developers and students because it:

* **Boosts Efficiency:** Significantly reduces the time and effort required to write manual unit tests, accelerating the development workflow.
* **Ensures Code Quality:** Helps verify code functionality by providing automated test foundations, allowing earlier bug detection and improving overall software quality.
* **Accelerates Development Process:** Automates repetitive testing tasks, freeing up time for innovation and new feature development.
* **Simplifies Learning Testing:** Serves as a practical tool for students or junior developers to understand the structure and best practices of unit testing.

---

## Developed By

**Peno** - **NIM 221220095**

---