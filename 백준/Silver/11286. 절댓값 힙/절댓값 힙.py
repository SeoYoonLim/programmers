import sys,heapq

# 힙으로 사용할 빈 리스트를 선언합니다.
heap = []

N = int(sys.stdin.readline())
for i in range(N):
    a = int(sys.stdin.readline())
    if a != 0:
        # (절댓값, 원본값) 튜플 형태로 힙에 추가합니다.
        heapq.heappush(heap, (abs(a), a))
    else:
        # 힙이 비어있으면 0을 출력합니다.
        if not heap:
            print(0)
        else:
            # 힙에서 가장 작은 튜플을 꺼내고, 그 튜플의 두 번째 원소(원본값)를 출력합니다.
            print(heapq.heappop(heap)[1])