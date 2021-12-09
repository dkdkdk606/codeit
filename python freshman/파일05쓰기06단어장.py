#with open('new_file.txt', 'w') as f: #'a' 는 append 추가 만약 해당 파일이 없으면 만들고 있으면 추가
    #f.write("hellow world\n")
    #f.wirte("My name is byeongchan."
with open('vocavulary.txt', 'a', encoding='UTF8') as f:
    en = ""

    while True:
        en = input("영어 단어를 입력하세요: ")
        if en == "q":
            break
        f.write(f"{en}: ")
        
        kr = input("한국어 뜻을 입력하세요: ")
        if kr == "q":
            break
        f.write(f"{kr}\n")
