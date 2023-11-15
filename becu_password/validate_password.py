def validate(password):
    errors = []

    if len(password) < 16:
        errors.append(1)

    if "password" in password.lower():
        errors.append(2)

    char_counts = {}
    contains_upper = False
    contains_lower = False
    contains_control = False
    for ch in password:
        char_counts[ch] = char_counts.get(ch, 0) + 1
        contains_upper |= ch.isupper()
        contains_lower |= ch.islower()
        contains_control |= ch in "*#@"

    if any(count > 4 for count in char_counts.values()):
        errors.append(3)

    if not contains_upper or not contains_lower:
        errors.append(4)

    if not contains_control:
        errors.append(5)

    return sorted(errors)


def validate_orig(password):
    errors = []

    if len(password) < 16:
        errors.append(1)

    password_lc = password.lower()
    password_len = len("password")
    for i in range(len(password) - password_len + 1):
        sub_password = password_lc[i:i + password_len]
        if (sub_password == "password"):
            errors.append(2)
            break

    char_counts = {}
    contains_upper = False
    contains_lower = False
    contains_control = False
    for i in range(len(password)):
        if password[i] in char_counts:
            char_counts[password[i]] += 1
        else:
            char_counts[password[i]] = 1
        if password[i].isupper():
            contains_upper = True
        if password[i].islower():
            contains_lower = True
        if password[i] == '*' or password[i] == '#' or password[i] == "@":
            contains_control = True

    for key, value in char_counts.items():
        print(key, value)
        if value > 4:
            errors.append(3)
            break

    if not contains_upper or not contains_lower:
        errors.append(4)

    if not contains_control:
        errors.append(5)

    return sorted(errors)


"""
You are working on an authentication system and there is a set of rules the users have to follow when picking a new password:

1. It has to be at least 16 characters long.
2. The password cannot contain the word "password". This rule is not case-sensitive.
3. The same character cannot be used more than 4 times. This rule is case-sensitive, "a" and "A" are different characters.
4. The password has to contain at least one uppercase and one lowercase letter.
5. The password has to contain at least one of the following special characters "*", "#", "@".

Write a function that takes in a password and returns a collection of any rule numbers that are not met.

password_1 = "Strongpwd9999#abc"      ==> []
password_2 = "Less10#"                ==> [1]
password_3 = "Password@"              ==> [1,2]
password_4 = "#PassWord01111111222223x" ==> [2,3]
password_5 = "password#1111111"        ==> [2,3,4]
password_6 = "aaaapassword$$"         ==> [1,2,3,4,5]
password_7 = "LESS10#"                ==> [1,4]
password_8 = "SsSSSt#passWord"        ==> [1,2]
password_9 = "SsSSSt#passWordpassword" ==> [2,3]

All test cases:

validate(password_1) ==> []
validate(password_2) ==> [1]
validate(password_3) ==> [1,2]
validate(password_4) ==> [2,3]
validate(password_5) ==> [2,3,4]
validate(password_6) ==> [1,2,3,4,5]
validate(password_7) ==> [1,4]
validate(password_8) ==> [1,2]
validate(password_9) ==> [2,3]

Complexity variables:

N = length of the password
"""
