a = int(input("Enter your age:"))
if (a>=18):
    print("You are eligible to vote")
elif(a<0):
    print("Invalid age")
    
elif(a==0):
    print("Invalid age you are entering zero")
else:
    print("You are not eligible to vote")