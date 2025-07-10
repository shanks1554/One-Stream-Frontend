const loader = document.getElementById("backend-loader");
const BACKEND_PING_URL = "https://onestream-backend.onrender.com/ping";

fetch(BACKEND_PING_URL, { cache: "no-store" })
  .then((res) => res.json())
  .then((data) => {
    console.log("Backend awake:", data);
    loader.style.display = "none";
  })
  .catch((err) => {
    console.warn("Backend wake-up failed:", err);
    loader.querySelector("p").textContent = "Still waking up the backend...";
    setTimeout(() => {
      loader.style.display = "none"; // hide after 10s regardless
    }, 10000);
  });
