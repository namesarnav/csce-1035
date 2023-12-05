rows = 5
cols = 1
for row in range(rows):
    for col in range(cols):
        if (row+col) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    cols += 1   
    print()