// Menu sur téléphone
var boutonMenu = document.getElementById("bouton-menu");
var menu = document.getElementById("menu");

boutonMenu.addEventListener("click", function () {
  menu.classList.toggle("ouvert");
  boutonMenu.setAttribute("aria-expanded", menu.classList.contains("ouvert"));
});

// Formulaire de contact : ouvre la messagerie du visiteur avec le message pré-rempli
var formulaire = document.getElementById("form-contact");

if (formulaire) {
  formulaire.addEventListener("submit", function (evenement) {
    evenement.preventDefault();

    var objet = document.getElementById("objet").value;
    var corps =
      "Nom : " + document.getElementById("nom").value + "\n" +
      "E-mail : " + document.getElementById("email").value + "\n" +
      "Organisation : " + (document.getElementById("organisation").value || "—") + "\n" +
      "Objet : " + objet + "\n\n" +
      document.getElementById("message").value;

    window.location.href =
      "mailto:zhg.luc2909@gmail.com" +
      "?subject=" + encodeURIComponent("[Portfolio] " + objet) +
      "&body=" + encodeURIComponent(corps);

    document.getElementById("message-envoi").textContent =
      "Votre logiciel de messagerie va s'ouvrir avec le message pré-rempli. Il ne reste qu'à l'envoyer.";
  });
}
