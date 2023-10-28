
# YOUR CODE HERE - write code to create a text file out.txt in write mode 'w'

f = open("out.txt", "w")

# YOUR CODE HERE - populate the list with strings(text) of your choice. Add atleast 3

my_lines = ["Zain the King", "Sara the Knight", "Gryffin the Pawn"]

# Adding a \n after each line in list of strings
updated_my_lines = []

for line in my_lines:
    updated_my_lines.append(f"{line}\n")

# YOUR CODE HERE - write the lines in updated_my_lines to the file out.txt using f.writelines()
f.writelines(updated_my_lines)

# YOUR CODE HERE - write code to close the file using f.close()
f.close()


