# 📊 CP Problems Tracker

A structured Flask-based web application to track competitive programming problems (Codeforces, LeetCode, etc.).

Built as part of my structured Flask learning journey (Day 1–4 of rebuilding Flask fundamentals with clean architecture).

---

## 🚀 Features

- Add new problems
- Edit existing problems
- Delete problems
- Mark problems as completed
- Mark problems as favorite
- Ordered view (Favorites first, then recent activity)
- Flash messages for user actions
- Clean Blueprint-based structure
- SQLAlchemy ORM integration

---

## 🛠 Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML + CSS

---

## 📂 Project Structure

app/
│── models.py
│── extensions.py
│── routes/main.py (Blueprint)
│── templates/
|── __init__.py
│── static/

run.py
config.py
requirements.txt
README.md

## 📸 Screenshots

### Home Page
![Home Page]<img width="1897" height="910" alt="home png" src="https://github.com/user-attachments/assets/e3e1de6f-eb8e-4a01-8391-e4d55fa1433a" />


### Add Question Page
![Add Page]<img width="1918" height="905" alt="add png" src="https://github.com/user-attachments/assets/261bef87-034e-46fb-9ebe-6c2d31f7f70e" />


---

## ⚙️ How To Run

1. Clone the repository: https://github.com/YashXTensei/cp-problems-tracker.git

2. Create a virtual environment (recommended):


3. Activate the environment and install dependencies:


4. Run the application: python run.py


5. Open in browser: http://127.0.0.1:5000/


---

## 📈 Learning Context

This project was built after:

- 6 initial days of learning Flask, HTML, CSS (single-file SQLite project)
- A break for competitive programming focus
- Returning to Flask with structured architecture:
  - SQLAlchemy ORM
  - Blueprint separation
  - Clean routing
  - Better project organization

Time taken for this project: ~3 hours (including debugging and structure setup).

---

## 🔮 Future Improvements

- Normalize platform using database relationships
- Add filtering and search
- Add statistics dashboard
- Convert to API-based backend
- Improve UI consistency

---

## 📌 Author

Yash  
2nd Semester | Competitive Programming + Backend Learning Journey

