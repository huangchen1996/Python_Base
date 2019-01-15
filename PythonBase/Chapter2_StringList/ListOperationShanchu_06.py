'''
删除元素("删"del, pop, remove)
列表元素的常用删除方法有：

    del：根据下标进行删除
    pop：删除最后一个元素
    remove：根据元素的值进行删除
'''





movieName = ['加勒比海盗', '黑客帝国', '第一滴血', '指环王', '速度与激情']
print('----删除之前----')
for tempName in movieName:
    print(tempName)


    del movieName[2]


    print('----删除之后----')
    for tempName in movieName:
        print(tempName)
