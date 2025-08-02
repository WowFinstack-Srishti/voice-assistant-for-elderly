def soundex(word):
    word = word.upper()
    codes = {'BFPV': '1', 'CGJKQSXZ': '2', 'DT': '3', 'L': '4', 'MN': '5', 'R': '6'}
    soundex_code = word[0]
    for char in word[1:]:
        for key in codes:
            if char in key:
                code = codes[key]
                if code != soundex_code[-1]:
                    soundex_code += code
    soundex_code = soundex_code.ljust(4, '0')
    return soundex_code[:4]

def match_command(input_word, commands):
    input_code = soundex(input_word)
    for cmd in commands:
        if soundex(cmd) == input_code:
            return cmd
    return None