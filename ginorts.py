# Sorting - Ginorts
# Developer: Youssef Tarek
# Link: https://www.hackerrank.com/challenges/ginorts/problem

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
numbers = [10, 30, 2, 7]
# smallest_number = numbers[0]
def get_smallest(numbers):
    smallest_number = numbers[0]

    for number in numbers:
        if number < smallest_number:
            smallest_number = number
        
    return smallest_number
print(get_smallest(numbers))
