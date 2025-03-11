def compute_exam_scores(exam_scores):
    total_points = sum(exam_scores)
    average_score = total_points / len(exam_scores)
    return total_points, average_score

def main():
    last_name = input("Enter student's last name: ")
    scores = []
    for i in range(3):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)

    total_points, average_score = compute_exam_scores(scores)

    print(f"Student: {last_name}")
    print(f"Total Points: {total_points}")
    print(f"Average Exam Score: {average_score:.2f}")

main()

