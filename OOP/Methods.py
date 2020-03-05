# Encapsulation: Objects contain the data and methods that operate on that data, but do not expose
# those functions to outside code.
# Pyhon allows to encapsulate data with the Object Oriented Programming Paradigm,
# or the Modular approach.

class Account:
    """ Simple Bank Account """

    def __init__(self, name, balance): #__init__: used to initialize a class almost EVERY time; method
        self.name = name               # The init method takes two parameters in addition to "self", which are then used to set the values of the data attributes for name and balance
        self.balance = balance         # Whenever you want to refer to data attributes, you have to use self.<attribute>
        print("Account created for " + self.name)
        
    def deposit(self, amount):         #
        if amount > 0:
            self.balance += amount
        
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            
    def show_balance(self):
        print("Balance is {}".format(self.balance))

if __name__ == '__main__':
    blake = Account("Blake", 0) # initializes a variable or in this case, an object of data type (or class) Account called Blake, with a starting value of $0
    blake.show_balance()        # Method that shoes the balance of the Blake object, or "account"
    
    blake.deposit(675)          # Method that deposits $675 in the Blake account: assigns 675 to the amount attribute, which then updates the self.balance attribute
    blake.show_balance()        # Shows the balance of the account: calls the show_balance method that prints out the value that was assigned to the self.balance attribute in the method above
    blake.withdraw(233)         # Withdraws $233 dollars: withdraw method assigns the value of 233 to the amount attribue in the withdraw method, and then subtracts that amount from the balance attribute
    blake.show_balance()        # Calls the show_blalance method that prints out the value that was assigned to the self.balance attribute in the method above.