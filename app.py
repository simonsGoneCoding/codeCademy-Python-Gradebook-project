# Python Gradebook
# You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Use the zip() function to combine subjects and grades.
# Save this zip object as a list into a variable called gradebook
gradebook = list(zip(subjects, grades))
print(gradebook)

# After your definitions of subjects and grades but before you create gradebook, use append to add "computer science" to subjects and 100 to grades.
subjects.append("computer science")
grades.append(100)




