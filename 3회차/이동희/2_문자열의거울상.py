import sys

sys.stdin = open("_문자열의거울상.txt")

for tc in range(1, int(input())+1):
    str_ = ''
    num = input()
    # 입력 문자열 거꾸로 변환
    num = num[::-1]
    # print(num)
    
    # 문자열을 for문으로 순회하면서 bdpq문자열이 있을 때마다 반대되는 문자열을 str에 추가
    for i in num:
        if i == 'b':
            str_ = str_+'d'
        elif i == 'd':
            str_ = str_+'b'
        elif i == 'p':
            str_ = str_+'q'
        elif i == 'q':
            str_ = str_+'p'
    print(f'#{tc} {str_}')
