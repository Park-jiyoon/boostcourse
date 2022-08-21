# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4, 5, 3, 5, 6, 5, 3, 4, 1, 3, 4, 5], [2, 3, 4, 3, 1, 2, 0, 3, 2, 5, 7, 2],
                  [1, 3, 0, 3, 3, 4, 5, 6, 7, 2, 2, 1], [3, 2, 9, 2, 3, 5, 6, 6, 4, 6, 9, 9],
                  [8, 7, 7, 5, 6, 7, 5, 8, 8, 6, 10, 9], [7, 8, 4, 9, 5, 10, 3, 3, 2, 2, 1, 3]]


def sales_management(names, records):
    data = dict()
    sum = 0
    n = 0
    for name in names:
        for i in records[n]:
            sum = sum + i
        data[name] = sum / 12         # 평균 실적과 이름 딕셔너리에 넣음
        sum = 0
        n = n + 1
    new_data = list()

    for k, c in data.items():    #리스트로 매개변수 순서 변경해서 넣음
        new_data.append((c, k))

    new_data = sorted(new_data, reverse=True)  #내림차순으로 정렬

    for v in new_data[:2]:
        if v[0] > 5:
            print('보너스 대상자', v[1])
    for v in new_data[4:]:
        if v[0] < 3:
            print('면담 대상자', v[1])


sales_management(member_names, member_records)
