#本习题重点:转义字符(escape character)\n
print("Python使用双引号" 'Python使用单引号')

tabby_cat = "\tI'm tabbed in."

persian_cat = "I'm split\non aline"

backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list;
\t* Cat food
\t* Fishies
\t* Catnipn\n\t Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


#将转义序列和格式化
#转义字符演示
#r''是原始字符串，有点像，保持原始数据不会转义字符
print(r"\n [换行]演示", "\n第一行\n第二行")
print("-" * 20)
print(r"\\ [反斜杆]演示，", "\n一个反斜杆;\\", )
print("-" * 20)
print(r"\' 和 \" 【引号】演示,"," \n英文双引号,\",英文单引号,\'" )
print("-" * 20)
print(r"行末\ 【不换行】演示：", "\n我不想\换行")
print("-" * 20)
print(r"\t 【制表符】演示:", "\n\t横向制表符")
print("-" * 20)
print(r"\v 【纵向制表符】演示：", "\n\v纵向制表符")
print("-" * 20)
print(r"\v 【响铃】演示：", "\n打开音响哦\a")
print("-" * 20)
print(r"\v 【退格】演示：", "\n退格键\b(后面必须加一些东西)")
print("-" * 20)
print(r"\v 【空】演示：", "\n--\000--", '' == '\000')
print("-" * 20)
print(r"\v 【回车】演示：", "\naaa\r6666\r23333")
print("-" * 20)
print(r"\v 【翻页】演示：", "\n翻页\f翻页后")
print("-" * 20)
print(r"\v 【八进字符】演示：", "\n\044")
print("-" * 20)
print(r"\v 【十六进字符】演示：", "\n\x44")



