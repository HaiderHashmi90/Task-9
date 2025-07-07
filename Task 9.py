def read_student_marks(filepath):
    """
    Reads student names and marks from a text file, handling errors.
    Returns a dictionary of valid student marks.
    """
    student_marks = {}
    line_number = 0
    with open(filepath, 'r') as file:
        for line in file:
            line_number += 1
            line = line.strip()  # Remove leading/trailing whitespace and newline characters

            if not line:  # Skip empty lines
                continue

            parts = line.split(',')

            try:
                # Edge case: Missing values (e.g., Ali,) or (e.g., ,87) or (e.g., ,)
                if len(parts) != 2 or not parts[0].strip() or not parts[1].strip():
                    raise ValueError("Missing name or mark.")

                name = parts[0].strip()
                mark_str = parts[1].strip()

                # Edge case: Invalid data types (e.g., Ahmed,abc)
                mark = int(mark_str)

                student_marks[name] = mark

            except ValueError as e:
                print(f"Skipping line {line_number}: '{line}' - Error: {e}")
            except Exception as e:  # Catch any other unexpected errors
                print(f"Skipping line {line_number}: '{line}' - An unexpected error occurred: {e}")

    return student_marks


def analyze_student_marks(student_marks):
    """
    Prints each student's mark, calculates and displays the average.
    Handles empty data gracefully.
    """
    if not student_marks:
        print("\nNo valid student data to analyze.")
        return

    print("\n--- Student Marks ---")
    total_marks = 0
    for name, mark in student_marks.items():
        print(f"{name}: {mark}")
        total_marks += mark

    try:
        average_mark = total_marks / len(student_marks)
        print(f"\n--- Analysis ---")
        print(f"Total students: {len(student_marks)}")
        print(f"Average mark: {average_mark:.2f}")  # Format to 2 decimal places
    except ZeroDivisionError:
        # This case should ideally be caught by the initial `if not student_marks:` check,
        # but included for robustness as per instructions.
        print("\nNo students with valid marks to calculate an average.")
    except Exception as e:
        print(f"An error occurred during calculation: {e}")


# --- Main execution ---
if __name__ == "__main__":
    # Create a dummy text file for testing
    # You can change the content of 'marks.txt' to test different cases
    with open('marks.txt', 'w') as f:
        f.write("Zara,87\n")
        f.write("Rida,91\n")
        f.write("Ali,\n")  # Missing mark
        f.write("Ahmed,abc\n")  # Invalid mark type
        f.write("Hamza,75\n")
        f.write("Usman,\n")
        f.write(",100\n")  # Missing name
        f.write("Hina,95\n")
        f.write("Fahad,xyz\n")  # Invalid mark type
        f.write("NoCommaYet\n")  # No comma
        f.write("EmptyLine\n")
        f.write("\n")  # Empty line
        f.write("ValidStudent,88\n")
        f.write("Another,99,extra\n")  # Too many parts

    # Define the file path
    file_path = 'marks.txt'

    # Read student marks from the file
    valid_marks = read_student_marks(file_path)
    print("\n--- Valid Student Data Loaded ---")
    print(valid_marks)

    # Analyze and print results
    analyze_student_marks(valid_marks)

    # Test with an empty file (optional)
    # with open('empty_marks.txt', 'w') as f:
    #     pass
    # empty_marks = read_student_marks('empty_marks.txt')
    # analyze_student_marks(empty_marks)
