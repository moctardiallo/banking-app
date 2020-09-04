import sys
import staff
from db import Database
from domain.banque import Banque


banque = Banque()
db_clients = Database('./clients.txt')
db_transactions = Database('./transactions.txt')

def main():

    print(banque.enter())
    
    print(banque.request())

    choices = banque.options

    choice = int(input('Choose your action: '))

    if choice not in choices:
        print('This action is not implemented')
        main()

    if choice == 0:
        sys.exit()
        
    elif choice == 1:
        print("*********CREATING PROFILE*********")
        name, lastname, solde = staff.ask_name(), staff.ask_lastname(), staff.ask_solde()
        client = banque.create_profile(name, lastname, solde)
        db_clients.save(str(client))
        main()

    elif choice == 2:
        print("*********MAKING DEPOSIT*********")
        name = staff.ask_name()
        amount = staff.ask_amount('deposit')
        trans = banque.make_transaction('deposit', name, amount)
        if trans is None:
            print(f'Impossible transaction because client {name} does not exist')
            main()
        else:
            db_transactions.save(str(trans))
            main()

    elif choice == 3:
        print("*********MAKING DEBIT*********")
        name = staff.ask_name()
        amount = staff.ask_amount('debit')
        try:
            trans = banque.make_transaction('debit', name, amount)
        except ValueError as ve:
            print(ve.__traceback__)
            main()
        except IndexError:
            print(f"{name}'s account was not found.")
            main()
        db_transactions.save(str(trans))
        main()

    elif choice == 4:
        print("*********DISPLAYING CLIENTS*********")
        print(banque.clients)
        main()

    else:
        print('This action is not implemented')
        main()

if __name__ == '__main__':
    main()