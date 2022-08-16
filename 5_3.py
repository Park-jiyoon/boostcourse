import random


# 최소,중간,최대값 함수
def max_min(com, num):
    if com[0] == num:
        return '최솟값'
    elif com[1] == num:
        return '중간값'
    elif com[2] == num:
        return '최댓값'

def guess_number():
    i = 0
    count = [0, 0, 0]
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    num3 = random.randint(0, 100)
    num = list()
    num.append(num1)
    num.append(num2)
    num.append(num3)
    num.sort()
    print(num)
    num_list = list()
    while True:
        print(i + 1, "차 시도")
        n = int(input("숫자를 예측보세요: "))
        for j in num:
            # print('j는',j)
            if n == j:
                print("숫자를 맞추셨습니다!", n, '는', max_min(num, n))
                if max_min(num, n) == '최솟값':
                    count[0] = 1
                elif max_min(num, n) == '중간값':
                    count[1] = 1
                elif max_min(num, n) == '최댓값':
                    count[2] = 1
            # count 원소가 모두 1이면 게임 종료
            if count == [1, 1, 1]:
                print('게임종료')
                break
            # 입력한 숫자가 요소인 리스트에 있으면 중복
            if n in num_list and i > 0:
                print('이미 예측에 사용한 숫자입니다.')
                break
            #5, 10 에서 힌트
            if i + 1 == 5 or i + 1 == 10:
                print(n, '은 없습니다.')
                if n < num[0]:
                    print(n, '은 최솟값 보다 작습니다.')
                elif n > num[2]:
                    print(n, '은 최댓값 보다 큽니다.')
                break
        num_list.append(n)

        if count == [1, 1, 1]:
            print(i + 1, '번 시도만에 예측 성공')
            break
        i = i + 1


guess_number()
