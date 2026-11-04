// Thème : appliqué tout de suite, avant l'affichage de la page, pour éviter un flash blanc
var themeActuel = null;

try {
  themeActuel = localStorage.getItem("theme");
} catch (erreur) {
  // Stockage bloqué par le navigateur : le choix ne sera simplement pas mémorisé
}

if (!themeActuel) {
  themeActuel = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

document.documentElement.dataset.theme = themeActuel;

document.addEventListener("DOMContentLoaded", function () {
  // Bouton de thème
  var boutonTheme = document.getElementById("bouton-theme");

  function afficherLibelle() {
    boutonTheme.textContent = themeActuel === "dark" ? "Thème clair" : "Thème sombre";
  }

  afficherLibelle();

  boutonTheme.addEventListener("click", function () {
    themeActuel = themeActuel === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = themeActuel;
    afficherLibelle();

    try {
      localStorage.setItem("theme", themeActuel);
    } catch (erreur) {
      // Stockage bloqué : le thème change quand même sur cette page
    }
  });

  // Menu sur téléphone
  var boutonMenu = document.getElementById("bouton-menu");
  var menu = document.getElementById("menu");

  boutonMenu.addEventListener("click", function () {
    menu.classList.toggle("ouvert");
    boutonMenu.setAttribute("aria-expanded", menu.classList.contains("ouvert"));
  });
});
