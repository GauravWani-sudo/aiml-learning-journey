class InvalidAgeError(Exception):
    pass

age = -1

try:
    if age < 0:
        raise InvalidAgeError("invalid age")

    print(age)

except InvalidAgeError as e:
    print(e)