#dick = {}
#dick[1] = 2
#dick[2] = 4
#print(dick)

#for i in dick.items():
#    print(i)
#    print(type(i))

#a, b = i
#print(b, a)


# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
#def reverse_dict(dict):
#    new_dict = {}  # 새로운 사전
    
    # dict의 key와 value를 뒤집어서 new_dict에 저장
    # 코드를 입력하세요.
#    for en, kr in dict.items():
#        new_dict[kr] = en

#    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
#vocab = {
#    'sanitizer': '살균제',
##    'ambition': '야망',
#    'conscience': '양심',
#    'civilization': '문명',
#    'privilege': '특권',
#    'principles': '원칙'
#}

# 기존 단어장 출력
#print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
#reversed_vocab = reverse_dict(vocab)
#print("한-영 단어장\n{}".format(reversed_vocab))

dickdick = ['람사', '람사', '람사', '람사', '람사', '사람']
dick = {
    '사람': 1,
    '람사': 1,
    '동물': 1,
    '식물': 1
}
print(dick['사람'] + 1)
print('람사' in dick.keys())
print(('람사' in dick.keys() )== True)


