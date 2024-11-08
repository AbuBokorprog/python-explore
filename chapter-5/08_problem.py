# If languages of two friends are same; what will happen to the program in problem
# 6?

favorite_languages = {}

for i in range(4):
    name = input(f"Enter the name of friend {i + 1}: ");
    language = input(f"Enter {name} favorite language: ");
    favorite_languages[name] = language;

print(favorite_languages)

# Output is {'AbuBokor': 'Bengali', 'saidul': 'english', 'babu': 'english', 'Bokor': 'hindi'}