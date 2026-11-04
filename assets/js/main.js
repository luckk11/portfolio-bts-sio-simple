// Menu sur téléphone
var boutonMenu = document.getElementById("bouton-menu");
var menu = document.getElementById("menu");

boutonMenu.addEventListener("click", function () {
  menu.classList.toggle("ouvert");
  boutonMenu.setAttribute("aria-expanded", menu.classList.contains("ouvert"));
});
