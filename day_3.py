def process_input(file):
    input_list = []
    while (line := file.readline().rstrip('\n')):
        input_list.append(line)
    return input_list

def collisions(input_list, right, down):
    count = 0
    how_long = len(input_list[0])
    for i, trees in enumerate(input_list):
        if i % down != 0:
            continue
        fixer = i // down
        line_position = (fixer * right) % how_long
        if trees[line_position] == '#':
            count += 1
    return count

