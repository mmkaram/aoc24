def parse_disk_map(disk_map):
    """Parse the disk map into a list of file IDs and free spaces."""
    blocks = []
    file_id = 0
    is_file = True  # Alternate between file and space

    for i, char in enumerate(disk_map):
        length = int(char)
        if is_file:
            blocks.extend([file_id] * length)  # Add the file ID for file blocks
            file_id += 1
        else:
            blocks.extend(['.'] * length)  # Add '.' for free space
        is_file = not is_file

    return blocks

def compact_disk(blocks):
    """Compact the blocks by moving file blocks to the left."""
    write_index = 0

    for read_index in range(len(blocks)):
        if blocks[read_index] != '.':
            # Move file block to the left
            blocks[write_index] = blocks[read_index]
            write_index += 1

    # Fill the remaining space with '.'
    for i in range(write_index, len(blocks)):
        blocks[i] = '.'

    return blocks

def calculate_checksum(blocks):
    """Calculate the checksum by summing position * file ID for each file block."""
    checksum = 0
    for pos, block in enumerate(blocks):
        if block != '.':
            checksum += pos * block
    return checksum

def solve_disk_fragmenter(disk_map):
    """Solve the problem by parsing, compacting, and calculating the checksum."""
    blocks = parse_disk_map(disk_map)
    compacted_blocks = compact_disk(blocks)
    return calculate_checksum(compacted_blocks)

# Read the disk map from input.txt
with open("input.txt", "r") as file:
    disk_map = file.read().strip()

# Solve the problem
result = solve_disk_fragmenter(disk_map)
print("Checksum:", result)

