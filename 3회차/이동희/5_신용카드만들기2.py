import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for tc in range(1, T+1):
    card = input()
    
    #입력값의 첫번째 값이 3,4,5,6,9 조건에 적합한지 확인
    if card[0] in ['3','4','5','6','9']:
        #적합하다면 -문자를 모두 제거하고 길이가 16인지 확인 후에 맞다면 1 출력 아니면 0 출력
        card_modified = card.replace('-', '')
        
        if len(card_modified) == 16:
            print(f'#{tc} 1')
            
        else:
            print(f'#{tc} 0')
    else:
        print(f'#{tc} 0')
