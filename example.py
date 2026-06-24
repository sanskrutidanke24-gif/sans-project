class insta:
    def __init__(self,name,username,pwd):
        self.name=name
        self.username=username
        self.pwd=pwd

    def login(self,username,pwd):
        if self.username==username and self.pwd==pwd:
            print("Login successfull!")
            set.__otp=random.radiant(1000,999)
        else:
            print("Invalid creditials")
            

obj=insta("ram","ram@123",12345)
obj.login("ram123",1234)
