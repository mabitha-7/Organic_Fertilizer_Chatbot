# 🌱 Organic Fertilizer Recommendation Chatbot

## 📌 Project Overview

The **Organic Fertilizer Recommendation Chatbot** is a web-based application designed to assist farmers by providing recommendations for crops, organic fertilizers, and solutions for plant diseases.

This chatbot interacts with users in **Tamil language** and provides intelligent responses based on user input.

---

## 🎯 Objectives

* To help farmers choose suitable crops based on soil type
* To recommend eco-friendly organic fertilizers
* To provide solutions for common plant diseases
* To build a simple and user-friendly chatbot system

---

## 🧠 Features

* 🌾 Soil-based crop recommendation
* 🌿 Organic fertilizer suggestions
* 🍂 Plant disease identification and remedies
* 💬 Tamil language chatbot interaction
* 🤖 Fuzzy matching for handling spelling mistakes
* ⚡ Fast response using Flask API

---

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Libraries:**

  * Flask
  * Flask-CORS
  * RapidFuzz

---

## 📂 Project Structure

```
Organic_Fertilizer_Chatbot/
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│   └── dataset files
│
└── README.md
```

---

## ⚙️ How It Works

1. User enters a message in the chatbot
2. The request is sent to the Flask backend
3. The system checks:

   * Soil type
   * Fertilizer query
   * Disease-related query
4. If input is not exact, **fuzzy matching** is used
5. The chatbot returns the appropriate response

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Organic_Fertilizer_Chatbot.git
cd Organic_Fertilizer_Chatbot
```

### 2️⃣ Install Dependencies

```bash
pip install flask flask-cors rapidfuzz
```

### 3️⃣ Run the Backend

```bash
cd backend
python app.py
```

### 4️⃣ Run the Frontend

* Open `index.html` in your browser

---

## 💡 Example Inputs

* "red soil"
* "fertilizer for black soil"
* "yellow leaf problem"
* "hi"

---

## 📊 Output

* Crop recommendations
* Organic fertilizer suggestions
* Disease solutions

---

## 🔮 Future Enhancements

* 🌐 Multi-language support
* 📱 Mobile application
* 🤖 Integration with Machine Learning models
* 📡 Real-time weather-based suggestions

---

## 👩‍💻 Author

**Mabitha M**
B.Tech (AI & ML) Student

---

## 📜 License

This project is for educational purposes only.
