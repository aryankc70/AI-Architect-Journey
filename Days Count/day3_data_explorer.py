import csv

def load_csv(filename):
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data

def summarize_column(data,column):
    values = [float(row[column]) for row in data]
    return {
        "min" : min(values),
        "max" : max(values),
        "mean" : sum(values)/len(values),
        "count" : len(values)
    }

def value_count(data,coloumn):
    freq = {}
    for row in data:
        val = row[coloumn]
        freq[val] = freq.get(val, 0)+1
    return freq

def generate_report(summary,counts,coloumn):
    lines = ["="*50,
        f"DATA SUMMARY FOR '{coloumn}'",
        "="*50]
    lines.append(f"Min: {summary['min']}")
    lines.append(f"Max: {summary['max']}")
    lines.append(f"Mean: {summary['mean']}")
    lines.append(f"Count: {summary['count']}")
    lines.append("")
    lines.append(f"VALUE COUNTS FOR '{coloumn}'")
    for val,count in counts.items():
        lines.append(f" {val}: {count}")
    lines.append("="*50)
    return "\n".join(lines)


if __name__ == "__main__":
    data = load_csv("students.csv")

    # Score Summary
    score_summary = summarize_column(data, "Score")
    score_counts = value_count(data, "Score")
    score_report = generate_report(score_summary, score_counts, "Score")
    print(score_report)

    with open("Score_summary.txt", "w") as f:
        f.write(score_report)

    # Age Summary
    age_summary = summarize_column(data, "Age")
    age_counts = value_count(data, "Age")
    age_report = generate_report(age_summary, age_counts, "Age")
    print(age_report)

    with open("Age_summary.txt", "w") as f:
        f.write(age_report)
