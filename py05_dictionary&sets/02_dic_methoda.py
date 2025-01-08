marks = {
    "Tekendra": 90,
    "Berlin": 85,
    "Sujan": 50,
}

print(marks.items()) 
print(marks.keys())
print(marks.values())
marks.update({"Sujan": 60})
print(marks)
dict.clear(marks)
print(marks)