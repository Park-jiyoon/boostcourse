import random

my_win = 0
com_win = 0
draw = 0
def rsp_advanced(num):
    i = 1

    while i <= num:
        my = input("가위 바위 보 : ")
        if another_inpu(my) == False:
            continue
        else:
            rsp(my, i)
            i = i+1
    print('나의 전적 : ',my_win, '승', draw, '무', com_win, '패')
    print('컴퓨터의 전적 : ', com_win, '승', draw, '무', my_win, '패')



#컴퓨터와 비교하는 함수
def rsp(my_num, count):
    global my_win
    global com_win
    global draw
    computer = str(random.randint(0, 2))
    print("나", transfer_num(my_num))
    print("컴퓨터", transfer_num(computer))

    transfer_kor(my_num)
    transfer_num(computer)
    if my_num == computer:
        print(count, '번째 판 무승부!')
        draw = draw + 1
    elif (my_num == '0' and computer == '1') | (my_num == '1' and computer == '2') |(my_num == '2' and computer == '0') :
        print(count, '번째 판 컴퓨터 승리!')
        com_win = com_win + 1
    elif (my_num == '1' and computer == '0') | (my_num == '2' and computer == '1') | (my_num == '0' and computer == '2'):
        print(count, '번째 판 나의 승리!')
        my_win = my_win + 1

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



def another_inpu(data):
    if data == '0' or data == '1' or data == '2' or data =='가위' or data == '바위' or data == '보':
        return True
    else:
        return False

games = int(input("몇 판을 진행하시겠습니까? "))

rsp_advanced(games)