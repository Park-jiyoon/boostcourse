import random


def bs31():
    i = 0
    now = 0
    print("베스킨라빈스 써리원 게임")
    while now <= 31:
        my = input("My turn - 숫자를 입력하세요: ")
        my= my.split()

        if int(my[0]) != now+1:
            print('1 큰수만 입력 하세요.')
            continue
        if len(my) == 2:
            if int(my[1])-int(my[0]) != 1:
                print('연속된 숫자를 입력하세요.')
                continue
        if len(my) == 3:
            if int(my[1])-int(my[0]) != 1 or int(my[2])-int(my[1]) != 1:
                print('연속된 숫자를 입력하세요.')
                continue
        if len(my) > 3:
            print('3개 이하로 입력하세요.')
            continue

        now = int(my[-1])
        print('현재 숫자', now)
        if now >= 31:
            print('패배')
            break
        computer_turn_num = random.randint(1,3)
        j=1
        while j <= computer_turn_num:
            num = now +j
            com = list()
            com.append(num)
            print('컴퓨터:', num)
            j = j + 1
        if 31 in com:
            print('승리')
            break
        now = num
        print('현재 숫자',now)
        i = i + 1
    print('게임 종료')
bs31()


