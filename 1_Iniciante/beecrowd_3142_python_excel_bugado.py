import sys

MAX_COLUMN_INDEX = 16384

for line in sys.stdin:
    column = line.strip()
    if not column:
        continue

    column_number = 0
    for char in column:
        column_number = column_number * 26 + (ord(char) - ord('A') + 1)

    if column_number > MAX_COLUMN_INDEX:
        print("Essa coluna nao existe Tobias!")
    else:
        print(column_number)