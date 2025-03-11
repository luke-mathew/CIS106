def calculate_bowler_scores(scores, handicap):
    average_score = sum(scores) / len(scores)
    average_score_with_handicap = average_score + handicap
    return average_score, average_score_with_handicap

def main():
    bowler_last_name = input("Enter bowler's last name: ")
    scores = []
    for i in range(3):
        score = float(input(f"Enter game score {i+1}: "))
        scores.append(score)
    handicap = float(input("Enter handicap: "))

    average_score, average_score_with_handicap = calculate_bowler_scores(scores, handicap)

    print(f"Bowler: {bowler_last_name}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Average Score with Handicap: {average_score_with_handicap:.2f}")

main()

