def validate(password):
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

    if not contains_upper or not contains_lower:
        errors.append(4)

    if not contains_control:
        errors.append(5)

    for key, value in char_counts.items():
        if value > 4:
            errors.append(3)
            break

    return errors
