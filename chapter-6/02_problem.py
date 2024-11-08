# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.


# Input marks for three subjects
subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))

# Calculate total marks and percentage
total_marks = subject1 + subject2 + subject3;
percentage = (total_marks / 300) * 100;

# Check if the student has passed or failed
if (percentage >= 40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33):
    print("Congratulations! You have passed.")
else:
    print("Sorry, you have failed.")