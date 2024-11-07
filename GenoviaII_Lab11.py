grades = []

while True:
    grades_input = input("Enter A Grade Of Student (or type 'done' to finish): ")
    
    if grades_input.lower() == 'done':
        break
    
    try:
        grade = float(grades_input)
        if 40 < grade < 100:
            grades.append(grade)
        else:
            print("Please enter a grade between 40 and 100")
    except ValueError:
        print("Please Enter a valid grade or 'done' to finish")
        
if grades:
    average_grade = sum(grades) / len(grades)
    print(f"\nAverage grade: {sum(grades)} / {len(grades)} = {average_grade:.2f}")
else:
    print("No Grades Entered")
    exit()  # Exit if no grades are entered

passing_grade = 75
passedStudents = [grade for grade in grades if grade >= passing_grade]  # Include equal to passing grade
passed = len(passedStudents)
total_students = len(grades)

if total_students > 0:
    passing_percent = (passed / total_students) * 100
    print(f"\nNumber of students passed: {passed} out of {total_students}")
    print(f"Passing Percentage: {passed}/{total_students} = {passing_percent:.2f}%")
else:
    print("No valid grades were entered.")

