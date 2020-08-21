sentence = 'tom\'s pet is a cat'
sentence2 = "tom 's pet is acat"
sentence4 = 'tom said:"hello world"'
sentence3 = "tom said:\"hello world!\""
words = """
hello
world
abcd"""
print(words)
py_str = 'pyhton'
print(len(py_str))
print(py_str[1]) #第二个字符
print(py_str[2:4]) #切面，从起始下表包含，结束下表不包含
print(py_str[2:])# 从下标为2的字符取到结尾
print(py_str[:2])# 从开头取到下标是2之前的字符
print(py_str[:]) #取全部
print(py_str[::2])# 步长值为2，默认是1
print(py_str[1::2])# 取出yhn
print(py_str[::-1])# 步长为负，表示自右向左取
print(py_str + 'is good') #字符串拼接
print(py_str * 3)# 把字符串重复3遍
't' in py_str   #字符串关系测试
'r' not in py_str