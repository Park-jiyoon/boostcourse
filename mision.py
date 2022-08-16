import random

#컴퓨터와 비교하는 함수
def rsp(my_rsp):
    transfer_kor(my_rsp)
    transfer_num(computer)
    if my_rsp == computer:
        return '무승부'
    elif (my_rsp == '0' and computer == '1') | (my_rsp == '1' and computer == '2') |(my_rsp == '2' and computer == '0') :
        return '컴퓨터 승리'
    elif (my_rsp == '1' and computer == '0') | (my_rsp == '2' and computer == '1') | (my_rsp == '0' and computer == '2'):
        return '내가 승리'

#숫자인 경우 한글로 변환
def transfer_num(number):
    if number == '0':
        return '가위'
    elif number == '1':
        return '바위'
    elif number == '2':
        return '보'

def transfer_kor(number):
    if number == '0' or number == '1' or number == '2':
        return int(number)
    elif number == '가위':
        return 0
    elif number == '바위':
        return 1
    elif number == '보:':
        return 2

my = input("가위 바위 보 : ")

computer = str(random.randint(0, 2))

print("나", transfer_num(my))
print("컴퓨터", transfer_num(computer))

print(rsp(my))