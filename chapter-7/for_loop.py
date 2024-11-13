# For loop

# for i in range(1, 4):
#     print(i);

# *for loop in list

l = [1, 5, 7, 3, "Bokor"];

# for i in l:
#     print(i);

# *for loop in tuple

t = (1, 5, 7, 3, "Bokor");

# for i in t:
#     print(i);


## * Range in for loop:

# range(start, stop, step_size)

# for i in range(0, 20, 5):
#     print(i);


# *FOR LOOP WITH ELSE
# l= [1,7,8]
# for item in l:
#     print(item)
# else:
#     print("done") # this is printed when the loop exhausts!


# *Break
for i in range (0,80):
    print(i) # this will print 0,1,2 and 3
    if i==3:
        break # stop / exit the loop
# *continue

for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue # skip
    print(i);


# *pass

l = [1,7,8]
for item in l:
    pass # without pass, the program will throw an error