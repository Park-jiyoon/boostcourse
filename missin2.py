monthly_payment = input("월급 입력 : ")
pay_yearly = int(monthly_payment) * 12


def yearly_payment(pay):

    if pay_yearly <= 1200:
        return pay_yearly * (1-0.06)
    elif pay_yearly <= 4600:
        return pay_yearly * (1-0.15)
    elif pay_yearly <= 8800:
        return pay_yearly * (1-0.24)
    elif pay_yearly <= 15000:
        return pay_yearly * (1-0.38)
    elif pay_yearly <= 50000:
        return pay_yearly * (1-0.4)
    elif pay_yearly > 50000:
        return pay_yearly * (1-0.42)

print("세전 연봉 : ", pay_yearly , "만원")
print("세후 연봉 : ", int(yearly_payment(pay_yearly)), "만원")