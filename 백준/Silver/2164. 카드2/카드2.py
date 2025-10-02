import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

# 1부터 n까지의 숫자를 담은 deque를 생성
cards = deque(range(1, n + 1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])