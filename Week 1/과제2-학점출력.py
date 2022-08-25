score=int(input("점수를 입력하세요: "))

if score>=90:
    print("A 학점입니다.")
elif score<90 and score>=80:
    print("B학점입니다.")
elif score<80 and score>=70:
    print("C 학점입니다.")
elif score>=60 and score<70:
    print("D 학점입니다.")
else:
    print("F 학점입니다.")
    

