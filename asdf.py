# print("choose a branch:\nSBI Rajpur Road - SBIN0001001\nSBI Clock Tower - SBIN0001002\nSBI Ballupur - SBIN0001003")
# class bank:
#     def __init__(self, name, ifsc_code):
#         self.name = name
#         self.ifsc_code = ifsc_code

# class card:
#     def __init__(self,phone_number):
#         self.phone_number = phone_number

# class customer:
#     def __init__(self,name,card_number, phone_number, balance,branch):
#         self.name = name
#         self.card_number = card_number
#         self.phone_number = phone_number
#         self.balance = balance
#         self.branch = branch 
    
#     def credit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"the amount creditted is {amount}. your current balance is {self.balance}")
#         else:
#             print("invalid response from user")
        
#     def debit(self,amount):
#         if amount > 0:
#             self.balance -= amount
#             print(f"the amount debitted is {amount}. your current balance is {self.balance}")
#         elif amount < 0:
#             self.balance += amount 
#             print(f"the amount debitted is {amount}. your current balance is {self.balance}")
#         else:
#             print("invalid response from user")

#     def show_balance(self):
#         print(f"your current balance is {self.balance}")


# branch1 = bank("SBI Rajpur Road", "SBIN0001001")
# branch2 = bank("SBI Clock Tower", "SBIN0001002")
# branch3 = bank("SBI Ballupur", "SBIN0001003")

# card1 = card(1234567890)
# card2 = card(9876543210)
# card3 = card(9876512345)

# aayush = customer("aayush",1234-5678-9012-3456, 1234567890, 16000, "SBI Ballupur")
# aayush.credit(11000)
# aayush.debit(1000)
# aayush.show_balance()




class Bank:
    def __init__(self, name, ifsc_code):
        self.name = name
        self.ifsc_code = ifsc_code

class Card:
    def __init__(self, phone_number):
        self.phone_number = phone_number

class Customer:
    def __init__(self, name, card, balance, branch):
        self.name = name
        self.card = card
        self.balance = balance
        self.branch = branch
    
    def credit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Credited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid amount for credit.")

    def debit(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Debited ₹{amount}. New balance: ₹{self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount for debit.")

    def show_balance(self):
        print(f"Current balance: ₹{self.balance}")


branches = {
    1: Bank("SBI Rajpur Road", "SBIN0001001"),
    2: Bank("SBI Clock Tower", "SBIN0001002"),
    3: Bank("SBI Ballupur", "SBIN0001003")
}

print("Choose a branch:")
for key, branch in branches.items():
    print(f"{key}) {branch.name} - {branch.ifsc_code}")

branch_choice = int(input("Enter branch number (1-3): "))
selected_branch = branches.get(branch_choice)

if not selected_branch:
    print("Invalid branch selected.")
    exit()

name = input("Enter your name: ")
phone_number = int(input("Enter your phone number: "))
card_number = input("Enter your card number (e.g. 1234-5678-9012-3456): ")

linked_card = Card(phone_number)
user = Customer(name, linked_card, balance=0, branch=selected_branch)

while True:
    print("\nChoose an operation:")
    print("1. Credit")
    print("2. Debit")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = float(input("Enter amount to credit: "))
        user.credit(amt)
    elif choice == "2":
        amt = float(input("Enter amount to debit: "))
        user.debit(amt)
    elif choice == "3":
        user.show_balance()
    elif choice == "4":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Try again.")
