def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    target_len = len(target)
    occurrences = 0

    for i in range(rows):
        for j in range(cols - target_len + 1):
            if grid[i][j:j + target_len] == target:
                occurrences += 1
            if grid[i][j:j + target_len] == target[::-1]:
                occurrences += 1

    for i in range(cols):
        for j in range(rows - target_len + 1):
            vertical_str = ''.join([grid[j+k][i] for k in range(target_len)])
            if vertical_str == target:
                occurrences += 1
            if vertical_str == target[::-1]:
                occurrences += 1

    for i in range(rows - target_len + 1):
        for j in range(cols - target_len + 1):
            diagonal_str = ''.join([grid[i+k][j+k] for k in range(target_len)])
            if diagonal_str == target:
                occurrences += 1
            if diagonal_str == target[::-1]:
                occurrences += 1

    for i in range(rows - target_len + 1):
        for j in range(target_len - 1, cols):
            diagonal_str = ''.join([grid[i+k][j-k] for k in range(target_len)])
            if diagonal_str == target:
                occurrences += 1
            if diagonal_str == target[::-1]:
                occurrences += 1

    return occurrences

def load_grid_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def main():
    filename = "input.txt"  # Replace with your input file name
    grid = load_grid_from_file(filename)
    occurrences = find_xmas(grid)
    print(occurrences)

if __name__ == "__main__":
    main()

