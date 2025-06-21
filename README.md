# 🐍 Childhood Backend - Flask API

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-blueviolet)](https://render.com)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

---

This is the backend for the **Childhood in a Nutshell** app. It provides a Flask API to serve Disney character data and deliver ML-based similar character suggestions.

---

## 📦 Tech Stack

- **Python 3**
- **Flask + Flask-CORS**
- **Pandas** for data manipulation
- **Render** for deployment

---

## 🚀 Endpoints

| Route              | Description                             |
|-------------------|-----------------------------------------|
| `/characters`     | Get all Disney characters               |
| `/random`         | Get a random Disney character           |
| `/hero/<name>`    | Get a character by hero name            |
| `/similar/<name>` | Get similar characters (ML-based)       |

---

## 📂 Files

- `app.py` – Main Flask API
- `disney-characters.csv` – Character dataset
- `requirements.txt` – Python dependencies
- `Dockerfile` – Optional containerization support

---

## ▶️ Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start server
python app.py
```

---

## 🌐 Deployed API

The backend is live at:

📎 [`https://childhood-in-a-nutshell-backend.onrender.com`](https://childhood-in-a-nutshell-backend.onrender.com)

---

## 👩‍💻 Author

**Sanya Shresta Jathanna**  
[![GitHub](https://img.shields.io/badge/GitHub-SanyaShresta25-black?style=flat&logo=github)](https://github.com/SanyaShresta25)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/sanya-shresta-jathanna)
[![Portfolio](https://img.shields.io/badge/Portfolio-Website-purple)](https://sanyashresta.netlify.app/)
