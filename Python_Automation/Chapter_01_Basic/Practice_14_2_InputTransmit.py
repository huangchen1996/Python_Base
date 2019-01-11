#将prompt修改为其他参数再运行

from sys import argv

script, user_name = argv
#prompt这个变量改变为user_name
prompt = '%s' % user_name

print("Hi %s,I'm the %s script." % (user_name, script))
print("I'd like to ask a few questions.")
print("Do you like me %s?" % user_name)
likes = input()

print("Where do you live %s?" % user_name)
lives = input()

print("What kind of computer do you have?")

computer = input()

print("""
Alright,so you said %r about liking me.
you live in %r,Not sure where that is.
And you have a %r computer.Nice.
""" % (likes, lives, computer))
