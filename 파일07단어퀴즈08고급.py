import random
with open('vocavulary.txt', 'r', encoding = 'UTF8') as f:
    #파일 불러와서 영어랑 한글 나누기
    # for line in f:
        #그줄 앞은 영어 뒤는 한글
       # en = (line.strip()).split(": ")[0]
       # kr = (line.strip()).split(": ")[1]
        
       # answer = input(f"{kr}: ")

       
       # if answer == en:
       #     print("맞았습니다!\n")
       # else:
       #     print(f"아쉽습니다. 정답은 {en}입니다.\n")
    voca_dic = []
    
    for line in f:
        #단어분리, 단어장에 추가
        en = line.strip().split(": ")[0]
        kr = line.strip().split(": ")[1]
        voca_dic.append([en, kr])
    
    while True:
        i = random.randrange(len(voca_dic))
        answer = input(f"{voca_dic[i][1]}: ")
        
        if answer == "q":
            break

        if answer == voca_dic[i][0]:
            print("맞았습니다!\n")
        else:
            print(f"틀렸습니다. 정답은 {voca_dic[i][0]}입니다.\n")

