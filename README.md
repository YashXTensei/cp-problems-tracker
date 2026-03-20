# 📊 CP Problem Tracker (Full Stack Flask + API)

A structured and scalable Flask-based web application to track competitive programming problems (Codeforces, LeetCode, etc.) with a clean UI and a powerful backend API.

This project evolved from a basic CRUD tracker into a **modular backend system with filtering, pagination, AJAX interactions, and REST-style API design**.

---

## 🚀 Features

### 🔐 Authentication

* User registration, login & logout
* Secure session management (Flask-Login)

### 📝 Problem Management

* Add, edit, delete problems
* Track rating, difficulty, platform

### ⭐ Productivity Tools

* Mark problems as Favorite ❤️
* Mark problems as Completed ✅

### 🔍 Filtering & Search

* Search by question number
* Filter by platform & difficulty
* Sort by rating

### 📊 Dashboard

* Total problems
* Completed problems
* Favorite problems
* Completion percentage
* Last activity tracking

### ⚡ Modern UI

* AJAX-based toggles (no reload)
* Toast notifications instead of flash
* Dynamic UI updates

### 🔌 API (Backend Ready)

* Get problems via API
* Filtering & pagination support
* JSON-based responses
* Ready for frontend/mobile integration

---

## 🛠 Tech Stack

* **Backend:** Flask, SQLAlchemy
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite
* **Authentication:** Flask-Login

---

## 📡 API Endpoints

### Get all problems

GET /api/problems

### With filters & pagination

GET /api/problems?platform=Codeforces&difficulty=Easy&page=1

---

## 📂 Project Structure

app/
│── models.py
│── extensions.py
│── routes/
│   ├── main.py
│   ├── auth.py
│── templates/
│── static/
│── **init**.py

run.py
config.py
requirements.txt
README.md

---

## ⚙️ Setup & Run

```bash
git clone https://github.com/YashXTensei/cp-problem-tracker.git
cd cp-problem-tracker
pip install -r requirements.txt
python run.py
```

Open in browser:
http://127.0.0.1:5000/

---

## 🧠 Learning Highlights

* Built REST-style API with filtering & pagination
* Implemented AJAX for real-time UI updates
* Designed modular Flask architecture using Blueprints
* Improved UX using toast notifications
* Applied backend concepts like data normalization & separation of concerns

---

## 🔮 Future Improvements

* Full API CRUD (PUT/DELETE)
* React frontend integration
* Advanced analytics dashboard

---

## 📌 Author

Yash Mittal
Competitive Programmer + Backend Learner 🚀
