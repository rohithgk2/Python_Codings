
from itertools import product

def sudokuPuzzle():
    puzzle = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    for (row,col) in product(range(0,9),repeat=2):
        if puzzle[row][col] ==0: #find unassigned cell
            for num in range(1,10):
                allowed = True #Check if num is allowed in row.col
                for i in range(0,9):
                    if (puzzle[row][i] == num) or (puzzle[i][col]==0):
                        allowed = False;break
                for (i,j) in product(range(0,3),repeat=2):
                    if puzzle[row-row%3+i][col-col%3+j] == num:
                        allowed = False;break
                if allowed:
                    puzzle[row][col] = num
                    if trial := sudokuPuzzle():
                        return trial
                    else:
                        puzzle[row][col] = 0
            return False
    return puzzle
def main():

    print(sudokuPuzzle())

if __name__ == '__main__':
    main()
