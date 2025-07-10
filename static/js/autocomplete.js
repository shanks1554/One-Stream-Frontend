const API_BASE = "https://onestream-backend.onrender.com";  // FastAPI backend
const input = document.getElementById("search-input");
const resultsBox = document.getElementById("autocomplete-results");

let debounceTimer = null;

input.addEventListener("input", () => {
  const query = input.value.trim();
  if (!query) {
    resultsBox.innerHTML = "";
    return;
  }

  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {
    fetch(`${API_BASE}/autocomplete?prefix=${encodeURIComponent(query)}&limit=6`)
      .then(res => res.json())
      .then(data => {
        resultsBox.innerHTML = "";
        for (const a of data) {
          const card = document.createElement("div");
          card.className = "autocomplete-item";

          card.innerHTML = `
            <img src="${a.poster_url}" alt="">
            <span>${a.title}</span>
          `;

          card.onclick = () => {
            window.location.href = `/anime/${encodeURIComponent(a.title)}`;
          };

          resultsBox.appendChild(card);
        }
      })
      .catch(err => {
        resultsBox.innerHTML = "";
        console.error("Autocomplete error:", err);
      });
  }, 250);
});

document.addEventListener("click", (e) => {
  if (!resultsBox.contains(e.target) && e.target !== input) {
    resultsBox.innerHTML = "";
  }
});
