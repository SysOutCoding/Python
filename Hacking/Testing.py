numbers = [1, 3, 6, 9, 1] # max. 5 numbers
sorted_numbers = sorted(numbers)
print("Sorted numbers:")
print(sorted_numbers)
if sorted_numbers[0] == sorted_numbers[1]:
    print(sorted_numbers[0])
elif sorted_numbers[0] == sorted_numbers[2]:
    print(sorted_numbers[0])
elif sorted_numbers[0] == sorted_numbers[3]:
    print(sorted_numbers[0])
elif sorted_numbers[0] == sorted_numbers[4]:
    print(sorted_numbers[0])
elif sorted_numbers[1] == sorted_numbers[2]:
    print(sorted_numbers[1])
elif sorted_numbers[1] == sorted_numbers[3]:
    print(sorted_numbers[1])
elif sorted_numbers[1] == sorted_numbers[4]:
    print(sorted_numbers[1])
elif sorted_numbers[2] == sorted_numbers[3]:
    print(sorted_numbers[2])
elif sorted_numbers[2] == sorted_numbers[4]:
    print(sorted_numbers[2])
elif sorted_numbers[3] == sorted_numbers[4]:
    print(sorted_numbers[3])
else:
    print("No doubled number!")