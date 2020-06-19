import time

Trys = 0
def printHangman(Trys):
    if Trys == 0:
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    if Trys == 1:
        print("_________")
        print("|	 |")
        print("|    o")
        print("|")
        print("|")
        print("|")
        print("|________")
    if Trys == 2:
        print("_________")
        print("|	 |")
        print("|    o")
        print("|    |")
        print("|    |")
        print("|")
        print("|________")
    if Trys == 3:
        print("_________")
        print("|	 |")
        print("|    o")
        print("|   \|")
        print("|    |")
        print("|")
        print("|________")
    if Trys == 4:
        print("_________")
        print("|	 |")
        print("|    o")
        print("|   \|/")
        print("|    |")
        print("|")
        print("|________")
    if Trys == 5:
        print("_________")
        print("|	 |")
        print("|    o")
        print("|   \|/")
        print("|    |")
        print("|   /")
        print("|________")
    if Trys == 6:
        print("_________")
        print("|	 |")
        print("|    o")
        print("|   \|/")
        print("|    |")
        print("|   / \ ")
        print("|________")
        print("\n")
        print("Du hast VERLOREN")
        print("\n")
        again = input("Willst du es nocheinmal Spielen? (Ja oder Nein):")
        if again == "Ja" or "ja":
            selectRoles()
            hangMan()
        return

def selectRoles():
    print("Willkommen bei Hangman!")
    print("[Coded by Paul]\n\n")
    Ratende = input("Wer muss Raten: ")
    Wortaussuchende = input("Wer muss das Wort aussuchen: ")
    print("------------------------")
    print("Perfekt, also " + Ratende + " errät dass Wort und " + Wortaussuchende + " sucht dass Wort aus!")
    print("------------------------\n\n")

    NameProve = input("Ist das Richtig? (Ja oder Nein): ")
    if NameProve == "Ja" or "ja":
        time.sleep(1)
        print("\n\n------------------------")
        print("Perfekt!")
        print("------------------------\n\n")
        time.sleep(1)
        print("///////////////////////////")
        print(Ratende + " muss jetzt wegschauen")
        print("///////////////////////////")
        time.sleep(1)
        print("------------3--------------")
        time.sleep(1)
        print("------------2--------------")
        time.sleep(1)
        print("------------1--------------")
        time.sleep(1)

    elif NameProve == "Nein" or "nein":
        print("\n\n------------------------")
        print("Oh, Kein Problem!")
        print("------------------------\n\n")
        time.sleep(1)
        selectRoles()

    else:
        print("///////////////////////////")
        print("Undefinierte Eingabe!")
        print("///////////////////////////\n\n")
        time.sleep(1)
        selectRoles()


def selectWord():
    myword = input("Ok, suche jetzt ein Wort aus! (Es darf nur bis zu 4 Buchstaben Haben!): ")
    if len(myword) <= 4:
        print("\n\n------------------------")
        print("Perfekt, dein Wort ist Gültig und wurde ausgewählt!")
        print("------------------------\n\n\n")
        time.sleep(2)
        myword = myword.lower()
        return myword
    else:
        print("///////////////////////////")
        print("Dein Wort ist ungültig! Es darf nur Max 4 Buchstaben haben!")
        print("///////////////////////////")
        time.sleep(1)
        selectWord()



def hangMan():
    Trys = 0
    word = selectWord()
    word_list = list(word)
    blanks = "_"*len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []


    printHangman(Trys)
    print("" + ' '.join(blanks_list))


    while Trys < 6:
        guess = input("Rate einen Buchstaben: ")
        guess = guess.lower()

        if len(guess) > 1:
            print("///////////////////////////")
            print("Du darfst nur einen Buchstaben eingeben!")
            print("///////////////////////////")
        elif guess == "":
            print("///////////////////////////")
            print("Gibt doch bitte etwas ein :(")
            print("///////////////////////////")
        elif guess in guess_list:
            print("///////////////////////////")
            print("Du Hast diesen Buchstaben schon gerraten! Hier sind alle Buchstaben die du Schon gerraten hast: ")
            print("///////////////////////////")
            time.sleep(2)
            print(' '.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i+1
            if new_blanks_list == blanks_list:
                print("\n\nDieser Buchstabe ist nicht im Wort enthalten!")
                Trys = Trys + 1
                printHangman(Trys)


            elif word_list != blanks_list:
                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))

                if word_list == blanks_list:
                    print("\n\nDu Hast GEWONNEN!\n\n")
                    quit()
                else:
                    print("Richtig! Rate nochmal!")





selectRoles()
hangMan()