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

