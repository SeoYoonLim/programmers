import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
# 입력값을 map 객체(이터레이터)로 받아 바로 사용합니다.
A_stream = map(int, input().split())

# 덱(deque)에는 (값, 인덱스)를 저장합니다.
mydeque = deque()

# enumerate를 사용하여 인덱스와 값을 함께 순회합니다.
for i, num in enumerate(A_stream):
    # 1. 덱의 맨 앞 요소가 현재 윈도우(i-L+1 ~ i) 범위를 벗어났는지 확인하고, 벗어났다면 제거합니다.
    # mydeque가 비어있지 않은지 먼저 확인해야 합니다.
    if mydeque and mydeque[0][1] < i - L + 1:
        mydeque.popleft()

    # 2. 덱의 맨 뒤에서부터 현재 들어올 값(num)보다 큰 값들을 모두 제거합니다.
    # 이렇게 하면 덱은 항상 오름차순을 유지하게 됩니다.
    while mydeque and mydeque[-1][0] > num:
        mydeque.pop()

    # 3. 현재 값과 인덱스를 덱에 추가합니다.
    mydeque.append((num, i))

    # 4. 덱의 맨 앞 요소가 현재 윈도우의 최솟값이므로 출력합니다.
    # sys.stdout.write가 print보다 빠릅니다.
    sys.stdout.write(str(mydeque[0][0]) + " ")