grades = [] 
total = 0 
passing_count = 0 
passing_percent = 0 
print("Enter students' grades (between 40-100). Type 'done' to finish.")

attempts = 0

while True:
    user_input = input(f"Student {attempts + 1}: ")
    
    if user_input.lower() == "done":
        break
    
    try:
        grade = int(user_input)
        
        if 40 <= grade <= 100:
            grades.append(grade)
            total += grade
            
            if grade >= 75:
                passing_count += 1
        else:
            print("Grade must be between 40 and 100. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done' to finish.")
    
    attempts += 1

if len(grades) > 0:
    average_grade = total / len(grades)
    passing_percent = (passing_count / len(grades)) * 100
else:
    average_grade = 0
    passing_percent = 0

print("\nGrades you've entered:", grades)
print("Average grade:", average_grade)
print("Number of students who passed:", passing_count)
print("Passing percentage: {:.2f}%".format(passing_percent))
