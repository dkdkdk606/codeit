#폴더만들고 __init__.py 만들기
#패키지 완성
#import shape.volume
#       패키지.모듈
#당연하지않지만 import shape 는 안됨
#                     패키지
# 이거 쓰려면 __init__.py 써야함 담강의 ㄱㄱ

# utils 모듈의 'read_image' 함수와 'display' 함수를 임포트해 주세요
# 코드를 작성해 주세요 ###
#import cil.units 도 가능
#from cil.utils import read_image
#from cil.utils import display ㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴ
#from cil.utils import read_image, display

# processing 모듈의 'invert' 함수를 'inv'로 임포트하고 'merge' 함수를 'mrg'로 임포트해 주세요
# 코드를 작성해 주세요 ###
#from cil.processing import invert as inv
#from cil.processing import merge as mrg 


def merge(img1, img2):
    # img1과 img2의 크기가 같은지 확인
    if len(img1[0]) == len(img2[0]) and len(img1) == len(img2):
        new_img = []
        for i in range(len(img1)):
            new_img.append([])
            for j in range(len(img1[0])):
                new_img[i].append(max(img1[i][j], img2[i][j]))
                
        return new_img
#이건 왜 또 시키는거지 그냥 복습인가






