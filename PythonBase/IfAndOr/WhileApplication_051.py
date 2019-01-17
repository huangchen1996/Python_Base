#计算1~100之间偶数累积和
i = 1
sum = 0
while i<= 100:
    if i%2 == 0:
        sum = sum + i
    i+=1

print("1~100偶数累加和为:%d"%sum)
