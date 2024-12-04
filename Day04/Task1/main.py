import numpy as np

def check_for_xmas(arr, row, col, direction, word, rows, cols):
    for i in range(len(word)):
        new_row = row + i * direction[0]
        new_col = col + i * direction[1]
        if not (0 <= new_row < rows and 0 <= new_col < cols):
            return False
        if arr[new_row][new_col] != word[i]:
            return False
    return True

def find_xmas(arr, word):
    rows = len(arr)
    cols = len(arr[0])
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for row in range(rows):
        for col in range(cols):
            for direction in directions:
                if check_for_xmas(arr, row, col, direction, word, rows, cols):
                    count += 1
    return count

if __name__ == '__main__':
    arr = []
    with open('text.txt', 'r') as f:
        for line in f: 
            arr.append(list(line.rstrip()))
            leng=len(list(line.rstrip()))

    word = "XMAS"
    result = find_xmas(arr, word)
    print(result) 

    