def calculate_fencing_cost(garden_map):
    rows, cols = len(garden_map), len(garden_map[0])
    visited = set()
    total_cost = 0

    def explore_region(row, col, plant_type):
        stack = [(row, col)]
        area, perimeter = 0, 0
        while stack:
            row, col = stack.pop()
            if (
                0 <= row < rows
                and 0 <= col < cols
                and garden_map[row][col] == plant_type
                and (row, col) not in visited
            ):
                visited.add((row, col))
                area += 1
                perimeter += 4  # Assume each plot has 4 sides initially

                # Check neighbors and adjust perimeter for shared borders
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = row + dr, col + dc
                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and garden_map[new_row][new_col] == plant_type
                        and (new_row, new_col) not in visited  # Only subtract if neighbor is not already visited
                    ):
                        perimeter -= 2  # Subtract 2 for each shared border
                    stack.append((new_row, new_col))

        return area, perimeter

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                plant_type = garden_map[row][col]
                area, perimeter = explore_region(row, col, plant_type)
                total_cost += area * perimeter

    return total_cost

# Read the garden map from the file "text.txt"
with open("text.txt", "r") as file:
    garden_map = [line.strip() for line in file]

total_fencing_cost = calculate_fencing_cost(garden_map)
print(f"The total price of fencing all regions is: {total_fencing_cost}")