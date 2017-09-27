#! python3

import re

checkLong = re.compile(r'[a-zA-Z0-9]{8,}')

checkUpperCase = re.compile(r'[A-Z]')
checkLowerCase = re.compile(r'[a-z]')
checkNumber    = re.compile(r'\d')

checkUpperLowerAndNumber = a = re.compile(r'''(
    [A-Z][a-z]+\d+ |
    [A-Z]\d+[a-z]+ |
    \d[a-z]+[A-Z]+ |
    \d[A-Z]+[a-z]+ |
    [a-z]\d+[A-Z]+ |
    [a-z][A-Z]+\d+
    )''', re.VERBOSE)

passwords = []

goodPass1 = "brunoA1meid4"
goodPass2 = "2runoA1meid4"
goodPass3 = "Bruno4lmeida"
goodPass4 = "8rB"

badPass1 = "brunoAxmeida"
badPass2 = "brunoaxmeida"
badPass3 = "BRUNO4444444"
badPass4 = "134"

passwords.append(goodPass1)
passwords.append(goodPass2)
passwords.append(goodPass3)
passwords.append(goodPass4)
passwords.append(badPass1)
passwords.append(badPass2)
passwords.append(badPass3)
passwords.append(badPass4)

for password in passwords:
    print("PASSWORD => " + password)

    checkLongObj = checkLong.search(password)
    print("SUCCESS it is more than 8 chars") if checkLongObj else print("ERROR less than 8 chars")

    checkUpperObj = checkUpperCase.search(password)
    print("SUCCESS it contains at least 1 uppercase") if checkUpperObj else print("ERROR it does not contains an uppercase")

    checkLowerObj = checkLowerCase.search(password)
    print("SUCCESS it contains at least 1 lowercase") if checkLowerObj else print("ERROR it does not contains an lowercase")

    checkNumberObj = checkNumber.search(password)
    print("SUCCESS it contains at least 1 number") if checkNumberObj else print("ERROR it does not contains an number")

    checkObj = checkUpperLowerAndNumber.search(password)
    print("SUCCESS incorrect format") if checkObj else print("ERROR incorrect format")

    print("####################")



