def calculate_mpg(miles, gallons):
    return miles / gallons if gallons != 0 else 0

def main():
    trip_count = 0
    while True:
        destination = input("Enter destination city: ")
        miles = float(input("Enter miles travelled: "))
        gallons = float(input("Enter gallons used: "))
        
        mpg = calculate_mpg(miles, gallons)
        trip_count += 1
        
        print(f"Destination: {destination}, Miles: {miles}, Miles per Gallon: {mpg:.2f}")
        
        continue_program = input("Do you want to continue? (Yes or No): ")
        if continue_program.lower() != "yes":
            break
    
    print(f"\nTotal number of trips entered: {trip_count}")

main()

