// main.js — placeholder for future features
console.log("Main JS loaded.");

document.addEventListener("DOMContentLoaded",()=>{
  const obs=new IntersectionObserver((ents)=>ents.forEach(e=>e.isIntersecting&&e.target.classList.add("appear")),
                                    {threshold:.1});
  document.querySelectorAll(".anime-card").forEach(c=>obs.observe(c));
});
