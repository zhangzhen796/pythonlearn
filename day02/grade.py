seco = int(input("请输入分数："))
if 60 <= seco <= 70:
    print("及格")
elif 70 <= seco <= 80:
    print('良')
elif 80 <= seco <= 90:
    print('好')
elif 90 <= seco:
    print('优秀')
else:
    print('要努力了')
