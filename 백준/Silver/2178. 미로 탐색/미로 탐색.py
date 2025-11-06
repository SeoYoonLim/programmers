import sys
from collections import deque

# 입력을 빠르게 받기 위함
input = sys.stdin.readline

# 상하좌우를 탐색하기 위한 방향 벡터
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
# 미로 정보를 저장할 2차원 리스트
A = []
for _ in range(N):
    # 입력받은 문자열을 정수 리스트로 변환하여 추가
    A.append(list(map(int, list(input().strip()))))

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    
    # 큐가 빌 때까지 반복
    while queue:
        now = queue.popleft()
        # 현재 위치에서 상하좌우 탐색
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            
            # 미로 범위를 벗어나지 않는지 확인
            if 0 <= x < N and 0 <= y < M:
                # 갈 수 있는 길(1)이고, 아직 방문하지 않은 곳인지 확인
                if A[x][y] == 1:
                    # 이전 칸의 값에 1을 더해 거리를 기록 (이것이 방문 체크 역할도 함)
                    A[x][y] = A[now[0]][now[1]] + 1
                    queue.append((x, y))

# (0, 0) 위치에서 BFS 탐색 시작
BFS(0, 0)

# 도착 지점 (N-1, M-1)에 기록된 최단 거리를 출력
print(A[N-1][M-1])
