#变量名帮忙记住程序的内容，变量简单理解就是给一段代码或值取个名字，这个名字就是变量了，在编写代码的时候可以用变量名代指被命名的代码或值
#print()函数以及运算方式的基础上将值命名成为变量后进行运算并打印

#变量命名规则
#变量名只能使用字母、数字、下划线。但不能以数字开头
#变量名不能包含空格，但可以用下划线替代表示
#不要使用 Python 的关键字和函数名作为变量名。（ Python 关键字可参考：37.复习各种符号 ）
#变量名应该尽力简洁但更应具有具有描述性。
#慎用易混淆的字符，例如小写 l 和大写 O 它们很容易被当作数字。而中文的逗号、引号也容易和英文的混淆。



#汽车100辆
cars = 100

#一辆汽车的空间大小
space_in_a_car = 4.0

#30名司机
drivers = 30

#90个路人
passengers = 90

#不开(闲置)的车辆为汽车总数减去司机人数
cars_not_driven = cars - drivers

#汽车司机的人数等于汽车的总数
cars_driven = drivers

#一起使用汽车的利用率等于司机人数乘以汽车内部空间
carpool_capacity = cars_driven * space_in_a_car

#平均每辆车搭载的游客数为游客数量除以司机人数
average_passengers_per_car = passengers / cars_driven




print("这儿有",cars,"cars 是在使用的.")

print("这儿只有",drivers,"drivers可以驾驶汽车")

print("这儿将会有",cars_not_driven,"cars 是空的，不会被驾驶在今天")

print("We can transport",carpool_capacity,"people today")

print("We have",passengers,"to carpool today.")

print("We need to put about",average_passengers_per_car,"in echo car.")

