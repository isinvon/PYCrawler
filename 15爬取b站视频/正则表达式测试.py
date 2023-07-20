import re

string = 'abcdefg我不是林信欢abcdefg12345'
print('原文: ' + string)

# 测试贪婪匹配
demo1 = re.findall('(a.*)', string)
print('贪婪匹配:' + str(demo1))

# 测试非贪婪匹配
demo2 = re.findall('(a.*?)', string)
print('非贪婪匹配: ' + str(demo2))

# 测试其他

demo3 = re.findall('(a.)', string)
print('其他3: ' + str(demo3))

demo4 = re.findall('(a...)', string)
print('其他4: ' + str(demo4))

demo5 = re.findall('(a.......)', string)
print('其他5: ' + str(demo5))

demo6 = re.findall('(.)', string)
print('其他6: ' + str(demo6))

demo7 = re.findall('(.我)', string)
print('其他7: ' + str(demo7))

demo8 = re.findall('(..我)', string)
print('其他8: ' + str(demo8))

demo9 = re.findall('(..我..)', string)
print('其他9: ' + str(demo9))

demo10 = re.findall('(..我.*)', string)
print('其他10: ' + str(demo10))

demo11 = re.findall('(..我.*..?)', string)
print('其他11: ' + str(demo11))

demo12 = re.findall('(.?我)', string)
print('其他12: ' + str(demo12))


