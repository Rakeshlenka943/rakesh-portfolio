# variables_conditionals.py
# Tiny demo of variables, input, type conversion, and conditionals

name = input("Enter your name: ")
age_str = input("Enter your age: ")

# Convert age safely
try:
    age = int(age_str)
except ValueError:
    print("Please enter a valid number for age.")
    raise SystemExit(1)

# Example boolean
is_student = True  # pretend you're a student for the demo

# Basic if/elif/else
if age < 13:
    stage = "kid"
elif age < 18:
    stage = "teen"
else:
    stage = "adult"

print(f"Hello {name}, you are an {stage}.")

# Conditional (ternary) expression
vote_msg = "eligible to vote" if age >= 18 else "not eligible to vote"
print(f"You are {vote_msg} in India.")

# Function + condition
def can_get_student_discount(is_student: bool, age: int) -> bool:
    return is_student and age >= 13

print("Student discount:", can_get_student_discount(is_student, age))
