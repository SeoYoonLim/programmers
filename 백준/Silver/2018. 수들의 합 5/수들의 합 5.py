import sys
input=sys.stdin.readline

N= int(input())

count = 0
start = 1
end = 1
sum_val = 1

while start <= N:
    if sum_val == N:
        count += 1
        end += 1
        sum_val += end
    elif sum_val < N:
        end += 1
        sum_val += end
    else:
        sum_val -= start
        start += 1
print(count)