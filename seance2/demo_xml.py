import xml.etree.ElementTree as ET

print("--- 1. Lecture du XML (Parsing) ---")
# On charge l'arbre (Tree) en mémoire
tree = ET.parse("books.xml")

# On récupère la racine de l'arbre (<library>)
root = tree.getroot()

print(f"Racine du document : <{root.tag}>")
print(f"Nombre de livres trouvés : {len(root)}")

print("\n--- 2. Parcours des données ---")
# On boucle sur chaque enfant <book> de la racine
for book in root.findall("book"):
    # book est un Element, on cherche ses sous-éléments
    titre = book.find("title").text
    auteur = book.find("author").text
    print(f"📖 {titre} -- écrit par {auteur}")

print("\n--- 3. Modification et Sauvegarde ---")
# Création d'un nouvel élément <book>
new_book = ET.Element("book")

# Ajout des sous-éléments (ID, Titre, Auteur...)
ET.SubElement(new_book, "id").text = "3"
ET.SubElement(new_book, "title").text = "Dune"
ET.SubElement(new_book, "author").text = "Frank Herbert"
ET.SubElement(new_book, "year").text = "1965"

# On attache ce nouveau livre à la racine <library>
root.append(new_book)

# Sauvegarde
# xml_declaration=True ajoute la ligne <?xml version...?> en haut
tree.write("books_updated.xml", encoding="utf-8", xml_declaration=True)

print(" Sauvegarde terminée dans 'books_updated.xml'")