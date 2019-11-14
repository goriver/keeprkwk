print("일반계산기 프로그램입니다!")
print()
a = int(input("계산할 첫번째 값을 입력해주세요 : " ))
b = int(input("계산할 두번째 값을 입력해주세요 : " ))
# input 하고 바로 형변환 진행해도 됨!

# sum = a+b
# minu = a-b
# multi =  a*b

print("두개의 값"+str(a)+"와"+str(b))
print()
print("더하기 값(a+b) : " ,(a+b) )
print("빼기 값 (a-b) : ",(a-b))
print("곱하기 값 ( a * b) : ",(a*b))
print("정수 나누기 값 ( a//b) : ",(a//b))
print("실수 나누기 값 ( a/b) : ",(a/b))
print("나머지 값 ( a % b) : ",(a%b))

# 인강에 배웠던 내용을 활용