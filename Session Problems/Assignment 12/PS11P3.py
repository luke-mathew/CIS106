def find_highest_and_lowest(names, scores):
    high_var = 0
    low_var = 999
    high_index = -1
    low_index = -1

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print(f"Highest score: {names[high_index]} with score {high_var}")
    print(f"Lowest score: {names[low_index]} with score {low_var}")

def main():
    # Initialize an array of last names and parallel array for exam scores
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", 
                  "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    scores = [85, 92, 78, 88, 76, 90, 95, 84, 91, 89]

    find_highest_and_lowest(last_names, scores)

main()

