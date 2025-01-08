a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if(a1>a2 and a2>a3 and a3>a4):
    print("Numbers are in decreasing order")
elif(a1<a2 and a2<a3 and a3<a4):
    print("Numbers are in increasing order")
else:
    print("Numbers are not in increasing or decreasing order")  