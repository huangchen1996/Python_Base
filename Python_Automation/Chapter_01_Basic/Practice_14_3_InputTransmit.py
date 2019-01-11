from sys import argv

#加一个call
script, user_name, call = argv
#将prompt变量改为user_name
prompt = '%s>' % user_name

print("Hi%s,I'm The %s Script." % (user_name, script))
print("Hmmm,you want me call you %s" % call) #新增的call参数
print("I'd like to ask you a few question.")
print("Do you like me%s" % user_name)
likes = input(call + "" + prompt)

print("Where do you live %s?" % user_name)
lives = input(call + "" + prompt)

print("What kind of computer do you have?")
computer = input(call + "" + prompt)

print("""
Alright,so you said %r about liking me.
you live in %r,Not sure where that is.
And you have a %r computer.Nice.
""" % (likes, lives, computer))
