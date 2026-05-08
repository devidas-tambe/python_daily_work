class account:
    def __init__(self, acc_no, password):
        self.acc_no=acc_no
        self.__password=password
    
    def get_password(self):
        print(self.__password) 

acc1=account("12345", "pass123")

print(acc1.acc_no)
# print(acc1.get_password())
