# 자리수 합 리턴
def sum_digit(num):
    # 코드를 입력하세요.
    total = 0
    for i in str(num):
        total += int(i) 
    
    return(total)


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
sum_totla = 0
for i in range(1001):
    sum_totla += sum_digit(i)

print(sum_totla)