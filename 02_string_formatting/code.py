name = "Zaid"
greeting = "Hello, Zaid"

print(greeting)

name = "Dija"

print(greeting)

greeting = f"Hello, {name}"
print(greeting)

# --

name = "Hafsa"
print(
    greeting
)  # This still prints "Hello, Dija" because `greeting` was calculated earlier.
print(
    f"Hello, {name}"
)  # This is correct, since it uses `name` at the current point in time.

# -- Using .format() --

# We can define template strings and then replace parts of it with another value, instead of doing it directly in the string.

greeting = "Hello, {}"
with_name = greeting.format("Dija")
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Dija", "Monday")
print(formatted)
