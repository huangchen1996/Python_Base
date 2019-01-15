'''
append
通过append可以向列表添加元素
'''
#定义变量A，默认有3个元素
A = ['huangchen', 'nan', 'age']


print("---添加之前，列表A的数据---")
for tempName in A:
    print(tempName)

    #提示，并添加元素
    temp = input("请输入要添加的学生姓名:")
    A.append(temp)

    print("----添加之后，列表A的数据----")
    for tempName in A:
        print(tempName)


'''
extend
通过extend可以将另一个集合中的元素逐一添加到列表中
'''
a = [1, 2]
b = [3, 4]
print(a.append(b))
print(a)


'''
insert
insert(index, object) 在指定位置index前插入元素object
'''
a = [0, 1, 2]
a.insert(1, 3)
print(a)

