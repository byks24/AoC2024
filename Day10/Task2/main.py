def find_trail_ratings(heightmap):
  rows, cols = len(heightmap), len(heightmap[0])
  total_rating = 0

  def explore_path(row, col, path, visited):
    if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols):
      return set()
    visited.add((row, col))
    path.append((row, col))
    current_height = heightmap[row][col]
    if current_height == 9:
      return {tuple(path)} 
    paths_to_nines = set()
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      new_row, new_col = row + dr, col + dc
      if 0 <= new_row < rows and 0 <= new_col < cols and heightmap[new_row][new_col] == current_height + 1:
        paths_to_nines.update(explore_path(new_row, new_col, path.copy(), visited.copy()))
    return paths_to_nines

  for row in range(rows):
    for col in range(cols):
      if heightmap[row][col] == 0: 
        paths = explore_path(row, col, [], set())
        total_rating += len(paths) 

  return total_rating

with open("text.txt", "r") as file:
  heightmap = [[int(x) for x in line.strip()] for line in file]

print(find_trail_ratings(heightmap))