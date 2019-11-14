print("BMI 계산기 입니다")

height = input("신장: ")
weight = input("몸무게:")
bmi = (float(weight)/(float(height)*float(height)))*10000

print("BMI : "+str(bmi))