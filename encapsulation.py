class account:
    def __init__(self,bal):
        self.__bal=bal
    
    def get_bal(self):
        return self.__bal
    
    def set_bal(self,amt):
        self.__bal=amt
        print("Balance updated successfully!")

    def deposit(self,amt):
        self.__bal+=amt
        print("Amount deposited successfully!")

    def withdraw(self,amt):
        if self.__bal>=amt:
            self.__bal-=amt
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def __private_method(self):
        return "hello im a private method"



obj = account(0)
print(obj.get_bal())

obj.set_bal(500)
print(obj.get_bal())

obj.deposit(200)
print(obj.get_bal())

obj.withdraw(300)
print(obj.get_bal())

obj.withdraw(500)
print(obj.get_bal())
