with open('data/chicken.txt', 'r', encoding='UTF8') as data:
    
    day = 0
    cash_sum = 0
    
    #print(data)

    for line in data:
        day = int(line.split("일: ")[0])
        cash_sum += int(line.split("일: ")[1])
        
        #if j <= 31:
        #    day = j
        #else:
        #    cash += j

    print(cash_sum/day)

