#导入Python部分功能模块

from sys import argv

#将argv进行解包，作用是将argv中包含的值依次赋值给左边的几个变量
script, user_name = argv
prompt = '>'

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s" % user_name)
likes = input(prompt)


print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
          Alright,so you said %r about liking me.
          You live in %r,Not sure where that is.
          And you have a %r computer. Nice         
""" % (likes, lives,  computer))
