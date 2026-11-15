

def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")

def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")

def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche enregistrée.")
    else:
        print("\nListe des tâches :")
        for i, titre in enumerate(taches, start=1):
            print(f"{i}. {titre}")

def rechercher_tache():
    if len(taches) == 0:
        print("Aucune tâche à rechercher.")
        return
    mot_cle = input("Mot-clé à rechercher : ").strip().lower()
    resultats = []
    for i, titre in enumerate(taches, start=1):
        if mot_cle in titre.lower():
            resultats.append((i, titre))
    
    if len(resultats) == 0:
        print("Aucune tâche ne contient ce mot-clé.")
    else:
        print("\nRésultats de la recherche :")
        for num, titre in resultats:
            print(f"{num}. {titre}")

while True:
    afficher_menu()
    choix = input("Votre choix : ").strip()
    
    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        rechercher_tache()
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez choisir 0, 1, 2 ou 3.")