def calculate_tuition():
    total_tuition = 0
    student_count = 0
    with open("students.txt", "r") as file:
        lines = file.readlines()

    for i in range(0, len(lines), 3):  # Every three lines: name, district, credits
        last_name = lines[i].strip()
        district_code = lines[i + 1].strip()
        credits = int(lines[i + 2].strip())
        
        if district_code == "I":
            cost_per_credit = 250
        else:
            cost_per_credit = 500
        
        tuition_owed = credits * cost_per_credit
        total_tuition += tuition_owed
        student_count += 1
        
        print(f"{last_name}: Credits Taken = {credits}, Tuition Owed = ${tuition_owed:,.2f}")
    
    print(f"\nTotal Tuition Owed: ${total_tuition:,.2f}")
    print(f"Number of Students: {student_count}")

calculate_tuition()

