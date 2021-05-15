numbers = [2, 3, 5, 7, 11, 13, 17, 19]
#in_numbers = []
# 리스트 뒤집기
#for i in numbers:
#    in_numbers.insert(0,i)
#numbers = in_numbers
# 코드를 입력하세요.


for i in range(len(numbers) // 2):
    numbers[i], numbers[-1 - i] = numbers[-1 - i], numbers[i]



print("뒤집어진 리스트: " + str(numbers))