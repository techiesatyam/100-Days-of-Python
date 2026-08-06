def john():
    plate = input("Plate: ")
    if print_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def print_valid(s):

    # Check the length of the string
    if len(s) <= 2 or len(s) >= 6:
        return False
    # Checking the first two character are letters
    elif not s[0].isalpha() or not s[1].isalpha():
        return False
    # Only letters and numbers are allowed
    elif not s.isalnum():
        return False
    # After alphabet the characters must be numbers
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            break
    return True

john()