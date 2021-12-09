# a + b + c = 1000인 피타고라스 수의 abc 찾기(a<b<c)
for a in range(1, 1000):
    for b in range(a+1, 500):
        for c in range(b+1, a+b):
        # c = 1000 - a - b 하면 되네...
            if a + b + c == 1000:
                if a*a + b*b == c*c:
                    print(a * b * c) 