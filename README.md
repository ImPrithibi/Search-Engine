# 🚀 Real-Time Web Search Engine

A professional, real-time, stateless search engine built from scratch by **Prithibi Paul**.

This project was built as an independent, full-stack, live search engine that fetches fresh web results every time a user searches — no saved index, no database, no storage.  
It delivers **fast, clean, and current search results** with a modern frontend and efficient backend.

---

## 🌟 About This Project

I built this project entirely from scratch to explore how real search engines work — starting from basic crawling, indexing, ranking, and finally turning it into a **stateless real-time search engine**.

It is:
- Fully functional
- Cleanly architected
- Minimal, but production-ready
- Uses modern tech stack

---

## 🎯 What Makes This Unique

✅ **No Database**  
✅ **No Stored Index**  
✅ **No old data — every search is fresh**  
✅ **Fully real-time**  
✅ **Fast & Lightweight**  
✅ **Professional frontend & backend separation**  
✅ **Customizable and ready to deploy**

---

## 🚀 Live Demo


```
https://search.afk.ac
```

---

## ⚙️ How It Works

Whenever a user searches:
1. The **backend fetches fresh search results live from the web** using DuckDuckGo Search API.
2. It extracts relevant page links in real-time.
3. The **frontend immediately displays these fresh links** — no old data, no index.

**It is fast, clean, and stateless.**

---

## 🏗️ Tech Stack

- **Backend:** Python, Flask, BeautifulSoup, DuckDuckGo Search API
- **Frontend:** React, TailwindCSS, Vite
- **Optional:** Docker

---

## 🛠️ Installation & Usage

### 1. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Backend will start on:
```
http://127.0.0.1:5001
```

---

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Frontend will start on:
```
http://localhost:5173
```

---

## 🌐 Production Deployment (Optional)

You can easily deploy this using:

```bash
docker-compose up --build
```

Or deploy on:
- Render
- Railway
- VPS
- Any server of your choice

---

## ✨ What You Can Search

You can search literally anything:

- `elon musk`
- `saitama`
- `solo leveling`
- `latest news`
- `python web scraping`

Every search will **fetch fresh results live from the internet.**

---

## 💡 Why I Built This

I wanted to challenge myself and build something meaningful:

✅ **Understand how search engines work under the hood**  
✅ **Practice advanced backend + frontend integration**  
✅ **Deploy a real, stateless, production-ready project**  
✅ **Go beyond CRUD apps and build something smart & live**

This project is a result of that goal.

---

## 🙌 Credits

Built from scratch by **Prithibi Paul**  
[https://www.linkedin.com/in/prithibipaul/] | [http://afk.ac/] 

---

## 📌 Next Goals (Optional)

- Add Search History (per session)
- Add pagination
- Add Redis caching
- Add AI-based ranking 

---

## 🏆 Status

✅ **Backend: Done**  
✅ **Frontend: Done**  
✅ **Stateless Real-Time Search: Done**  
✅ **Ready for Production: Done** 

---