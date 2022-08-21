stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]


def stock_profit(st, se):
    st = st.split(',')
    profit = 0
    n = 0
    dic = dict()
    for s in st:
        v = s.split('/')
        profit = (se[n]/int((v[2]))*100 - 100)   #수익률 : 현재가/매입가*100 - 100
        dic[v[0]] = profit
        n = n + 1
    new = list()
    for k, c in dic.items():
        new.append((c, k))

    new = sorted(new, reverse=True)

    for li in new:
        print(li[1] + "의 수익률 %.2f"%li[0])

stock_profit(stocks, sells)