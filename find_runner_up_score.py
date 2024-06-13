# Find The Runner-up Score
# Developer: Youssef Tarek
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up = list(set(arr))
    runner_up.sort()
    print(runner_up[-2])