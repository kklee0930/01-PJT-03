import sys

sys.stdin = open("_신용카드만들기1.txt")

for tc in range(1, int(input())+1):
    card = input().split()
    lst = list(map(int, card))
    # print(lst)
    odd = 0
    even = 0
    
    # range 0 ~ 15
    for i in range(len(lst)):
        # 홀수일 경우에 짝수이다.
        if i == 0:
            odd += 2*lst[i]
        # 짝수일 경우
        elif i % 2 != 0:
            even += lst[i]
        #홀수인 경우에는
        elif i % 2 == 0:
            # 마찬가지로 even 변수에 더해준다.
            odd += (2*lst[i])
    else:
        if (odd + even) % 10 == 0:
            print(f'#{tc} 0')
        else:
            print(f'#{tc} {10 - ((odd + even) % 10 )}')