def display_names(names):
    for name in names:
        print(name)

def display_names_reverse(names):
    for name in reversed(names):
        print(name)

def main():
    # Initialize an array with 10 last names
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", 
                  "Davis", "Miller", "Wilson", "Moore", "Taylor"]

    print("Names in normal order:")
    display_names(last_names)

    print("\nNames in reverse order:")
    display_names_reverse(last_names)

main()

