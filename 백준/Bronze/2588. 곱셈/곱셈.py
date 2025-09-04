#입력받은 것을 int형으로 변환
a = int(input())
#숫자는 슬라이싱이 안되므로 그냥 문자로 입력 받음
b = input()
#변수b 자릿수만큼 곱하기
for i in range(int(len(b))):
    #b의 뒤에서부터 하나식 슬라이싱 후 int로 바꿔서 a와 계산 출력
    print(a * int(b[-(i+1)]))
#곱셈의 결과를 출력    
print(a * int(b))
