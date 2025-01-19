import sys

number_tests = int(sys.stdin.readline())
size = 9
for case in range(number_tests):
    sudoku = []
    for _ in range(size):
        sudoku.append(list(map(int, sys.stdin.readline().split())))
    valid = True
    
    for i in range(size):
        for j in range(size):
            if sudoku[i].count(sudoku[i][j]) > 1:
                valid = False
                break
            column = []
            
            for k in range(size):
                column.append(sudoku[k][j])
            
            if column.count(sudoku[i][j]) > 1:
                valid = False
                break
            
        if not valid:
            break
        
    for i in range(0, size, 3):
        for j in range(0, size, 3):
            square = []
            
            for k in range(3):
                for l in range(3):
                    square.append(sudoku[i + k][j + l])
                    
            if square.count(sudoku[i][j]) > 1:
                valid = False
                break
            
        if not valid:
            break

    print(f'Instancia {case + 1}')
    print('SIM' if valid else 'NAO')
    print()