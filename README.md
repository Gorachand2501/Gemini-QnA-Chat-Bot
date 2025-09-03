# 🤖 Gemini Q&A Chat-Bot

This project is a **Q&A chatbot** powered by **Google Gemini (Generative AI)** and **Streamlit**.  
It uses the **Gemini Pro model (`gemini-1.5-flash`)** to generate responses in real time with streaming output.

---

## 🎯 Objective
Provide an **interactive chatbot experience** where users can ask questions and get instant, AI-powered answers using Google's Gemini API.

---

## ✅ Features
- 🧠 Powered by **Google Gemini Pro (1.5 Flash)**.  
- 💬 Maintains **chat history** across interactions.  
- ⚡ Streams AI responses with a **blinking cursor effect**.  
- 🎨 Built with a **clean Streamlit UI**.  
- 🔒 Secure API key handling with **dotenv**.  

---

## 🛠️ Tech Stack
- **Python 3.x**  
- **Streamlit**  
- **Google Generative AI SDK (`google-generativeai`)**  
- **python-dotenv**  

---

## 🧠 Model
- **Model Used**: `models/gemini-1.5-flash`  
- **Interaction Mode**: `start_chat` with conversation history.  
- **Streaming Responses** for a more natural chat feel.  

---

## 🚀 How to Run

### Step 1: Clone the Repository & Install Dependencies
```bash
git clone <repository-url>
cd gemini-chatbot
pip install -r requirements.txt
```

### Step 2: Set Up Environment Variables
Create a `.env` file in the root directory and add your Google API key.

```env
GOOGLE_API_KEY="your_google_api_key_here"
```
### Step 3: Launch the App
Run the Streamlit application:

```bash
streamlit run app.py
```

## 📂 Project Structure

```plaintext
├── app.py             # Main Streamlit chatbot app
├── requirements.txt   # Python dependencies
└── .env               # Environment variables (Google API Key)
```

## ⚠️ Disclaimer

This project is for **educational purposes only**.  
Do **not** share your API key publicly or commit it to GitHub.

