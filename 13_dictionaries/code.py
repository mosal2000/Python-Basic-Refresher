friend_ages = {"Dija": 24, "Adam": 30, "Hafsa": 27}

friend_ages["Zaid"] = 20

print(friend_ages)  # {'Dija': 24, 'Adam': 30, 'Hafsa': 27, 'Zaid': 20}
print(friend_ages["Zaid"])

# -- List of dictionaries --

friends = [
    {"name": "Dija Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Hafsa Pun", "age": 27},
]

print(friends)

# -- Iteration --

student_attendance = {"Dija": 96, "Zaid": 80, "Hafsa": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

# Better

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# -- Using the `in` keyword --

if "Zaid" in student_attendance:
    print(f"Zaid: {student_attendance[student]}")
else:
    print("Zaid isn't a student in this class!")

# -- Calculate an average with `.values()` --

attendace_values = student_attendance.values()
print(sum(attendace_values) / len(attendace_values))
