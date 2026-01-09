import xml.etree.ElementTree as ET
import json

print(" Début de la conversion XML -> JSON...")

# 1. Charger le fichier XML (books_updated.xml)
tree = ET.parse("books_updated.xml")
root = tree.getroot()

ma_bibliotheque = []

# 2. Parcourir chaque livre
for book in root.findall("book"):
    # Récupération des données brutes
    titre = book.find("title").text
    auteur = book.find("author").text
    id_txt = book.find("id").text
    annee_txt = book.find("year").text

    # Dictionnaire propre (avec conversions)
    livre_dict = {
        "id": int(id_txt),
        "titre": titre,
        "auteur": auteur,
        "annee": int(annee_txt)
    }

    # Ajoute le dictionnaire à la liste
    ma_bibliotheque.append(livre_dict)

# 3. Sauvegarder la liste 'ma_bibliotheque' dans 'books.json'
with open("books.json", "w", encoding="utf-8") as f:
    json.dump(ma_bibliotheque, f, indent=4, ensure_ascii=False)

print(f" Conversion terminée. {len(ma_bibliotheque)} livres exportés.")
