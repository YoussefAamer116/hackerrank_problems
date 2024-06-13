# List Comprehensions
# Developer: Youssef Tarek
# Link: https://www.hackerrank.com/challenges/list-comprehensions/problem

# list = [expression  for item in iterable  if condition(optionaly)] 

# squares_of_evens = [num**2 for num in range(1,11) if num % 2 == 0]

# print(squares_of_evens)

# evens_and_odds = ['Even' if num % 2 == 0 else 'Odd' for num in range(1, 11)]
# print(evens_and_odds)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i + j + k !=n]
    print(result)
