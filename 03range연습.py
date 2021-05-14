numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

#인덱스와 원소 출력
# for i in numbers:
#     print(f"{numbers.index(i)} {i}")
#range를 어디다가 사용하지?

for i in range(len(numbers)):
    print(f"{i} {numbers[i]}")
