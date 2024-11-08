# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

favorite_languages = {}

for i in range(4):
    name = input(f"Enter the name of friend {i + 1}: ");
    language = input(f"Enter {name} favorite language: ");
    favorite_languages[name] = language;

print(favorite_languages)