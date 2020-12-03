def trees_along_slope(rows, dx, dy):
    col = 0
    count = 0

    for row in rows[::dy]:
        if row[col % len(row)] == '#':
            count += 1
        col += dx

    return count


with open('./inputs/3_toboggan_trajectory.txt', 'r') as f:
    puzzle_input = [x for x in f.read().split('\n')]


print(trees_along_slope(puzzle_input, 3, 1))
t1 = trees_along_slope(puzzle_input, 1, 1)
t2 = trees_along_slope(puzzle_input, 3, 1)
t3 = trees_along_slope(puzzle_input, 5, 1)
t4 = trees_along_slope(puzzle_input, 7, 1)
t5 = trees_along_slope(puzzle_input, 1, 2)
print(t1 * t2 * t3 * t4 * t5)
