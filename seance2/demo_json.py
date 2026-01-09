import json

print("--- 1. Lecture du fichier JSON ---")

# 'r' = read (lecture), encoding='utf-8' est CRUCIAL sur Windows
with open("data.json", "r", encoding="utf-8") as f:
    # json.load() transforme le fichier texte en dictionnaire Python
    contenu = json.load(f)

print(f"Type de données : {type(contenu)}")
print("Contenu brut :", contenu)

print("\n--- 2. Manipulation des données ---")
# On manipule ça comme un dictionnaire classique
print(f"Cours actuel : {contenu['cours']}")

# Ajoutons un étudiant
contenu['etudiants'].append("David")
print("Étudiants mis à jour :", contenu['etudiants'])

print("\n--- 3. Sauvegarde dans un nouveau fichier ---")
# 'w' = write (écriture)
with open("data_updated.json", "w", encoding="utf-8") as f:
    # indent=4 permet d'avoir un fichier lisible par un humain
    # ensure_ascii=False permet de garder les accents (é, à, etc.)
    json.dump(contenu, f, indent=4, ensure_ascii=False)

print(" Sauvegarde terminée dans 'data_updated.json'")