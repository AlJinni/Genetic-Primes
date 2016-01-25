import random

squcos=random.randint(-200,200)
lincos=random.randint(-200,200)
varcos=random.randint(-200,200)
gen=[]
for x in range(0,100):
    gen.append(1)
    gen[x]=squcos*x*x+lincos*x+varcos
gen.sort()
print squcos
print ":::::::"
print lincos
print ":::::::"
print varcos
print ":::::::"
print gen
