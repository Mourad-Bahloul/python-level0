def main():
    print("here the main")
    note1 = int(input("Entrer la première note: "))
    note2 = int(input("Entrer la deuxième note: "))
    note3 = int(input("Entrer la troisième note: "))
    resultat = (note1 + note2 + note3) / 3
    print("Le résultat est: " + str(resultat))


if __name__ == '__main__':
    main()
