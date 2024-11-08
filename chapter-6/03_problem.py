# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams

# Input the comment from the user
comment = input("Enter the comment: ").lower()

# List of spam keywords to check
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

is_spam = any(keyword in comment for keyword in spam_keywords);

if is_spam:
    print("This is spam message");
else:
    print("This is not a spam message.");