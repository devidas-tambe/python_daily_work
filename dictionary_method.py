d={"name":"Devidas",
   "city":"Nashik",
   "age":21,
   "cource":"Python"
   
   }

print(d)

# ''' get method'''
print(d.get("city")) 

c=d.copy()
print(c)

d.pop("cource")
print(d)

d={"name":"Devidas",
   "city":"Nashik",
   "age":21,
   "cource":"Python"
   
   }

print(sorted(d.keys()))

print(sorted(d.items()))

c=d.items()
print(c)

k=d.keys()
print(k)


f=d.fromkeys(k,"hi")
print(f)

d.update({"branch":"PMC"})
print(d)

d["branch"]="pune"
print(d)