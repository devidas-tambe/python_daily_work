def swap(a, b):
    return b, a

print(swap(5, 10))

def subtraction(a,b):
    return b-a
print(subtraction(10,5))

total=0
num=12345
for i in str(num):
    total=total + int(i)
print(total)


# Check prime number
n = 7
flag = True

for i in range(2, n):
    if n % i == 0:
        flag = False

print(flag)


# 🔹 18. Reverse string manually
s = "hello"
rev = ""

for ch in s:
    rev = ch + rev

print(rev)




for i in range(1,9,1):
    for j in 
    print("*")