import json
import xml.etree.ElementTree as ET
import os

class DataParser:
    def __init__(self, filepath):
        """Initialise le parseur avec le chemin du fichier."""
        self.filepath = filepath
        
        # Vérification défensive 
        if not os.path.exists(filepath):
            raise FileNotFoundError(f" Erreur : Le fichier '{filepath}' est introuvable.")

    def _parse_json(self):
        """Méthode interne pour lire du JSON."""
        print(f" Détection format JSON pour {self.filepath}")
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _parse_xml(self):
        """Méthode interne pour lire du XML de manière générique."""
        print(f" Détection format XML pour {self.filepath}")
        tree = ET.parse(self.filepath)
        root = tree.getroot()
        
        data = []
        # On suppose une structure simple : Racine -> Items -> Propriétés
        for child in root:
            item = {}
            # On transforme chaque sous-balise en clé/valeur
            for subchild in child:
                item[subchild.tag] = subchild.text
            data.append(item)
        return data

    def load(self):
        """Fonction principale : détecte l'extension et charge les données."""
        # os.path.splitext coupe le nom de fichier : ("data", ".json")
        _, extension = os.path.splitext(self.filepath)
        extension = extension.lower() # On met en minuscule pour éviter les soucis (.XML vs .xml)

        try:
            if extension == '.json':
                return self._parse_json()
            elif extension == '.xml':
                return self._parse_xml()
            else:
                return f" Format non supporté : {extension}"
                
        except Exception as e:
            return f" Erreur lors de la lecture : {e}"

# --- ZONE DE TEST ---
if __name__ == "__main__":
    print("--- TEST 1 : Fichier JSON ---")
    # On teste avec le fichier fusionné de l'exercice précédent
    loader1 = DataParser("merged.json")
    donnees_json = loader1.load()
    print("Résultat :", donnees_json)
    
    print("\n--- TEST 2 : Fichier XML ---")
    # On teste avec le fichier XML des livres
    loader2 = DataParser("books.xml")
    donnees_xml = loader2.load()
    print("Résultat :", donnees_xml)

    print("\n--- TEST 3 : Fichier Inexistant (Gestion d'erreur) ---")
    try:
        loader3 = DataParser("fantome.txt")
    except FileNotFoundError as e:
        print(e)