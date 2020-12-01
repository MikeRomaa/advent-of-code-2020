def report_repair_two(entries, sum):
    entry_map = {}
    for entry in entries:
        if sum - entry in entry_map:
            return [entry, sum - entry]
        else:
            entry_map[entry] = None
    return []


def report_repair_three(entries, sum):
    diff_map = {sum - entry for entry in entries}
    for diff in diff_map:
        diff_entries = report_repair_two(entries, diff)
        if len(diff_entries) > 0:
            return [sum - diff] + diff_entries
    return []


def multiply_array(array):
    prod = 1
    for x in array:
        prod *= x
    return prod


with open('./inputs/1_report_repair.txt', 'r') as f:
    puzzle_input = [int(x) for x in f.read().split('\n')]


print(multiply_array(report_repair_two(puzzle_input, 2020)))
print(multiply_array(report_repair_three(puzzle_input, 2020)))
