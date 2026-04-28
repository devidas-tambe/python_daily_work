sub=["wed","sql","java","python"]

sub.append(".net")
print(sub)

mark=[23,45,77,22]
sub.append(mark)
print(sub)

sub.pop(3)
print(sub)

c=sub.copy()
print(c)


print(sub.count("wed"))

num=[1,2,3,4,5,6]
num.pop()
print(num)

num=[1,2,3,4,5,6]
num.pop(3)
print(num)

num=[1,2,3,4,5,6]
p=num.pop(3)
print(p)

num=[1,2,3,4,5,6]
num.reverse()
print(num)

name=["ram","sham","abhi","ravi"]
name.sort()
print(name)

name.sort(reverse=True)
print(name)