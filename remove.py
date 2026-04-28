import os
# f=open("remove.txt","x")

# os.remove("remove.txt")

if os.path.exists("remove.txt"):
    os.remove("remove.txt")
else:
    print("File Already Deleted")