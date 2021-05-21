import random

def generate_numbers(a):
    numbers = []

    while len(numbers) < a:
        number = random.randrange(46)
        if number not in numbers:
            numbers.append(number)

    return numbers


def draw_winning_numbers():
    #개복잡하게 했구만
    #a = generate_numbers(7)
    #a = sorted(a[:6]) + a[6:] 슬라이싱해야 더하기가 되는군 그래야 리스트로 나오니까
    #print(generate_numbers(5).sort()) sort()는 결과값으로 아무것도 안반환해 그냥 변환해주는 함수니까!
    winning_numbers = sorted(generate_numbers(6))

    while len(winning_numbers) < 7:
        add = random.randrange(46)
        
        if add not in winning_numbers:
            winning_numbers.append(add)

    return winning_numbers


def count_matching_numbers(list_1, list_2):
    count = 0

    for i in list_1:
        if i in list_2:
            count += 1

    return count


def check(numbers, winning_numbers):
    count = len( set(numbers).intersection(set(winning_numbers[:6])))
    if count == 6:
        return 100000000
    elif count == 5 and winning_numbers[6] in numbers:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000


print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
