import sys
input = sys.stdin.readline

n=int(input())
arr = []
for i in range(n):
    # (값, 원래 인덱스)를 튜플로 묶어 리스트에 추가합니다.
    arr.append((int(input()), i))
    
# 값을 기준으로 리스트를 정렬합니다.
sorted_arr = sorted(arr)
max_diff = 0

for i in range(n):
    # (원래 인덱스 - 정렬 후 인덱스)가 가장 큰 값을 찾습니다.
    # 이 값이 바로 해당 원소가 왼쪽으로 이동한 칸의 수가 됩니다.
    diff = sorted_arr[i][1] - i
    if max_diff < diff:
        max_diff = diff

# 버블 소트가 한 번도 swap을 하지 않고 종료되는 루프를 고려하여 1을 더해줍니다.
print(max_diff + 1)