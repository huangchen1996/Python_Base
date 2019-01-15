#列表介绍
namesList = ['huangchen', 'huang', 'chen']
print("列表介绍")
print(namesList[0])
print(namesList[1])
print(namesList[2])
print("------"*30)
'''
列表的循环遍历
'''
#1使用for循环
print("for循环遍历名字")
namesList = ['xiaoming','xiao','ming']
for name in namesList:
    print(name)


print("=="*20)

#2while循环
nameLists = ['helloworld', 'hello', 'world']

length = len(nameLists)

i = 0

while i < length:
    print(nameLists[i])
    i+=1