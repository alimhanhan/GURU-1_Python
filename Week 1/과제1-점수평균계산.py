name= str(input("이름: "))
num=int(input("학번: "))
lan=int(input("국어 점수: "))
math=int(input("수학 점수: "))
eng=int(input("영어 점수: "))
sum=(lan+math+eng)/3

print("\n이름: %s" %name)
print("학번: %d" %num)
print("국어 점수: %d" %lan)
print("수학 점수: %d" %math)
print("영어 점수: %d" %eng)
print("평균 점수: %d" %sum)
