from pathlib import Path
from urllib.parse import quote_plus, unquote_plus   # NOTE: use unquote_plus here
from flask import Flask, render_template, send_from_directory, request
import requests

# ------------------------------------------------------------------------------------
# Config
# ------------------------------------------------------------------------------------
APP_ROOT        = Path(__file__).resolve().parent
STATIC_FOLDER   = APP_ROOT / "static"
TEMPLATE_FOLDER = APP_ROOT / "templates"
BACKEND_URL     = "https://onestream-backend.onrender.com"           # FastAPI host

app = Flask(
    __name__,
    static_folder=str(STATIC_FOLDER),
    template_folder=str(TEMPLATE_FOLDER),
)

# ------------------------------------------------------------------------------------
# Helper data & Jinja filter
# ------------------------------------------------------------------------------------
GENRES = [
    "Action", "Adventure", "Comedy", "Drama", "Fantasy",
    "Horror", "Mystery", "Romance", "Sci-Fi", "Slice of Life",
    "Sports", "Supernatural"
]

@app.template_filter("urlencode")
def _jinja_urlencode(s: str) -> str:
    """URL‑encode a string for use in <a href>.  Uses + for spaces."""
    return quote_plus(s or "")

# ------------------------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------------------------
@app.route("/")
def home():
    # Example genres – replace this with real data if needed
    popular_genres = ["Action", "Romance", "Fantasy", "Thriller", "Comedy"]
    
    return render_template("home.html", popular_genres=popular_genres)

@app.route("/explore")
def explore():
    return render_template("explore.html")


# ---- Multi‑genre explorer -----------------------------------------------------------
@app.route("/explore/genre", methods=["GET", "POST"])
def genre_explore():
    selected = request.form.getlist("genres")
    anime_list = []

    if selected:
        try:
            resp = requests.post(
                f"{BACKEND_URL}/genres",
                json={"genres": selected, "k": 10},
                timeout=5,
            )
            resp.raise_for_status()
            anime_list = resp.json()
        except Exception as e:
            print("Genre fetch error:", e)

    return render_template(
        "genre.html",
        genres=GENRES,
        selected=selected,
        anime_list=anime_list,
    )


# ---- Watched‑list recommender -------------------------------------------------------
@app.route("/explore/watched", methods=["GET", "POST"])
def recommend_by_watched():
    liked_raw = ""
    selected_genres = []
    recommended = []

    if request.method == "POST":
        liked_raw = request.form.get("liked_titles", "")
        selected_genres = request.form.getlist("genres")
        liked_titles = [t.strip() for t in liked_raw.split(",") if t.strip()]

        if liked_titles:
            payload = {
                "liked_titles": liked_titles,
                "genre_filter": selected_genres or None,
                "top_n": 10,
            }
            try:
                res = requests.post(f"{BACKEND_URL}/recommend", json=payload, timeout=8)
                res.raise_for_status()
                recommended = res.json()
            except Exception as e:
                print("Recommendation error:", e)

            # 🔑  CLEAR the form inputs for the next render
            liked_raw = ""
            selected_genres = []

    return render_template(
        "recommend.html",
        liked_titles=liked_raw,        # now an empty string
        genres=GENRES,
        selected_genres=selected_genres,
        recommended=recommended,
    )


# ---- Anime detail (fixed decoding) --------------------------------------------------
@app.route("/anime/<path:title>", endpoint="anime_detail")
def anime_detail(title):
    safe_title = unquote_plus(title)  # converts "+" back to space
    try:
        res = requests.get(f"{BACKEND_URL}/meta", params={"title": safe_title}, timeout=5)
        res.raise_for_status()
        meta = res.json()
    except Exception as e:
        print("Meta fetch error:", e)
        return render_template("error.html", message="Anime not found.")

    return render_template("anime_detail.html", anime=meta)


# ---- Static logo --------------------------------------------------------------------
@app.route("/logo.svg")
def logo():
    return send_from_directory(STATIC_FOLDER / "img", "logo.svg")


# ------------------------------------------------------------------------------------
# Dev entry point
# ------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
