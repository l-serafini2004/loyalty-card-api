import lcard.Loyalty as ll

def login(email, password, token):
    data = {
        "email": email,
        "password": password,
        "api_token": token
    }

    instanceOfClass = ll.LoyCard(data)

    # Ritorna l'istanza
    return instanceOfClass

def printCompany(elem):
    print(f"\nInfo company:")
    elements = elem.infoCompany()
    for key in elements['company']:
        print(f"{key}: {elements['company'][key]}")

def printCards(elem):
    print("All your cards:")
    cards = elem.cards()['data']

    for card in cards:
        print("\nCard:")
        for key in card:
            print(f"{key}: {card[key]}")

def printCard(elem, cardName):
    card = elem.card(cardName)['data']

    if card == "[]":
        for carta in card:
            for key in carta:
                print(f"{key}: {carta[key]}")
    else:
        print("No cards match with this name")

def printAssociations(elem):
    print("All the card associations: ")
    associations = elem.associations()['data']
    for association in associations:
        print("-----")
        for key in association:
            print(f"{key}: {association[key]}")
        print("-----")

def upPoint(elem, email, point):
    try:
        result = elem.updatePoint(email, point)
        print(result)
    except:
        print("An error has occurred")



def deleteCard(elem, cardName):
    sure = input("Are you sure? (Y/n):  ")
    if sure == "Y":
        try:
            result = elem.deleteCard(cardName)
            print(result)
        except:
            print("An error has occurred")

def createAssoc(elem):
    email = input("Enter a mail: ")
    name = input("Enter a name: ")
    surname = input("Enter a surname: ")
    customer_number = input("Enter the customer number: ")

    # Prova a creare il profilo, se c'è già fallisce
    try:
        elem.createCustomer(email, name, surname, customer_number)
    except:
        print("The user already exists, you just have to associate the card with it")

    id = int(input("Enter the card_id: "))

    try:
        elem.createAssoc(email, id)
    except:
        print("The user is already associated with another card")

def manageFunction(n, elem):

    match n:
        case 1:
            printCompany(elem)
        case 2:
            printCards(elem)
        case 3:
            print("Name of the card: ")
            cardName = input()
            printCard(elem, cardName)
        case 4:
            printAssociations(elem)
        case 5:
            email = input("Enter the mail:")
            point = int(input("Enter the point (use - before the number if you want to remove the points): "))
            upPoint(elem, email, point)
        case 6:
            cardName = input("Enter the cardName of the card you want remove: ")
            deleteCard(elem, cardName)
        case 7:
            # Create user
            createAssoc(elem)
        case _:
            return


def stampaOpzioni():
    print("\nYou're now logged in, please select an option in the following menu:")
    print("1. Get the company info")
    print("2. Get all the cards of your shop")
    print("3. Get the card with that cardName")
    print("4. Get all the associations (the people who own your card)")
    print("5. Update the point of a specific card")
    print("6. Delete card")
    print("7. Create user")
    print("8. Exit")