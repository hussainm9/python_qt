class Card:
    def __init__(self,card_number):
        self.card_number =card_number
        self.annual_charges = 0
    def swipe(self,amount):
        print(f"card {self.card_number} used for RS {amount}")

class BankAccount:
    def __init__(self,account_id,name,mobile_no,email_id,balance,card):
        self.account_id = account_id
        self.name = name
        self.mobile_no = mobile_no
        self.email_id = email_id
        self.balance = balance
        self.card = card
        self.balance -= self.card.annual_charges


    def withdraw(self,amount):
        if amount > self.balance:
            return False
        else:
            self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def transfer(self,account,amount):
        self.withdraw(amount)
        account.deposit(amount)

# *** without card deposit,withdraw,transfer***
# ram_account = BankAccount('ram_01','ram',908908,'ram@gmail.com',995)
# print(ram_account)
# print(ram_account.account_id)
# print(ram_account.name)
# print(ram_account.mobile_no)
# print(ram_account.email_id)
# print(ram_account.balance)
# shyam_account = BankAccount('shyam_01','shyam',908900,'shyam@gmail.com',95)
# print(shyam_account)
# print(shyam_account.account_id)
# print(shyam_account.name)
# print(shyam_account.mobile_no)
# print(shyam_account.email_id)
# print(shyam_account.balance)
# print(ram_account.withdraw(500),'withdrawing 500 in ram account')
# print(ram_account.balance)
# print(shyam_account.deposit(500),'depositing 500 in shyam account')
# print(shyam_account.balance)
# print(ram_account.transfer(shyam_account,5))
# print(ram_account.balance) 
# print(shyam_account.balance)

class SilverCard(Card):
    pass
class PlatinumCard(Card):
   def __init__(self, card_number):
       super().__init__(card_number)
       self.annual_charges = 1000

card1 = SilverCard('7487-5487-3847-3453')
card2 = PlatinumCard('9854-4334-2312-4543')

print(card1,card1.card_number,card1.annual_charges,'card-1')

user1 = BankAccount('user_01','user1',87898,'user1@gmail.com',989,card1)
print(user1.card,user1.balance)
user2 = BankAccount('user_02','user2',80000,'user1@gmail.com',8000,card2)
print(user2.balance)