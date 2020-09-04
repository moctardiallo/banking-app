class Database:

    def __init__(self, db_file):
        self.db_file = db_file
        self.DB = open(self.db_file, mode='w+')
        self.DB.write(f"--------------{db_file.upper()} DATABASE--------------\n\n")
        self.DB.close()
            
    # Equivalent to the 'saveCreatedClient', 'saveDebitTransaction', 'saveCreditTransaction' 
    # functions
    def save(self, save_format):
        with open(self.db_file, 'a+') as db:
            db.write(save_format)
