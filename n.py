import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a1)

a4=np.array([2,3,4,5,6,7,4,2,4])
a5=np.where(a4%2==0)
print(a5)

a6 = np.where(a4>2)
print(a6)

print(np.sort(a5))

n=np.where(a4==4)
print(n)

a=np.array([2,3,4,5,6,7,4,2,4])
a8=a.reshape(3,3)
print(a8)

a9=a.reshape(3,3,1)
print(a9)

a9=np.array([[1,2,3,4],[4,5,6,7]])
for i in a9:
    for j in i:
        print(j)

a22=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
# for i in a22:
#     for j in i:
#         for k in j:
#             print(k)    

for i in np.nditer(a22):
    print(i)