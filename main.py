import ufunction as loyfun
import os


if __name__ == '__main__':

    # Richiedi i dati per il login
    if not os.path.exists("option.txt"):
        print("Hello, welcome in LoyaltyCardAPI.\nPlease provide your data.\nEmail: ")
        email = input()
        print("Password: ")
        password = input()
        print("Api_token: ")
        api_token = input()

        # Inizializza la classe
        cardClass = loyfun.login(email, password, api_token)
    else:
        lista = []
        with open("option.txt", "r") as file:
            for riga in file:
                lista.append(riga[:-1])
        cardClass = loyfun.login(lista[0], lista[1], lista[2])

    condizioneUscita = True
    while condizioneUscita:
        loyfun.stampaOpzioni()
        opzione = int(input())

        loyfun.manageFunction(opzione, cardClass)

        if opzione == 8:
            condizioneUscita = False






