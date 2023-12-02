import hashlib
import re


def check(password, user):
    numCount = 0
    upperCount = 0
    lowerCount = 0
    specialCount = 0
    for c in password:

        if c.isnumeric():
            numCount += 1
        elif c.isupper():
            upperCount += 1
        elif c.islower():
            lowerCount += 1
        elif c == '!' or c == '@' or c == '#' or c == '$' or c == '%' or c == '%' or c == '?' or c == '*':
            specialCount += 1

    # Reject if it doesn't contain at least one of each of the following:
    if numCount < 1:
        print("Password must contain at least 1 numbers")
        return False
    elif upperCount < 1:
        print("Password must contain at least 1 uppercase letters")
        return False
    elif lowerCount < 1:
        print("Password must contain at least 1 lowercase letters")
        return False
    elif specialCount < 1:
        print("Password must contain at least 1 special characters")
        return False
    elif 8 > len(password) or len(password) > 12:
        print("Password must be at least 8-12 characters long")
        return False
    elif user.getName() in password:
        print("Password cannot be your name")
        return False

    # Reject if contains calender date
    if re.match(r'\d{1,2}/\d{1,2}/\d{2,4}', password):
        print("Your password cannot be a date")
        return False

    # Reject if it resembles a license plate (e.g., ABC123)
    if re.match(r'[A-Za-z]{3}\d{3}', password):
        print("Your password cannot be a license plate")
        return False

    # Reject if it's too phone-number-ish (e.g., (555) 123-4567)
    if re.match(r'\(\d{3}\) \d{3}-\d{4}', password):
        print("Your password cannot be a phone number")
        return False

    if password.lower() in open("commonPasswords.txt").read():
        print("Your password is too common")
        return False

    # It's all good if it passed the checks!
    return True


def correctPassword(user, password):
    f = open("passwords.txt", "r")
    for line in f:
        if user.getUserID() in line.split(';')[0]:
            user = hashlib.sha3_256((password + line.split(';')[1]).encode()).hexdigest().strip()
            has = line.split(';')[2].strip()
            if user == has:
                print("Password accepted")
                return True
            else:
                return False
    f.close()
    return False
