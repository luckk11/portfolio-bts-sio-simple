# Contrôle le site avant de le publier.
# Utilisation : python3 _outils/verifier.py
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
BALISES = ["section", "div", "article", "aside", "nav", "main", "table", "ul", "li", "figure", "details"]
POIDS_MAX_KO = 400

alertes = []
pages = sorted(RACINE.glob("*.html"))

for page in pages:
    html = page.read_text(encoding="utf-8")

    # Liens cassés
    for lien in re.findall(r'(?:src|href)="([^"]+)"', html):
        if lien.startswith(("http", "mailto:", "tel:", "#")):
            continue
        if not (RACINE / lien.split("#")[0]).exists():
            alertes.append(page.name + " : lien cassé -> " + lien)

    # Images sans texte alternatif
    for image in re.findall(r"<img[^>]*>", html):
        if "alt=" not in image:
            alertes.append(page.name + " : image sans alt -> " + image)

    # Un seul titre principal
    if len(re.findall(r"<h1[\s>]", html)) != 1:
        alertes.append(page.name + " : il faut exactement un h1")

    # Identifiants en double
    identifiants = re.findall(r'\sid="([^"]+)"', html)
    for identifiant in set(identifiants):
        if identifiants.count(identifiant) > 1:
            alertes.append(page.name + " : identifiant en double -> " + identifiant)

    # Balises mal fermées
    for balise in BALISES:
        ouvertes = len(re.findall("<" + balise + r"[\s>]", html))
        fermees = html.count("</" + balise + ">")
        if ouvertes != fermees:
            alertes.append(page.name + " : balise " + balise + " mal fermée")

    # Champs à compléter
    nombre = html.count('class="todo"')
    if nombre > 0:
        print(page.name + " : " + str(nombre) + " champ(s) à compléter")

# Images trop lourdes
for image in (RACINE / "assets" / "img").iterdir():
    poids = image.stat().st_size / 1024
    if poids > POIDS_MAX_KO:
        alertes.append("image trop lourde : " + image.name)

print()
print(str(len(pages)) + " page(s) contrôlée(s)")
if alertes:
    print("ALERTES :")
    for alerte in alertes:
        print(" -", alerte)
else:
    print("Aucune alerte.")
