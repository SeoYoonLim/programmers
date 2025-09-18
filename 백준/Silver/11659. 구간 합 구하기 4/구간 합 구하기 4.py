import sys
input=sys.stdin.readline
N,M=map(int,input().split())
num=list(map(int,input().split()))
psum=[0]
temp=0
for i in num:
    temp=temp+i
    psum.append(temp)
for i in range(M):
    s,e = map(int, input().split())
    print(psum[e] -psum[s-1])