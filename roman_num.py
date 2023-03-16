import string

DICT_OF_NUMERALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_dec(num):
    dic = dict(DICT_OF_NUMERALS)
    if len(num) == 1:
        return dic[num[0]]
    if num == '':
        return 0
    last = num[-1]
    pent = num[-2]
    if dic[last] > dic[pent]:
        return dic[last] - dic[pent] + roman_to_dec(num[:-2])
    return dic[last] + roman_to_dec(num[:-1])


def single_to_roman(num, letters):
    assert 0 <= num < 10, 'Must be single digit'
    letter = ''
    if len(letters) == 1:
        for _ in range(num):
            letter += letters[0]
        return letter
    if num == 9:
        letter = f'{letters[0]}{letters[2]}'
    elif num == 4:
        letter = f'{letters[0]}{letters[1]}'
    elif 9 > num >= 5:
        letter = f'{letters[1]}{single_to_roman(num - 5, letters)}'
    else:
        for _ in range(num):
            letter += letters[0]
    return letter


def dec_to_roman(num, tier=0):
    def possible_letters():
        if tier == 3:
            return ['M']
        dic = dict(DICT_OF_NUMERALS)
        vals = iter(dic.keys())
        for _ in range(2*tier):
            next(vals)
        return [next(vals) for _ in range(3)]
    if num // 10 == 0:
        return single_to_roman(num, possible_letters())
    digit = num % 10
    return dec_to_roman(num // 10, tier + 1) + single_to_roman(digit, possible_letters())


def check_roman(num):
    dic = dict(DICT_OF_NUMERALS)
    if not all((c in dic.keys() for c in num)):
        return False
    count = 1
    for i in range(len(num) - 1):
        j = i + 1
        if num[i] == num[j]:
            if num[i] in ['V', 'L', 'D'] or count == 3:  # addition checks
                return False
            count += 1
        else:
            count = 1
        if dic[num[i]] < dic[num[j]]:  # subtraction checks
            if not dic[num[j]] // dic[num[i]] in [5, 10] or (len(num[i:]) > 2 and dic[num[j+1]] in [dic[num[i]], 5*dic[num[i]], 10*dic[num[i]]]):
                return False
    return True


def check_int(num):
    if not (0 < num < 4000):
        print('Error! Number exceeds range of Roman Numerals!\nTry a different number!')
        return False
    return True


def is_int(s):
    return all([(c in map(str, range(10))) for c in s])


def main():
    intro = 'Welcome to Ryan\'s Roman numeral converter!\n Enter the number you wish to convert in the prompt below.\n'
    print(intro)
    while True:
        print('Enter a decimal integer or a Roman Numeral (Type \"exit\", \"q\", or \"quit\" to exit)')
        number = input('>>')
        if number in ['exit', 'q', 'quit']:
            break
        if is_int(number) and check_int(int(number)):
            print(dec_to_roman(int(number)))
        elif check_roman(number.upper()):
            print(roman_to_dec(number.upper()))
        else:
            print('Error: Not a Valid Roman Numeral.')
    return


main()
