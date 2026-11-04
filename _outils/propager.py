# Recopie le menu et le pied de page de index.html dans toutes les autres pages.
# Utilisation : python3 _outils/propager.py
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


def lire_bloc(html, nom):
    debut = "<!-- #" + nom + " -->"
    fin = "<!-- /#" + nom + " -->"
    return html.split(debut)[1].split(fin)[0]


def remplacer_bloc(html, nom, contenu):
    debut = "<!-- #" + nom + " -->"
    fin = "<!-- /#" + nom + " -->"
    avant = html.split(debut)[0]
    apres = html.split(fin)[1]
    return avant + debut + contenu + fin + apres


accueil = (RACINE / "index.html").read_text(encoding="utf-8")
menu = lire_bloc(accueil, "header").replace(' aria-current="page"', "")
pied = lire_bloc(accueil, "footer")

for page in sorted(RACINE.glob("*.html")):
    if page.name == "index.html":
        continue

    # Le menu de chaque page signale la page en cours
    lien = '<a href="' + page.name + '"'
    menu_page = menu.replace(lien, lien + ' aria-current="page"', 1)

    html = page.read_text(encoding="utf-8")
    html = remplacer_bloc(html, "header", menu_page)
    html = remplacer_bloc(html, "footer", pied)
    page.write_text(html, encoding="utf-8")
    print("Mis à jour :", page.name)
