def fibonacci():
    n1, n2 = 1, 1
    print(f"{n1}, {n2}", end=", ")
    for _ in range(3, 21):
        n3 = n1 + n2
        print(n3, end=", " if _ < 20 else "\n")
        n1, n2 = n2, n3

fibonacci()

