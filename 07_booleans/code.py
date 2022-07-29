# -- Comparisons --

print(5 == 5)  # True
print(5 > 5)  # False
print(10 != 10)  # False

# Comparisons: ==, !=, >, <, >=, <=

# -- is --
# Python also has the `is` keyword. It's a confusing keyword for now, so I don't recommend using it.

friends = ["Dija", "Zaid"]
abroad = ["Dija", "Zaid"]

print(friends == abroad)  # True
print(friends is abroad)  # False
