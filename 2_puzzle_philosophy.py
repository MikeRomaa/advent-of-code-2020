def valid_passwords(passwords):
    count = 0

    for password in passwords:
        policy, pw = password.split(': ')
        range, letter = policy.split(' ')
        min, max = range.split('-')

        if int(max) >= pw.count(letter) >= int(min):
            count += 1

    return count


def valid_passwords_two(passwords):
    count = 0

    for password in passwords:
        policy, pw = password.split(': ')
        range, letter = policy.split(' ')
        first, second = range.split('-')

        if (pw[int(first) - 1] == letter) ^ (pw[int(second) - 1] == letter):
            count += 1

    return count


with open('./inputs/2_password_philosophy.txt', 'r') as f:
    puzzle_input = [x for x in f.read().split('\n')]


print(valid_passwords(puzzle_input))
print(valid_passwords_two(puzzle_input))

