# User inputs start, stop, and increment values
start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
increment = int(input("Enter increment value: "))

# Loop to display values
num = start
while num <= stop:
    print(num, end=" ")
    num += increment

