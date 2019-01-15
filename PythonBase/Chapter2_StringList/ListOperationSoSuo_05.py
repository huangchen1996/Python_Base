'''
查找元素(查in,not in,index,count)
所谓的查找，就是看看指定的元素是否存在

in,not in

python中查找的常用方法为:
in(存在),如果存在那么结果为true，否则为false
not in(不存在),如果不存在那么结果为true，否则为false
'''


#待查找的列表
nameList = ['小明', '一二三', '一二三二三']

#获取用户要查找的名字
findName = input('请输入要查找的姓名:')

#查找是否存在
if findName in nameList:
    print('在字典中找到了相同的名字')
else:
    print('没有找到')