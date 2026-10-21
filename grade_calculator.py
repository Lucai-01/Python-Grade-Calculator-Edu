# grade_calculator.py
def calculate_grade():
    print("--- Simple Grade Calculator ---")
    try:
        prelim = float(input("Enter Prelim grade: "))
        midterm = float(input("Enter Midterm grade: "))
        finals = float(input("Enter Finals grade: "))
        
        final_grade = (prelim * 0.3) + (midterm * 0.3) + (finals * 0.4)
        print(f"Your final grade is: {final_grade:.2f}")
    except ValueError:
        print("Please enter valid numeric grades.")

if __name__ == "__main__":
    calculate_grade()
