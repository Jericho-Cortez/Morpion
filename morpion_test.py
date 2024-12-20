"""
#Matrice du tableau qui pourra etre modifié en cour de jeu
def tableau(case):
    print(case[1],"|",case[2],"|",case[3])
    print("--|---|---")
    print(case[4],"|",case[5],"|",case[6])
    print("--|---|---")
    print(case[7],"|",case[8],"|",case[9])

#Les differentes combinaisons pour determiner un gagnant
def Condition_Pour_Gagner(case,joueur):
    victoire=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for combinaison in victoire:
        if case[combinaison[0]] == case[combinaison[1]] == case[combinaison[2]] == joueur:
            return True 
    return False # Si il y a une combinaison la partie en cour sera en FALSE (fini)

def Morpion():
    #Permet de donner une valeur pour chaque case de 1 à 9
    case={i:str(i) for i in range(1,10)}
    joueur_actuel="X"
    partie_en_cour=True
    nombre_tour=0
    print("Viens Jouer Batard")
    tableau(case)
    while partie_en_cour:
        try:
            tour=int(input(f"Joueur {joueur_actuel} choisi un chiffre entre 1 a 9 pour te placer: "))
            #verifie si la case n'est pas déja prise sinon renvoie la question
            if case[tour] in ["X","O"]:
                print("Tié trop lent le sang, c'est deja pris")
                continue
            #verifie que le chiffre demander est entre 1 et 9
            if 1 > tour >10:
                print("Apprend à compter")
                continue
            #Si la réponse n'est pas un chiffre renvoie une erreur et repose la question
        except ValueError:
            print("Un chiffre entre 1 a 9, c'est pas compliquer nan ?")
            continue
        #Le joueur remplace la valeur de la case par X ou O
        case[tour]= joueur_actuel
        tableau(case)

        if Condition_Pour_Gagner(case,joueur_actuel):
            print(f"Joueur {joueur_actuel} à gagner")
            partie_en_cour=False
        if nombre_tour==9:
            print("Egalité")
            partie_en_cour=False
        else:
            #alterne entre X et O si n'y a pas de gagnant
            joueur_actuel="O" if joueur_actuel=="X" else "X"
    print("C'est FINI DEGAGE")

Morpion()
        

        #Hello Jericho
        # Ca marche?

        # I'm checking again
"""



#Matrice du tableau qui pourra etre modifié en cour de jeu
def tableau(case):
    print("")
    print(case[1],"|",case[2],"|",case[3])
    print("--|---|---")
    print(case[4],"|",case[5],"|",case[6])
    print("--|---|---")
    print(case[7],"|",case[8],"|",case[9])
    print("")

#Les differentes combinaisons pour determiner un gagnant
def Condition_Pour_Gagner(case,joueur):
    victoire=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for combinaison in victoire:
        if case[combinaison[0]] == case[combinaison[1]] == case[combinaison[2]] == joueur:
            return True 
    return False # Si il y a une combinaison la partie en cour sera en FALSE (fini)

def Morpion():
    #Permet de donner une valeur pour chaque case de 1 à 9
    case={i:str(i) for i in range(1,10)}
    joueur_actuel="X"
    partie_en_cour=True
    nombre_tour=0
    print("\nViens Jouer Batard\n")
    tableau(case)
    while partie_en_cour:
        try:
            tour=int(input(f"\nJoueur {joueur_actuel} choisi un chiffre entre 1 a 9 pour te placer: \n"))
            #verifie si la case n'est pas déja prise sinon renvoie la question
            if case[tour] in ["X","O"]:
                print("\nTié trop lent le sang, c'est deja pris\n")
                continue
            #verifie que le chiffre demander est entre 1 et 9
            if 1 > tour >10:
                print("\nApprend à compter\n")
                continue
            #Si la réponse n'est pas un chiffre renvoie une erreur et repose la question
        except ValueError:
            print("\nUn chiffre entre 1 a 9, c'est pas compliquer nan ?\n")
            continue
        #Le joueur remplace la valeur de la case par X ou O
        case[tour]= joueur_actuel
        print("")
        tableau(case)
        print("")

        if Condition_Pour_Gagner(case,joueur_actuel):
            print(f"Joueur {joueur_actuel} à gagner\n")
            partie_en_cour=False
        if nombre_tour==9:
            print("Egalité")
            partie_en_cour=False
        else:
            #alterne entre X et O si n'y a pas de gagnant
            joueur_actuel="O" if joueur_actuel=="X" else "X"
    print("C'est FINI DEGAGE")

#Morpion()


def Morpion_IA():
    # Permet de donner une valeur pour chaque case de 1 à 9
    case = {i: str(i) for i in range(1, 10)}
    joueur_actuel = "X"
    partie_en_cour = True
    nombre_tour = 0
    print("\nViens Jouer Batard\n")
    tableau(case)
    
    while partie_en_cour:
        if joueur_actuel == "X":
            # Human's turn
            try:
                tour = int(input(f"Joueur {joueur_actuel}, choisis un chiffre entre 1 et 9 pour te placer: "))
                # Vérifie si la case n'est pas déjà prise sinon renvoie la question
                if case[tour] in ["X", "O"]:
                    print("Tié trop lent le sang, c'est déjà pris")
                    continue
                # Vérifie que le chiffre demandé est entre 1 et 9
                if 1 > tour > 9:
                    print("Apprends à compter")
                    continue
            except ValueError:
                print("Un chiffre entre 1 et 9, c'est pas compliqué nan ?")
                continue
        else:
            # Computer's turn
            # Choisit la première case libre disponible
            for i in range(1, 10):
                if case[i] not in ["X", "O"]:
                    tour = i
                    break
        
        # Le joueur remplace la valeur de la case par X ou O
        case[tour] = joueur_actuel
        tableau(case)

        # Vérifie s'il y a un gagnant
        if Condition_Pour_Gagner(case, joueur_actuel):
            print(f"Joueur {joueur_actuel} a gagné\n")
            partie_en_cour = False
        elif nombre_tour == 8:  # Si 9 tours ont été joués (0-8), c'est une égalité
            print("Égalité")
            partie_en_cour = False
        else:
            # Alterne entre X et O si n'y a pas de gagnant
            joueur_actuel = "O" if joueur_actuel == "X" else "X"
            nombre_tour += 1
    
    print("C'est FINI, DÉGAGE")




def vs_human():
    if input("\nDo you want to play against a friend (Yes or No): ") == "Yes":
        Morpion()  
    else:
        Morpion_IA()  

vs_human()

# Hello#
