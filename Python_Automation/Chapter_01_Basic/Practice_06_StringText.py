#字符串和文本
#习题学习要点
#使用复杂的字符串建立一系列的变量
#作用:字符串通常是指你想要从程序里"导出"的一段字符

#学习单词  binary:二进制


#基础练习
#在变量中使用格式化字符
x = "这儿有 %d 种类型的人。" % 10
#在变量中使用格式化字符，并且格式化其他变量
binary = "binary"
do_not = "don`t"
y = "有谁知道哪些是 %s 那些 %s." %(binary,do_not)

print(x)
print(y)

#利用%r格式化格式化字符显示原始字符的引号
#打印字符串和格式化的变量
print("我说: %r." % x)
print("我也说过: '%s'." %y )

#这里格式化了一个布尔变量False
hilarious = False
joke_evaluation = "这个笑话是否有趣?! %r"

print(joke_evaluation % hilarious)

#字符串拼接
w = "这是左边。。。"
e = "这是右边...."

print(w + e)


#显示字符串的拼接打印
print("双引号表示字符串")

print('单引号表示字符串')

#使用单引号还是双引号PEP8没有特别规定

#如何打印有引号的字符串?
print(w + e)