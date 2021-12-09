def is_palindrome(word):
    # 코드를 입력하세요.
    for i in range(len(word) // 2):
        if word[i] == word[-1-i]:
            continue
        # ㅋㅋ word[i] != word[-1-i]: return false == 쓰는걸 잘 몬하네 아직
        else:
            return False
    return True
#return 이 함수 끝낼수 있는거 생각점 ;;


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))