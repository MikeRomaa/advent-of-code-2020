def valid_passports(passports):
    count = 0

    for passport in passports:
        fields_list = passport.replace('\n', ' ').split(' ')
        fields_dict = dict(field.split(':') for field in fields_list)
        
        if validate_fields(fields_dict):
            count += 1
    
    return count


def validate_fields(fields):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    for req in required_fields:
        if req not in fields:
            return False
    
    if int(fields['byr']) > 2002 or int(fields['byr']) < 1920:
        return False
    
    if int(fields['iyr']) > 2020 or int(fields['iyr']) < 2010:
        return False
    
    if int(fields['eyr']) > 2030 or int(fields['eyr']) < 2020:
        return False

    if fields['hgt'][-2:] not in ['in', 'cm']:
        return False
    elif fields['hgt'][-2:] == 'cm':
        if int(fields['hgt'][:-2]) > 193 or int(fields['hgt'][:-2]) < 150:
            return False
    elif fields['hgt'][-2:] == 'in':
        if int(fields['hgt'][:-2]) > 76 or int(fields['hgt'][:-2]) < 59:
            return False

    if fields['hcl'][0] != '#':
        return False
    try:
        int(fields['hcl'][1:], 16)
    except ValueError:
        return False

    if fields['ecl'] not in valid_ecl:
        return False

    if len(fields['pid']) != 9:
        return False

    return True


with open('./inputs/4_passport_processing.txt', 'r') as f:
    puzzle_input = [x for x in f.read().split('\n\n')]


print(valid_passports(puzzle_input))
