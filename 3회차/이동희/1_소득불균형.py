import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #각 개인의 income 리스트에 추가
    income = list(map(int, input().split()))
    # 리스트의 평균
    avg = sum(income) / N
    count = 0
    # income리스트에서 평균보다 값이 큰 사람이 있을 때마다 count += 1
    for ppl in income:
        if ppl <= avg:
            count += 1
    
    print(f'#{tc} {count}')