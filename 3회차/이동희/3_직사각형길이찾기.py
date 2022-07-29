import sys

sys.stdin = open("_직사각형길이찾기.txt")

from collections import Counter

T = int(input())
for tc in range(1, T+1):
    # length에 입력값 추가
    length = map(int, input().split())
    # counter함수 사용해서 각 길이의 횟수 딕셔너리로 반환
    length = Counter(length)
    
    for k,v in length.items():
    # 사각형이므로 가로 == 가로, 세로 == 세로 이므로 value가 1인 key를 출력
        if v == 1:
            print(f'#{tc} {k}')
    # v == 3인 경우에는 정사각형이라는 뜻이므로 모든 변의 길이가 같으므로 key 출력
        elif v == 3:
            print(f'#{tc} {k}')