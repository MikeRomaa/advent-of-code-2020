def anyone_yes(groups):
    sum = 0
    
    for group in groups:
        questions = set()

        [questions.update(list(person)) for person in group.split('\n')]

        sum += len(questions)

    return sum


def everyone_yes(groups):
    sum = 0

    for group in groups:
        questions = set()

        for i, person in enumerate(group.split('\n')):
            if i == 0:
                questions = set(person)
            else:
                questions = questions.intersection(set(person))

        sum += len(questions)
    
    return sum


with open('./inputs/6_custom_customs.txt', 'r') as f:
    puzzle_input = [x for x in f.read().split('\n\n')]


print(anyone_yes(puzzle_input))
print(everyone_yes(puzzle_input))
