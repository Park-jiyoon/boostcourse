def grader(score):
    if 95 <= score <= 100:
        return 'A+'
    elif 90 <= score <= 94:
        return 'A'
    elif 85 <= score <= 89:
        return 'B+'
    elif 80 <= score <= 84:
        return 'B'
    elif 75 <= score <= 79:
        return 'C+'
    elif 70 <= score <= 74:
        return 'C'
    elif 65 <= score <= 69:
        return 'D+'
    elif 60 <= score <= 64:
        return 'D'
    elif score < 60:
        return 'F'

name = input("이름을 입력해주세요. : ")

score = input("점수를 입력해주세요.(0~100사이) : ")


print("학생 이름: ", name)
print("점수 : ", score)
print("학점 : ", grader(int(score)))