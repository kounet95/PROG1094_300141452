def quickSortByAge(liste, debut, fin):
    # Cas de base
    if fin - debut < 2:
        return

    # Sélection du pivot (ici, le dernier élément de la liste )
    pivot = liste[fin - 1][1]
    curseur = debut

    # Partition de la liste de tuples
    for i in range(debut, fin - 1):
        if liste[i][1] <= pivot:
            # Échanger les éléments d'indices i et curseur
            liste[i], liste[curseur] = liste[curseur], liste[i]
            curseur += 1

    # Positionnement définitif du pivot
    liste[fin - 1], liste[curseur] = liste[curseur], liste[fin - 1]

    # Appels récursifs
    quickSortByAge(liste, debut, curseur)
    quickSortByAge(liste, curseur + 1, fin)

# Exemple d'utilisation avec notre liste de tuples donne dans le fichier exel
liste = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27), ("Merlin", 19), ("Rachy", 25)]

# Appel du tri rapide sur la liste de tuples en fonction de l'âge (deuxième élément)
quickSortByAge(liste, 0, len(liste))

# Affichage du tableau trié
print("Liste triée par âge:", liste)
