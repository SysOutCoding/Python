import itertools
import time


# Brute force function
def tryPassword(passwordSet, stringTypeSet):
    start = time.time()
    chars = stringTypeSet
    attempts = 0
    for i in range(1, 7):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            # print(attempts)
            print(letter)
            if letter == passwordSet:
                end = time.time()
                distance = end - start
                return (attempts, distance)


password = input("Enter password: ")

stringType = "1234567890abcdefghijklmnopqrstuvwxyzäöüABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"
tries, timeAmount = tryPassword(password, stringType)
print("Cracked the password %s in %s tries and %s seconds!" % (password, tries, timeAmount))