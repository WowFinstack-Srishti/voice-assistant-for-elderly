def soundex(word):
    word = word.upper()
    codes = {'BFPV': '1', 'CGJKQSXZ': '2', 'DT': '3', 'L': '4', 'MN': '5', 'R': '6'}
    result = word[0]
    for char in word[1:]:
        for key in codes:
            if char in key:
                code = codes[key]
                if result[-1]!= code:
                    result += code
    result = result.ljust(4, '0')
    return result[:4]

def match_command(input_word, commands):
    input_code = soundex(input_word)
    for cmd in commands:
        if soundex(cmd) == input_code:
            return cmd
    return None