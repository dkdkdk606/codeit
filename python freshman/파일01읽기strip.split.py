with open('data/ddd.txt', 'r', encoding='UTF8') as f:
    print(type(f))
    for line in f:
        print(line.strip())

#split 엑셀 문자열나누기랑 똑같네
my_string = "1, 2, 3, 4, 5, 6"
print(my_string.split(", "))

print("\n ssibal \n seki \n\tㅋㅋㅋㅋ ㅈ밥\n 후 그래도 공부 하네".split())
#항상 str인것 잊지 말자