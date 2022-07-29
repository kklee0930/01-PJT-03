import sys

sys.stdin = open("_암호문1.txt")

for tc in range(1, 11):
    # 원본 암호문 길이
    N = int(input())
    # 원본 암호문 split으로 list 생성
    orig_code = input().split()
    # print(f'orig_code: {orig_code}')
    
    # 명령어의 갯수
    cmd_count = int(input())
    # 명령어에서 I를 기점으로 리스트로 나누고 cmd[0] == ''이므로 인덱스 1부터 끝까지를 cmd로 정의한다.
    cmd = input().split('I')[1:]
    for i in cmd:
        # I를 기점으로 나뉜 문자열을 split해서 공백을 기준으로 개별적인 원소로 이루어진 리스트를 생성.
        split_lst = i.split()
        # print(f'split_lst: {split_lst}')
        
        # split_lst[0]이 삽입할 위치, split_lst[1]이 삽입할 갯수, split_lst[2::]가 덧붙일 숫자들이다.
        orig_code[int(split_lst[0]):int(split_lst[0])] = split_lst[2::]
        
    # 수정된 결과의 처음 10개 숫자만 출력
    print(f"#{tc} {' '.join(orig_code[:10])}")
    