# Step 1: Create a list from user input
num_items = int(input("Enter the number of items in the list: "))
num_list = []
for _ in range(num_items):
    num = int(input("Enter an integer: "))
    num_list.append(num)
print("Initial list:", num_list)

# Step 2: Insert 99 at position 1
num_list.insert(1, 99)
print("After inserting 99 at position 1:", num_list)

# Step 3: Replace 99 with 100
if 99 in num_list:
    index_99 = num_list.index(99)
    num_list[index_99] = 100
print("After replacing 99 with 100:", num_list)

# Step 4: Extend first list with a second list
second_list = [500, 600, 700, 800, 900]
print("Second list:", second_list)
num_list.extend(second_list)
print("After extending with second list:", num_list)

# Step 5: Remove value 800
if 800 in num_list:
    num_list.remove(800)
print("After removing 800:", num_list)

# Step 6: Remove the third item
if len(num_list) > 2:
    del num_list[2]
print("After removing third item:", num_list)

# Step 7: Create grades list
grades = ["A", "B", "C", "A", "A", "C"]
print("Grades list:", grades)

# Step 8: Count the number of A grades
count_A = grades.count("A")
print("Number of A grades:", count_A)

# Step 9: Find index of first B grade
if "B" in grades:
    index_B = grades.index("B")
    print("Index of first B grade:", index_B)

# Step 10: Check for grade F
if "F" not in grades:
    print("Grade F is not in the list.")

# Step 11: Clear second list
second_list.clear()
print("Second list after clearing:", second_list)

# Step 12: Delete second list and try to display it
del second_list
try:
    print(second_list)
except NameError:
    print("Error: second_list no longer exists.")

# Step 13: Create a list of players
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print("Players list:", players)

# Step 14: Sort the players list
players.sort()
print("Sorted players list:", players)

# Step 15: Copy the players list
players2 = players.copy()
print("Copied players2 list:", players2)

# Step 16: Reverse players2 and display both lists
players2.reverse()
print("Original players list:", players)
print("Reversed players2 list:", players2)

