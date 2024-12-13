def find_trails(heightmap):
  rows, cols = len(heightmap), len(heightmap[0])
  total_score = 0

  def explore_path(row, col, visited):
    if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols):
      return set()
    visited.add((row, col))
    current_height = heightmap[row][col]
    if current_height == 9:
      return {(row, col)}
    reachable_nines = set()
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      new_row, new_col = row + dr, col + dc
      if 0 <= new_row < rows and 0 <= new_col < cols and heightmap[new_row][new_col] == current_height + 1:
        reachable_nines.update(explore_path(new_row, new_col, visited.copy()))
    return reachable_nines

  for row in range(rows):
    for col in range(cols):
      if heightmap[row][col] == 0:  
        total_score += len(explore_path(row, col, set()))

  return total_score

with open("text.txt", "r") as file:
  heightmap = [[int(x) for x in line.strip()] for line in file]

print(find_trails(heightmap))