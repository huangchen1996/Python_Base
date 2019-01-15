'''
find命令
检测huang是否包含在mystr中，如果是返回开始的初始值，如果不是返回-1
'''
mystr = 'My Name is hc'
print(mystr.find("h"))
#mystr.find(huang, 0, 17)


"""
index
也是查询字符串是否在里面，如果不在会报异常
mystr.index(str, start=0, end=len(mystr)) 
"""
print(mystr.index("My", 0, 2))


'''
count
返回字符串在start和end之间在字符串中出现的次数
mystr.count(str, start=0, end=len(mystr))
'''
MyName = "HuangChen"
print(MyName.count("n", 0, 9))

'''
replace
把 myName 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次
myName.replace(str1,str2,mystr.count(str1))
'''
myName = "Python Java C"
print(myName.replace("C", "Python", 2))


'''
split
以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
mystr.split(stri=" ", 2)   
'''
myBook = "This is my favorite book"
print(myBook.split(" ", 3))


'''
capitalize
把字符串第一个字符大写
mystr.capitallize()
'''
mystring = "nihao"
print(mystring.capitalize())


'''
title
把字符串的每个单词的首字母大写
a.title
'''
mytitle = "da xiao xie"
print(mytitle.title())

'''
startwith
检查字符串是否是以obj开头，是则返回True，否则返回False
mystartwith.startswith(obj)
'''
mystartwith = "obj是面向对象编程"
print(mystartwith.startswith('obj'))

'''
endwith
检查字符串是否以obj结束，如果是返回True,否则返回 False.
myendwith.endswith('obj')
'''
myendwith = "这是obj"
print(myendwith.endswith('obj'))


'''
lower
转换 mystr 中所有大写字符为小写
mystr.lower()      
'''
mylower = "ABCDEFGHIJKLMNOPQRST"
print(mylower.lower())





