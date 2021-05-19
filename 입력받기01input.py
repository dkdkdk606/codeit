#su = input("망나니망나니 망 망 나니 나니: ")
#if su == "망나니 일":
#    print("올 좀 놀줄 아는데?")
#else:
#    print("떙!")
import random

# 코드를 작성하세요.
answer = 3 #random.randint(1, 20)
for i in [4, 3, 2, 1, 0]:
    if i != 0:
        user_ans = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
        if answer == user_ans:
            print(f"축하합니다. {5 - i}번만에 숫자를 맞히셨습니다.")
            break
        else:
            if answer > user_ans:
                print("up")
            else:
                print("down")
    else:
        print(f"아쉽습니다. 정답은 {answer}입니다.")

#논리 흐름대로 하지 않고 결과를 내기위해 순서 섞는게 좀 그렇긴 하네



    
        
    
    
    