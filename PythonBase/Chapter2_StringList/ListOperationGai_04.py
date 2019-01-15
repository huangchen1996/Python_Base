'''
修改元素("改")
修改元素的时候，要通过下标来确定要修改的是哪个元素，然后才能进行修改
'''

#定义变量A，默认有3个元素
A = ['黄晨', '黄车', 'hahah']


print("----修改之前，列表A的数据----")
for tempName in A:
    print(tempName)



    #修改元素
    A[1] = '华一二'
    print("---修改之后，列表A的数据")
    for tempName in A:
        print(tempName)
