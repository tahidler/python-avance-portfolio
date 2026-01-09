import json
import xml.etree.ElementTree as ET

print("Création des fichiers de données pour la séance...")

# 1. Création de data.json (pour la démo lecture/écriture)
data_simple = {
    "cours": "Python Avancé",
    "seance": 2,
    "etudiants": ["Alice", "Bob", "Charlie"],
    "actif": True
}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data_simple, f, indent=4, ensure_ascii=False)
print(" data.json créé.")

# 2. Création de books.xml (pour la démo XML)
root = ET.Element("library")
b1 = ET.SubElement(root, "book")
ET.SubElement(b1, "id").text = "1"
ET.SubElement(b1, "title").text = "Le Petit Prince"
ET.SubElement(b1, "author").text = "Antoine de Saint-Exupéry"
ET.SubElement(b1, "year").text = "1943"

b2 = ET.SubElement(root, "book")
ET.SubElement(b2, "id").text = "2"
ET.SubElement(b2, "title").text = "1984"
ET.SubElement(b2, "author").text = "George Orwell"
ET.SubElement(b2, "year").text = "1949"

tree = ET.ElementTree(root)
ET.indent(tree, space="    ", level=0) # Pour faire joli (Python 3.9+)
tree.write("books.xml", encoding="utf-8", xml_declaration=True)
print(" books.xml créé.")

# 3. Création de data1.json et data2.json (pour l'exercice de fusion)
d1 = [
    {"id": 101, "nom": "Alice", "role": "Data Scientist"},
    {"id": 102, "nom": "Bob", "role": "DevOps"}
]
d2 = [
    {"id": 103, "nom": "Charlie", "role": "Manager"},
    {"id": 101, "nom": "Alice", "role": "Data Scientist"} # Doublon volontaire
]

with open("data1.json", "w", encoding="utf-8") as f:
    json.dump(d1, f, indent=4)
with open("data2.json", "w", encoding="utf-8") as f:
    json.dump(d2, f, indent=4)
print(" data1.json et data2.json créés.")

print("\n--- Tout est prêt ! Tu peux commencer les exercices. ---")