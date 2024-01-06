#creating a 2-D matrix by getting input for rows and columns from the user

a = int(input("Enter number of rows: "))
b = int(input("Enter number of columns: "))
matrix = []
for i in range(a):
    row = []
    for j in range(b):
        element = int(input(f"Enter element at position ({i+1},{j+1}): "))
        row.append(element)
    matrix.append(row)
print("Matrix - ")
for row in matrix:
    print(row)
