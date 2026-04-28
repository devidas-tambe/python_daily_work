def count_ovel(userinput):
    ovels="aeouiAEOUI"

    countovel=0
    countconsenent=0

    for i in userinput:
        if(i.isalpha()):
            if(i in ovels):
                countovel=countovel+1
            else:
                countconsenent=countconsenent+1
    return countovel,countconsenent

ovel,conconent=count_ovel("Devidas Tambe")
print(ovel,conconent)


#upper case
def upper_case(user_input):
     return user_input.upper()
   
print(upper_case("devidas"))




def full_name(fname,lname):
    return fname,lname

firstname,lastname=full_name("Devidas","Tambe")
print(firstname,lastname)