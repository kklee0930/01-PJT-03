import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dict = {}
    # 학생 1000명의 점수 입력받아서 리스트로 변환
    scores = list(map(int,input().split()))
    # 딕셔너리에 해당 점수가 존재하지 않으면 value값 1로 설정, 존재하면 value += 1
    for i in scores:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    # value가 점수 리스트에서의 빈도이므로 max(빈도)는 최빈값이다.
    max_val = max(dict.values())
    lst = []
    # 딕셔너리의 key, value에서 value == 최빈값이면 리스트에 append
    for k,v in dict.items():
        if v == max_val:
            lst.append(k)
    # 리스트 reverse sort
    lst.sort(reverse=True)
    
    # 가장 큰 값 출력
    print(f'#{tc} {lst[0]}')