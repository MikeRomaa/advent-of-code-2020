def seat_ids(seats):
    rows = [i for i in range(128)]
    cols = [i for i in range(8)]
    seat_ids = []

    for seat in seats:
        row = rows
        col = cols

        for partition in seat[:7]:
            middle = len(row) // 2
            row = row[:middle] if partition == 'F' else row[middle:]

        for partition in seat[7:]:
            middle = len(col) // 2
            col = col[:middle] if partition == 'L' else col[middle:]

        seat_ids += [row[0] * 8 + col[0]]
    
    return seat_ids
        

def find_missing_id(ids):
    return min(set(range(15, 126 * 8)) - set(ids))


with open('./inputs/5_binary_boarding.txt', 'r') as f:
    puzzle_input = [x for x in f.read().split('\n')]


print(max(seat_ids(puzzle_input)))
print(find_missing_id(seat_ids(puzzle_input)))
