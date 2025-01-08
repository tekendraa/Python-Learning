marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))
marks3 = int(input("Enter your marks: "))

# Check for total percentage
total_percentage = (marks1 + marks2 + marks3) / 300

if total_percentage >= 80:
    print("You have scored A grade.")
elif total_percentage >= 60 and total_percentage < 80:
    print("You have scored B grade.")
elif total_percentage >= 40 and total_percentage < 60:
    print("You have scored C grade.")
else :
    print("You have scored D grade. Try again next time.")
