import json

# Ouvrir l'inventaire depuis un fichier JSON
def ouvrir_inventaire(path="data/inventaire.json"):
    with open(path, 'r', encoding='utf-8') as fichier:
        inventaire = json.load(fichier)
    return inventaire

# Écrire l'inventaire dans un fichier JSON
def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)

# Ouvrir la trésorerie depuis un fichier texte
def ouvrir_tresorerie(path="data/tresorerie.txt"):
    with open(path, 'r', encoding='utf-8') as fichier:
        tresorerie = json.load(fichier)
    return tresorerie

# Écrire la trésorerie dans un fichier texte
def ecrire_tresorerie(tresorerie, path="data/tresorerie.txt"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)

# Ouvrir les prix depuis un fichier JSON
def ouvrir_prix(path="data/prix.json"):
    with open(path, 'r', encoding='utf-8') as fichier:
        prix = json.load(fichier)
    return prix

# Afficher les prix des fruits
def afficher_prix(prix):
    print("\nPrix des fruits :")
    for fruit, prix_unitaire in prix.items():
        print(f"- {fruit.capitalize()} : {prix_unitaire} $ par unité")

# Afficher la trésorerie
def afficher_tresorerie(tresorerie):
    print(f"\n💰 Trésorerie actuelle : {tresorerie:.2f} $")

# Afficher l'inventaire
def afficher_inventaire(inventaire):
    print("Inventaire actuel de la plantation :")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")

# Récolter des fruits et mettre à jour l'inventaire
def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"\n✅ Récolté {quantite} {fruit} supplémentaires !")

# Vendre des fruits et mettre à jour l'inventaire et la trésorerie
def vendre(inventaire, fruit, quantite, tresorerie, prix):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        revenu = calculer_revenu(prix, fruit, quantite)
        tresorerie += revenu  # Augmenter la trésorerie en fonction du revenu de la vente
        print(f"\n💰 Vendu {quantite} {fruit} pour {revenu} $ !")
        return inventaire, tresorerie
    else:
        print(f"\n❌ Pas assez de {fruit} pour vendre {quantite} unités.")
        return inventaire, tresorerie

# Calculer le revenu d'une vente
def calculer_revenu(prix, fruit, quantite):
    return prix.get(fruit, 0) * quantite

# Fonction principale
if __name__ == "__main__":
    inventaire = ouvrir_inventaire()  # Charger l'inventaire
    tresorerie = ouvrir_tresorerie()  # Charger la trésorerie
    prix = ouvrir_prix()  # Charger les prix des fruits

    afficher_tresorerie(tresorerie)   # Afficher la trésorerie
    afficher_inventaire(inventaire)   # Afficher l'inventaire
    afficher_prix(prix)               # Afficher les prix des fruits
    
    # Récolter et vendre des fruits
    recolter(inventaire, "bananes", 10)
    inventaire, tresorerie = vendre(inventaire, "bananes", 5, tresorerie, prix)
    
    # Sauvegarder les modifications dans les fichiers
    ecrire_inventaire(inventaire)  # Sauvegarder l'inventaire mis à jour
    ecrire_tresorerie(tresorerie)  # Sauvegarder la trésorerie mise à jour
