def is_x_mas_pattern(grid, row, col):
    """
    Check if there's an X-MAS pattern starting at the given row and column.
    The pattern looks like an X with MAS at each leg.
    """
    rows, cols = len(grid), len(grid[0])
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    def check_mas_pattern(forward=True):
        """
        Check for MAS (or SAM) patterns in different directions
        """
        directions = [
            # Horizontal, Vertical, and Diagonal directions
            [(0, 1), (0, 2), (0, 3)],     # Horizontal right
            [(1, 0), (2, 0), (3, 0)],     # Vertical down
            [(1, 1), (2, 2), (3, 3)],     # Diagonal down-right
            [(3, 1), (2, 2), (1, 3)]      # X-pattern
        ]
        
        mas_chars = 'MAS' if forward else 'SAM'
        
        for dx_sequence in directions:
            found = True
            for i, (dx, dy) in enumerate(dx_sequence):
                r, c = row + dx, col + dy
                if not is_valid(r, c) or grid[r][c] != mas_chars[i]:
                    found = False
                    break
            if found:
                return True
        return False
    
    # Check for both forward and backward MAS patterns
    return check_mas_pattern(forward=True) or check_mas_pattern(forward=False)

def count_x_mas_patterns(grid):
    """
    Count the number of X-MAS patterns in the grid.
    """
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'M':
                if is_x_mas_pattern(grid, row, col):
                    count += 1
    return count

# Read the input file
with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

# Count and print the number of X-MAS patterns
print(count_x_mas_patterns(grid))
