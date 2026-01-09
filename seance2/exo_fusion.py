import json

print(" Fusion des fichiers data1.json et data2.json...")

fichiers_a_fusionner = ["data1.json", "data2.json"]

# Dictionnaire temporaire pour stocker les uniques : { ID : Données }
db_temporaire = {}

for nom_fichier in fichiers_a_fusionner:
    with open(nom_fichier, "r", encoding="utf-8") as f:
        contenu = json.load(f)
        
        # Parcours de la liste d'employés
        for employe in contenu:
            id_unique = employe['id']
            
            # C'est ici que la magie opère :
            # On stocke l'employé dans le dictionnaire avec son ID comme clé.
            # Si l'ID existe déjà, la nouvelle version remplace l'ancienne automatiquement.
            db_temporaire[id_unique] = employe

# On a fini la déduplication, on repasse en format liste pour le JSON final
resultat_final = list(db_temporaire.values())

# Sauvegarde
with open("merged.json", "w", encoding="utf-8") as f:
    json.dump(resultat_final, f, indent=4, ensure_ascii=False)

print(f" Fusion terminée. {len(resultat_final)} éléments uniques sauvegardés.")
print("Vérifie que Alice n'apparait qu'une seule fois dans 'merged.json' !")