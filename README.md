# 🎬 One Stream Frontend

The frontend for the **One Stream Anime Recommender**, a beautiful, modern web interface that helps users discover anime through genre-based exploration and watched-title recommendations.

> 💡 This frontend is built with **Flask**, fully responsive with modern UI/UX using CSS, JavaScript, and animated elements. It consumes a separately hosted FastAPI backend.

---

## 🚀 Live Preview

- 🔗 Backend API: [https://onestream-backend.onrender.com](https://onestream-backend.onrender.com)
- 🔗 Frontend (if deployed): *[Add your frontend link here]*

---

## 🖼️ Features

- 🔍 **Autocomplete Search** with poster thumbnails
- 📂 **Explore by Genre** (multi-select)
- ⭐ **Personal Recommendations** based on watched anime
- 🎴 **Anime Detail Page** with synopsis, scores, episodes, and more
- 🎨 Animated UI with modern neumorphic style and glassmorphism

---

## 🛠️ Tech Stack

- **Frontend Framework:** Flask (Python)
- **Styling:** HTML, CSS, JavaScript (with transitions and effects)
- **API Integration:** Consumes FastAPI backend via REST calls
- **Fonts & Icons:** Google Fonts, Custom SVGs

---

## 🧑‍💻 Local Development

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/onestream-frontend.git
cd onestream-frontend
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
python app.py
```

The site will be live at `http://localhost:5000`

---

## 🌐 Deployment

You can deploy this frontend separately (e.g. using Render, Netlify, Vercel). Just make sure to:

- Set `BACKEND_URL` in `app.py` to your deployed FastAPI backend.
- Ensure CORS is enabled on the backend.

---

## 📂 Folder Structure

```
onestream-frontend/
├── static/             # CSS, JS, images
├── templates/          # HTML templates (Jinja2)
├── app.py              # Flask entry point
├── requirements.txt
└── README.md
```

---

## 📃 License

MIT License. Free to use with attribution.