# -- Difference between two sets --

friends = {"Zaid", "Dija", "Hafsa"}
abroad = {"Zaid", "Hafsa"}

# local_friends = ...
# If there are 3 friends, and 2 are abroad, that means that 1 friend is local.
# We can easily calculate which names are in `friends` but not in `abroad` by using `.difference`

local = friends.difference(abroad)
print(local)

print(abroad.difference(friends))  # This returns an empty set

# -- Union of two sets --

local = {"Dija"}
abroad = {"Zaid", "Hafsa"}

# friends = ...
# If we have 1 local friend and 2 abroad friends, we could calculate the total friends by using `.union`

friends = local.union(abroad)
print(friends)

# -- Intersection of two sets --

art = {"Zaid", "Fiya", "Dija", "Charlie"}
science = {"Zaid", "Fiya", "Adam", "Hafsa"}

# Given these two sets of students, we can calculate those who do both art and science by using `.intersection`

both = art.intersection(science)
print(both)
