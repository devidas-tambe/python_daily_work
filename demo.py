import os

f=open("demo.txt","r")
# print(f.read())

# print(f.read(10))

# print(f.readline())

for i in f:
    print(i)


with open("demo.txt","w") as f:
    content=f.write("hello")