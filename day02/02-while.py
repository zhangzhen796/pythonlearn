# userlist = {"zean":19871121,"wangxin":19871111}
#
# username = input('please input username: ')
# while username not in userlist:
#     username = input('please input username: ')
#
# # /
# for i in range(1,10000000):
# #     print(i)
# alist = [('a','b','c'),{'zean':19871121},['a','b','c']]
# for i in alist:
#     for data in i:
#         print(data)
#     print('*' * 30)
for i in range(1,10):
    for a in range(1,i+1):
        print('%s*%s=%s' %(i,a,i*a),end=' ')
    print()
