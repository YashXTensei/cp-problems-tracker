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

<img width="1292" height="873" alt="Screenshot 2026-03-20 233941" src="https://github.com/user-attachments/assets/0200c020-ca5c-4558-9f90-d64d0f28472b" />


### ⭐ Productivity Tools

* Mark problems as Favorite ❤️
* Mark problems as Completed ✅

### 🔍 Filtering & Search

* Search by question number
* Filter by platform & difficulty
* Sort by rating

* <img width="1526" height="911" alt="Screenshot 2026-03-21 001654" src="https://github.com/user-attachments/assets/27de12b2-ecbf-4542-9aee-378163e86906" />

### 📊 Dashboard

* Total problems
* Completed problems
* Favorite problems
* Completion percentage
* Last activity tracking

* <img width="1784" height="895" alt="Screenshot 2026-03-21 010132" src="https://github.com/user-attachments/assets/8a3ac372-17fc-4600-b2b1-4b30c1eb5b71" />

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
