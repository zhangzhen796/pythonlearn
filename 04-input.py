#!/usr/local/bin/python3
number = input("请输入数字: ")   #input用于获取键盘输入，默认是字符串类型
print(number)
print(type(number))  # input获得的数据是字符串

# print(number + 10 ) #报错,不能把字符和数字作运算
print(int(number) + 10)  #把input进来的字符串转成int类型，就可以和数字作运算
print(number + str(10)) #把10转换str类型与前面的值作拼接处理