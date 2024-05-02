# Import
import requests as req
import os

# GLi URL
PATH = "http://127.0.0.1:8000/api/" # PRINCIPAL PATH

LOGINURL = "authenticate"
COMPANYURL = "company/info"
CARDS = "card/all"
CARD = "card/show"
ASSOCIATIONS = "association/all"
ASSOCIATIONMODIFY = "association/update"
CREATECUSTOMER = "customer/store"
CREATEASSOCIATION = "association/store"
DELETECARD = "card/delete"

# Creo la classe
class LoyCard:

    # COSTRUTTORE
    def __init__(self, data):
        self.data = data

        # Verifichiamo se le credenziali passate sono corrette
        response = req.post(PATH + LOGINURL, self.data)

        # Se il login va a buon fine, settiamo il token --> altrimenti esci con errore
        if response.status_code == 200:
            json_data = response.json()
            self.token = "Bearer " + json_data['data']['token']

            # Creiamo un file e salviamone le informazioni
            if not os.path.exists("option.txt"):
                with open("option.txt", "w") as file:
                    file.write(data["email"])
                    file.write("\n")
                    file.write(data["password"])
                    file.write("\n")
                    file.write(data["api_token"])
                    file.write("\n")

        else:
            print("Error code: " + str(response.status_code))
            print("Error: " + response.json()['message'])
            exit(1)

        # Autorizzazione
        self.auth = {"Authorization":self.token}



    # DATI DELLA COMPANY
    def infoCompany(self):
        # Creo la richiesta
        company = req.get(PATH + COMPANYURL, headers=self.auth)

        if(company.status_code == 200):
            return company.json()
        else:
            return company.json()['message']

    def cards(self):

        # Se non ci sono tag --> prendo tutte le carte
        cards = req.get(PATH + CARDS, headers=self.auth)
        return cards.json()

    def card(self, tags):

        # Con parametri --> prendo solo certe cose
        cards = req.get(PATH + CARD, headers=self.auth, params={ "cardName": tags })
        return cards.json()

    def associations(self):

        # Prendi tutte le associations e i dati degli utenti
        associations = req.get(PATH + ASSOCIATIONS, headers=self.auth)
        return associations.json()

    def updatePoint(self, email, point):

        # Modifica il punteggio
        association = req.post(PATH + ASSOCIATIONMODIFY, headers=self.auth, params={ "email":email, "changePoint":point })
        return association.json()

    def createCustomer(self, email, name, surname, customer_number):

        #Parametri
        user_params = {
            "email":email,
            "name":name,
            "surname":surname,
            "customer_number":customer_number
        }

        user = req.post(PATH + CREATECUSTOMER, headers=self.auth, params=user_params)
        return user.json()

    def createAssoc(self, email, card_id):

        assoc_params = {
            "email":email,
            "card_id":card_id
        }

        assoc = req.post(PATH + CREATEASSOCIATION, headers=self.auth, params=assoc_params)
        return assoc.json()

    def deleteCard(self, cardName):

        try:
            card = self.card(cardName)['data'][0] # Trovo la carta
        except IndexError:
            return "A problem has occurred"

        id = card['id']
        delete = req.post(PATH + DELETECARD, headers=self.auth, params={"id":id})

        return delete.json()