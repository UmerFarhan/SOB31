# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) # Changed input to int

exam_three = int(input("Input exam grade three: ")) # Changed variable name to exam_three and changed input type to int

grades = [exam_one, exam_two, exam_three] # Added commas between the variables in list
sum = 0
for grade in grades: # Fixed loop by changing grade to grades
  sum = sum + grade

avg = sum / len(grades) # Fixed spelling mistake

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: # Added colon to fix statement
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" # Fixed mismatching closing quotes
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else: # Changed elif to else
    letter_grade = "F"

print("Exams: " + str(grades[0]) + ", " + str(grades[1]) + ", " + str(grades[2])) # Added the grades inputted to the print statement to match output cases

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade == "F": # Changed letter-grade to letter_grade and changed comparator to == instead of is
    print("Student is failing.") # Added parenthesis
else:
    print("Student is passing.") # Added parenthesis
