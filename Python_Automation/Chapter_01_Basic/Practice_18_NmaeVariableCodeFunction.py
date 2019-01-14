def print_two(*args):
    arg1, arg2 = args
    print("arg1:%r,arg2:%r" % (arg1, arg2))


def print_two_again(arg1, arg2):
    print("arg1:%r,arg2: %r" % (arg1, arg2))

#这是一个参数的
def print_one(arg1):
    print("arg1: %r" % arg1)

#这是没有参数的
def print_none():
    print("I got nothin")

#下面是调用函数的演示
#不去使用函数的话，它们是不会打印任何东西出来的
print_two("Huang", "Chen")
print_two_again("Huang", "Chen")
print_one("First!")
print_none()