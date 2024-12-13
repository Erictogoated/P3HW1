#Eric Corbett
#10/16/2024
#P2HW2
# Making lists storing and caculating the information in them 




#Ask user for grades on module 1-6
#Calculate the given grades
#Display results of the caculations 

grades = []


grades.append(float(input("Enter the grade for Module 1: ")))
grades.append(float(input("Enter the grade for Module 2: ")))
grades.append(float(input("Enter the grade for Module 3: ")))
grades.append(float(input("Enter the grade for Module 4: ")))
grades.append(float(input("Enter the grade for Module 5: ")))
grades.append(float(input("Enter the grade for Module 6: ")))


lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)


print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Sum of grades: {sum_of_grades}")
print(f"Average grade: {average_grade:.2f}")
