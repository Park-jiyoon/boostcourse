def check_id(id):
    gender = 0
    if id[7] == '1' or id[7] == '3':
        gender = '남자'
    elif id[7] == '2' or id[7] == '4':
        gender = '여자'

    print(id[:2] + '년' + id[2:4] + '월', gender)


def id_validation(id):
    year = int(id[:2])

    if 0 <= year <= 21:
        yes_or_no = input("2000년생 이후 출생자 입니까? 맞으면 o 아니면 x ")
        if (id[7] == 3 or id[7] == 4) and yes_or_no == 'o':
            return True
        else:
            return False
    else:
        return True


input_id = input("주민등록 번호를 입력해주세요: ")

if id_validation(input_id):
    check_id(input_id)
else:
    print('잘못된 번호입니다.\n올바른 번호를 입력하세요')