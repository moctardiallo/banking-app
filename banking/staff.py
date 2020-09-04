def ask_name():
    return input("Enter your name: ")

def ask_lastname():
    return input("Enter your lastname: ")

def ask_solde():
    return int(input("Enter your solde: "))

def ask_amount(transaction='deposit'):
    return int(input(f"Enter your {transaction} amount: "))

def prepare_transaction(transaction):
    pass