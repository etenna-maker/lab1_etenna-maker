import csv
import sys
import os

def load_csv_data():
    filename = input("Enter the name of the CSV file to process (for example, grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    print("\n--- Processing Grades ---")

    # a) Validate scores are between 0 and 100
    for assignment in data:
        if assignment['score'] < 0 or assignment['score'] > 100:
            print(f"Error: Score for '{assignment['assignment']}' is out of range (0-100).")
            sys.exit(1)
    print("All scores are valid.")

    # b) Validate weights
    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    for assignment in data:
        total_weight += assignment['weight']
        if assignment['group'] == 'Formative':
            formative_weight += assignment['weight']
        elif assignment['group'] == 'Summative':
            summative_weight += assignment['weight']

    if total_weight != 100:
        print(f"Error: Total weights add up to {total_weight}, not 100.")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Error: Formative weights add up to {formative_weight}, not 60.")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Error: Summative weights add up to {summative_weight}, not 40.")
        sys.exit(1)
    print("All weights are valid.")

    # c) Calculate final grade and GPA
    total_grade = 0
    formative_score = 0
    summative_score = 0

    for assignment in data:
        weighted_score = (assignment['score'] * assignment['weight']) / 100
        total_grade += weighted_score
        if assignment['group'] == 'Formative':
            formative_score += weighted_score
        elif assignment['group'] == 'Summative':
            summative_score += weighted_score

    formative_percentage = (formative_score / formative_weight) * 100
    summative_percentage = (summative_score / summative_weight) * 100
    gpa = (total_grade / 100) * 5.0

    print(f"Formative Score: {formative_percentage:.2f}%")
    print(f"Summative Score: {summative_percentage:.2f}%")
    print(f"Final Grade: {total_grade:.2f}%")
    print(f"GPA: {gpa:.2f} / 5.0")
    # d) Pass/Fail per category
    formative_passed = formative_percentage >= 50
    summative_passed = summative_percentage >= 50

    if formative_passed and summative_passed:
        print("\nFinal Status: PASSED")
    else:
        print("\nFinal Status: FAILED")
        if not formative_passed:
            print("  - Failed Formative category")
        if not summative_passed:
            print("  - Failed Summative category")
# e) Resubmission logic
    failed_formative = []
    for assignment in data:
        if assignment['group'] == 'Formative' and assignment['score'] < 50:
            failed_formative.append(assignment)

    if len(failed_formative) > 0:
        highest_weight = 0
        for assignment in failed_formative:
            if assignment['weight'] > highest_weight:
                highest_weight = assignment['weight']

        print("\nEligible for Resubmission:")
        for assignment in failed_formative:
            if assignment['weight'] == highest_weight:
                print(f"  - {assignment['assignment']} (Weight: {assignment['weight']}, Score: {assignment['score']})")
    else:
        print("\nNo failed Formative assignments. No resubmission needed.")git add grade-evaluator.py

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
    