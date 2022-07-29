numbers = [1, 3, 5]
squares = [x * 2 for x in numbers]

# -- Dealing with strings --

friends = ["Dija", "Sam", "Samantha", "Saurabh", "Fiya"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


# -- Can make a new list of friends whose name starts with S --

friends = ["Dija", "Sam", "Samantha", "Saurabh", "Fiya"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

# -- List comprehension creates a _new_ list --

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), " starts_s: ", id(starts_s))
