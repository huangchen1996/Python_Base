ticket = 1
knife = 9
if ticket == 1:
    print("你可以进入车栈")
    if knife > 8:
        print("不好意思，您携带的工具太过于危险，不能上车")
    else:
        print("祝您旅途愉快")
else:
    print("不好意思，您缺少相关物件不能进入车站")
