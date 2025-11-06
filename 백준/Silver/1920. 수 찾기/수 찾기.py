# 데이터 개수
N = int(input())
# 수 데이터 리스트 저장
A = list(map(int, input().split()))
# 리스트 정렬
A.sort()
# 탐색할 숫자 개수 저장
M = int(input())
# 탐색할 수 데이터 리스트 저장
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]
    # 이진 탐색 시작
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = int((start + end) / 2)
        midv = A[mid]
        if midv > target:
            end = mid - 1
        elif midv < target:
            start = mid + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)