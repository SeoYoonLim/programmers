import sys
input=sys.stdin.readline
N = int(input())

# 숫자 리스트를 입력받아 정렬합니다.
numbers = sorted(list(map(int, input().split())))

good_count = 0

# 각 숫자가 '좋은 수'인지 확인합니다.
for k in range(N):
    target = numbers[k]
    # target을 제외한 나머지 부분에서 투 포인터를 사용합니다.
    start = 0
    end = N - 1
    
    while start < end:
        current_sum = numbers[start] + numbers[end]
        
        if current_sum == target:
            # 합이 target과 같을 때, 두 포인터가 target의 인덱스와 다른지 확인합니다.
            # 자기 자신을 사용해서는 안 됩니다.
            if start != k and end != k:
                good_count += 1
                break # 좋은 수를 찾았으므로 현재 target에 대한 탐색 종료
            elif start == k:
                start += 1 # start 포인터가 target이므로 오른쪽으로 이동
            elif end == k:
                end -= 1 # end 포인터가 target이므로 왼쪽으로 이동
        elif current_sum < target:
            start += 1 # 합이 작으므로 start를 오른쪽으로 이동
        else: # current_sum > target
            end -= 1 # 합이 크므로 end를 왼쪽으로 이동

print(good_count)