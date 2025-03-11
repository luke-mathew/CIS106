def calculate_tuition(credits, district_code):
    rate = 250 if district_code == "I" else 550
    return credits * rate

def main():
    total_tuition = 0
    while True:
        last_name = input("Enter student's last name: ")
        credits = int(input("Enter credit hours: "))
        district_code = input("Enter district code (I for in-district, O for out-of-district): ")
        
        tuition_owed = calculate_tuition(credits, district_code)
        total_tuition += tuition_owed
        
        print(f"{last_name}: Tuition Owed: ${tuition_owed:.2f}")
        
        continue_program = input("Do you want to continue? (Yes or No): ")
        if continue_program.lower() != "yes":
            break
    
    print(f"\nTotal tuition owed: ${total_tuition:.2f}")

main()

