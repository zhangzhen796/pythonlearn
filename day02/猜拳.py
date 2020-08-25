import random
comwin = 0
humwin = 0
count = 0
all_choices = ['石头','剪刀','布']
while count <= 4:
    com = random.choice(all_choices)
    hum = input('请出拳(石头/剪刀/布):')
    win_list = [["石头","剪刀"],["剪刀","布"],["布","石头"]]
    print('电脑出的%s' %com)
    print('你出的%s' %hum)
    if [hum,com] in win_list:
        print('你赢了')
        humwin += 1
        if humwin == 2:
            print("你赢了比赛")
            break
    elif hum == com:
        print('平局')
    elif [com,hum] in win_list:
        print("你输了")
        comwin += 1
        if comwin == 2:
            print("你输了比赛")
            break
    count += 1



