def login1(username,password):
    user_name="detidas_tambe"
    u_pass="Devi@123"

    if (user_name==user_name):
        if(u_pass==password):
            print("login succesful")
        else:
            print("incorect detail")
login1("devidas_tambe","Devi@123")



def login2():
    Uid="devidas_tambe"
    upasss="Devi@123"
   
    while True:
        correct_id=input("enter the user id = ")
        correct_pass=input("enter th user pass =")

   
        if correct_id==Uid and correct_pass==upasss:
            print("login succesfully")
            break
        else:
            print("try again") 
login2()