def mask_security_number(security_number):
    # 코드를 입력하세요.
    temp = []
    for i in security_number:
        temp.append(i)
    #temp = list(secruity_number)

    for i in range(-4, 0):
        temp[i] = "*"
    
    security_number_masked = "".join(temp)
    #security_number_masked = ""
    #for i in temp:
    #    security_number_masked += i

    return security_number_masked    



#    security_number = str(security_number[0:-4]) + "****"
#    return security_number


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

#문제에서 문자열만 넣어주니까 궂이 str()이 필요없지
def p(a):
    a = a[:1] + "3"
    print(a)
#a = 3
#a = 3 + "3"
p("사람")