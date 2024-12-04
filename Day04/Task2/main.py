def check_for_mas(arr,row, col, direction, word, rows, cols):
    for i in (-1,1):
        new_row = row + i * direction[0] 
        new_col = col + i * direction[1]
        new_row2 = row + i * -direction[0]
        new_col2 = col + i * -direction[1]
        if not (0 <= new_row < rows and 0 <= new_col < cols):
            return False
        if (arr[new_row][new_col] != word[2] or arr[new_row2][new_col2] != word[0]) and (arr[new_row][new_col] != word[0] or arr[new_row2][new_col2] != word[2]):
            return False
    return True

def find_xmas(arr, word):
    rows = len(arr)
    cols = len(arr[0])
    count = 0
    directions = [(1, 1)]
    for row in range(rows):
        for col in range(cols):
            if arr[row][col] == 'A' and (row>0 and row<rows-1) and (col>0 and col<cols-1) :
                for direction in directions:
                    opposite_direction = (-direction[0], direction[1])
                    if check_for_mas(arr, row, col, direction, word, rows, cols) and check_for_mas(arr, row, col, opposite_direction, word, rows, cols):
                        count += 1
    return count

if __name__ == '__main__':
    arr = []
    with open('text.txt', 'r') as f:
        for line in f: 
            arr.append(list(line.rstrip()))
            leng=len(list(line.rstrip()))
    word = "MAS"
    result = find_xmas(arr, word)
    print(result) 

    