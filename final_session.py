def quickSortByAge(liste, debut, fin):
    # Cas de base
    if fin - debut < 2:
        return

    # selection du pivot (ici, le dernier element de la liste )
    pivot = liste[fin - 1][1]
    curseur = debut

    # partition de la liste de tuples
    for i in range(debut, fin - 1):
        if liste[i][1] <= pivot:
            # echanger les elements d'indices i et curseur
            liste[i], liste[curseur] = liste[curseur], liste[i]
            curseur += 1

    # positionnement definitif du pivot
    liste[fin - 1], liste[curseur] = liste[curseur], liste[fin - 1]

    # appels recursifs
    quickSortByAge(liste, debut, curseur)
    quickSortByAge(liste, curseur + 1, fin)

# exemple d'utilisation avec notre liste de tuples donne dans le fichier exel
liste = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27), ("Merlin", 19), ("Rachy", 25)]

# appel du tri rapide sur la liste de tuples en fonction de lage (deuxieme element)
quickSortByAge(liste, 0, len(liste))

# affichage du tableau trie
print("Liste triée par âge:", liste)
#exercice 2 sur la recherche dicotomie -----------------------------------------------

def recherche_dichotomique(liste_tuples, nom_A_recherche):
    # triez la liste par nom pour utiliser la recherche dichotomique
    liste_triee = sorted(liste_tuples, key=lambda x: x[0])

    # recherche dichotomique
    gauche, droite = 0, len(liste_triee) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste_triee[milieu][0] == nom_A_recherche:
            # Renvoie lage correspondant au nom trouver
            return liste_triee[milieu][1]  
        elif liste_triee[milieu][0] < nom_A_recherche:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    # S'il  ne pas trouver le nom
    return None

# exemple d'utilisation avec notre liste de tuples
liste = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27), ("Merlin", 19), ("Rachy", 25)]

# fonction de recherche par nom
def searchByName(nom):
    age = recherche_dichotomique(liste, nom)
    if age is not None:
        print(f"L'âge de {nom} est {age}.")
    else:
        print(f"Le nom '{nom}' n'a pas été trouvé dans la liste.")

# exemples d'utilisation
searchByName("Ryan")
searchByName("Lilian")
#pour ulistre si sa fonction prend non un nom qui nexiste pas 
searchByName("Alice")
searchByName("Viny")


#exercices 3

def printNames(lisdeuples):
    for nom, _ in lisdeuples:
        print(nom)

# exemple d'utilisation avec votre liste de tuples
liste = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27), ("Merlin", 19), ("Rachy", 25)]

# appel de la fonction pour afficher les noms
print("Liste des noms est :")
printNames(liste)

def printRecNames(lisdetuples):
    # Si la liste est vide, on arrête la récursion
    if not lisdetuples:
        return
    # affichage du premier nom du premier tuple
    print(lisdetuples[0][0])
    # ici va faire la récursivite avec le reste de la liste
    printRecNames(lisdetuples[1:])

# exemple d'utilisation avec notre liste de tuples
liste = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27), ("Merlin", 19), ("Rachy", 25)]

# appel de la fonction pour afficher les noms
print("Liste des noms est :")
printRecNames(liste)

