# Open the input file
with open("input.txt", "r") as file:
    # Initialize empty lists for the two columns
    left_list = []
    right_list = []

    # Read each line in the file
    for line in file:
        # Strip whitespace and check if the line is valid
        stripped_line = line.strip()
        if stripped_line:  # Ensure the line is not empty
            parts = stripped_line.split()
            if len(parts) == 2:  # Ensure there are exactly two columns
                left_id, right_id = parts
                left_list.append(int(left_id))
                right_list.append(int(right_id))

# Print the lists to verify
# print("Left List:", left_list)
# print("Right List:", right_list)

left_list.sort()
right_list.sort()

similarity_score = 0
memo = {}

for l in left_list:
    # if found in memo just dump
    if l in memo:
        similarity_score += memo[l]
    # find that number in the list
    # if found, iterate thru the list until the number changes
    if l in right_list:
        index = right_list.index(l)
        found = 0
        while right_list[index] == l:
            found += 1
            index += 1
        memo[l] = l * found
        similarity_score += memo[l]
    # if not found, go to the next number

print(similarity_score)
