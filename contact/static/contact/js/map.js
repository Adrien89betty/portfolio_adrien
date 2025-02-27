document.addEventListener("DOMContentLoaded", function () {
  // Map initializing centered on Montpellier.
  const map = L.map("map").setView([43.6117, 3.8772], 8);

  // Ajout des tuiles OpenStreetMap
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "© OpenStreetMap contributors",
  }).addTo(map);

  // Add pin on Montpellier
  L.marker([43.6117, 3.8772]).addTo(map)
      .bindPopup("<strong>Je suis ici ! 📍</strong>")
      .openPopup();
});
