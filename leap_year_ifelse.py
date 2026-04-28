y = int(input("Enter a year: "))

if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
    print("Year is a Leapyear")
else:
    print("Year is Not a Leapyear")
