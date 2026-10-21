# Grade Calculator Program
# Calculates average score and determines letter grade

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("=== Student Grade Calculator ===")
    
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects <= 0:
            print("Number of subjects must be greater than zero.")
            return

        scores = []
        for i in range(1, num_subjects + 1):
            score = float(input(f"Enter score for subject {i} (0-100): "))
            while score < 0 or score > 100:
                print("Invalid score! Please enter a value between 0 and 100.")
                score = float(input(f"Enter score for subject {i} (0-100): "))
            scores.append(score)

        average = sum(scores) / len(scores)
        letter_grade = calculate_grade(average)

        print("\n--- Summary ---")
        print(f"Total Subjects: {num_subjects}")
        print(f"Average Score:  {average:.2f}")
        print(f"Final Grade:    {letter_grade}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    main()
