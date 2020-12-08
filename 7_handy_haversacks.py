def rules_to_dict(raw):
    rules = {}

    for rule in raw:
        outer, contents = rule.split(' bags contain ')
        if 'no other bags' not in rule:
            contents = contents.replace(' bags', '').replace(' bag', '').replace('.', '')

            rules[outer] = [(int(bag[:2]), bag[2:]) for bag in contents.split(', ')]
        else:
            rules[outer] = []

    return rules


def can_contain(colors, rules):
    bags = set()

    for outer, contents in rules.items():
        for color in colors:
            if color in [content[1] for content in contents]:
                bags.add(outer)

    if bags:
        bags.update(can_contain(bags, rules))

    return bags


def count_contents(color, rules):
    total = 1

    for bag in rules[color]:
        total += bag[0] * count_contents(bag[1], rules)
    
    return total


with open('./inputs/7_handy_haversacks.txt', 'r') as f:
    puzzle_input = [x for x in f.read().split('\n')]


print(len(can_contain(['shiny gold'], rules_to_dict(puzzle_input))))
print(count_contents('shiny gold', rules_to_dict(puzzle_input)) - 1)