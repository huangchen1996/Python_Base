from sys import argv

#通过解析包argv获取 脚本名 和将要保存的文件名
script, filename = argv

#询问是否继续编辑文件filename
print("We're going to erase %r." % filename)
print("If you don't want that,hit CTRL-C(^C).")
print("If you do want that,hit RETURN.")

#等待用户输入是否继续编辑
input("?")

#如果用户未输入ctrl-c则会继续执行
print("Opening the file....")

#打开文件对象
target = open(filename, 'w')

#没有指定truncate（）大小，所以实际上删除了文件的内容
print("Truncation the file,GoodBye!")
target.truncate()

#获取三个input变量的内容
print("Now I'm going toask you for three lines.")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

#将内容写入文件(只在内存中，并未写入硬盘)
print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#关闭文件，将文件写入硬盘
print("And finally,we close it.")
target.close()


