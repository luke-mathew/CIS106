def calculate_batting_average(hits, at_bats):
    return hits / at_bats if at_bats != 0 else 0

def main():
    player_count = 0
    while True:
        last_name = input("Enter player's last name: ")
        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at bats: "))
        
        batting_average = calculate_batting_average(hits, at_bats)
        player_count += 1
        
        print(f"{last_name}: Batting Average: {batting_average:.3f}")
        
        continue_program = input("Do you want to continue? (Yes or No): ")
        if continue_program.lower() != "yes":
            break
    
    print(f"\nTotal number of players entered: {player_count}")

main()

