# Example of multiple if-else statements

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
    