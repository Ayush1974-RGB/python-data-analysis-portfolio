# Student Grade Calculator


# Function for grade calculation
def calculate_grade(marks):

    if marks >= 90:
        return "A", "Excellent Work! 🌟"

    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"

    elif marks >= 70:
        return "C", "Good Job! 😊"

    elif marks >= 60:
        return "D", "Keep Practicing! 📚"

    else:
        return "F", "Don't Give Up! 💪"


# Get student name
student_name = input("Enter student name: ")


# Input validation using while loop
while True:

    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break

        else:
            print("Enter marks between 0 and 100")

    except:
        print("Invalid input! Enter numbers only")


# Function call
grade, message = calculate_grade(marks)


# Final output
print("\nResult for", student_name)

print("Marks :", marks)
print("Grade :", grade)
print("Message :", message)