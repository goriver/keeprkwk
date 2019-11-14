# birth = input("생년월일 6자리를 입력해주세요.(yymmdd) : " )
# print("당신의 생일은 "+birth[0:2]+'년'+birth[2:4]+"월"+birth[4:]+"일")


birth = input("생년월일 6자리로 입력해주세요(yymmdd) : ")
print("당신의 생일은",birth[:2], '년',birth[2:4],"월",birth[4:], "일 입니다.")