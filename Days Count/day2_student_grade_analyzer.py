# Day 2: Student Grade Analyzer
# Phase 0: Foundations - Week 1

def calculate_grade(score):
    """
    Convert a score (0-100) to a letter grade.
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: <60
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def analyze_grades(students_scores):
    """
    Analyze a dictionary of students and their scores.
    Returns a summary with average, highest, lowest, and grades.
    """
    if not students_scores:
        print("No students provided!")
        return None

    scores_list = list(students_scores.values())

    # Calculate statistics
    average = sum(scores_list) / len(scores_list)
    highest = max(scores_list)
    lowest = min(scores_list)

    # Assign grades
    grades = {}
    for student, score in students_scores.items():
        grades[student] = calculate_grade(score)

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grades": grades,
        "students_scores": students_scores
    }


def generate_report(analysis):
    """
    Generate a formatted report from analysis.
    """
    report = []
    report.append("=" * 60)
    report.append("STUDENT GRADE REPORT")
    report.append("=" * 60)
    report.append("")

    # Class statistics
    report.append("CLASS STATISTICS:")
    report.append(f"  Average Score: {analysis['average']:.2f}")
    report.append(f"  Highest Score: {analysis['highest']}")
    report.append(f"  Lowest Score: {analysis['lowest']}")
    report.append("")

    # Individual grades
    report.append("INDIVIDUAL GRADES:")
    for student, score in analysis['students_scores'].items():
        grade = analysis['grades'][student]
        report.append(f"  {student}: {score}/100 ({grade})")

    report.append("")
    report.append("=" * 60)

    return "\n".join(report)


def save_report(report, filename="grade_report.txt"):
    """
    Save report to a file.
    """
    with open(filename, "w") as f:
        f.write(report)
    print(f"Report saved to {filename}")


# Main program
if __name__ == "__main__":
    # Sample data (you can modify this)
    students_scores = {
        "Aryan": 92,
        "Priya": 85,
        "Kumar": 78,
        "Anita": 95,
        "Rajesh": 88,
        "Neha": 73
    }

    # Analyze grades
    analysis = analyze_grades(students_scores)

    # Generate and print report
    report = generate_report(analysis)
    print(report)

    # Save to file
    save_report(report)


my_class ={
    "Aryan" : 94,
    "Rahul" : 58,
    "el": 68,
    "suman" : 72,
    "ashim" : 89

}

analysis2 = analyze_grades(my_class)
report2 = generate_report(analysis2)

print("\n\nMY CLASS REPORT:")
print(report2)
save_report(report2,"My_class_report.txt")
