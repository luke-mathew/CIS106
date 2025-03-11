def display_players_and_averages(names, averages):
    for i in range(len(names)):
        print(f"{names[i]}: {averages[i]}")

def search_player(names, averages, last_name):
    if last_name in names:
        index = names.index(last_name)
        print(f"Player: {names[index]}, Batting Average: {averages[index]}")
    else:
        print("Player not found.")

def main():
    # Load data from a file (create a file `players.txt` with player names and averages)
    names = []
    averages = []

    with open('players.txt', 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):  # Assuming each player name is followed by their average
            names.append(lines[i].strip())
            averages.append(float(lines[i+1].strip()))

    display_players_and_averages(names, averages)

    while True:
        search_name = input("Enter a player's last name to search (or type 'exit' to quit): ")
        if search_name.lower() == 'exit':
            break
        search_player(names, averages, search_name)

main()

