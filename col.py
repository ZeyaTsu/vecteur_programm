import math

def colineaire():
    xa = float(input("Vecteur 1, Xa = "))
    ya = float(input("Vecteur 1, Ya = "))
    xb = float(input("Vecteur 2, Xb = "))
    yb = float(input("Vecteur 2, Yb = "))

    result = (xa * yb) - (ya * xb)
    if result == 0:
        print("Le vecteur 1 et 2 sont colinéraires. Les droits Vecteur 1 et 2 sont parallèles.")
        print("car le DET est égal à", result)
    elif result != 0:
        print("Le vecteur 1 et 2 ne sont pas colinéraires. Les droits Vecteur 1 et 2 ne sont pas parallèles.")
        print("car le DET est égal à", result)


    s = True
    while s:
        confirm = str(input("Relancer ? Y/N > "))
        if confirm == "Y":
            colineaire()
        elif confirm == "N":
            choixmath()
            s = False
            

def vec():
    choice = str(input("Type de vecteur : AB | BA > "))
    if choice == "AB":
        vec2()
    elif choice == "BA":
        vec3()
    elif choice != "AB" or "BA":
        vec()

def vec2():
    xa = float(input("Point A | X = "))
    ya = float(input("Point A | Y = "))
    xb = float(input("Point B | X = "))
    yb = float(input("Point B | Y = "))

    vec_result = xb - xa
    vec_result2 = yb - ya
    print("Les coordonnées du vecteur AB sont AB(", vec_result,";", vec_result2,")")
    choixmath()

def vec3():
    xa = float(input("Point A | X = "))
    ya = float(input("Point A | Y = "))
    xb = float(input("Point B | X = "))
    yb = float(input("Point B | Y = "))

    vec_result1 = xa - xb
    vec_result3 = ya - yb
    print("Les coordonnées du vecteur AB sont AB(", vec_result1,";", vec_result3,")")
    choixmath()


def choixmath():
    print("CALCUL: Coordonnées Vecteurs (1) | Déterminer si 2 vecteurs sont colinéaires (2) | QUIT (0)")
    choixmath = int(input("> "))
    w = True
    while w:
        if choixmath == 1:
            vec()
            w = False
        elif choixmath == 2:
            colineaire()
            w = False
        elif choixmath == 0:
            w = False
    
choixmath()
 