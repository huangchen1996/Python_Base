#print(spam(1))从未被执行是因为一旦执行跳到except子句的代码，就不会回到try子句。
def spam(divideBy):
	return 42 / divideBy

try:
	print(spam(2))
	print(spam(12))
	print(spam(0))
	print(spam(1))
except ZeroDivisionError:
	print("除数不能为0")
