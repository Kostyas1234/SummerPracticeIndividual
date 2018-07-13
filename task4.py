import sys , math
args = sys.argv
args = [float(i) for i in args[1:]]


def result(arg):
    print("log(%s)" % (str(arg)))
    if arg > 0:
        print(" = {}".format(round(math.log(arg), 6)))
    else:
        print(" is illegal")


print("first loop")
for r in args[0:]:
    result(r)
print("second loop")
for r in range(len(args)):
    result(args[r])
print("third loop")
r = 0
while r < len(args):
    result(args[r])
    r += 1;
print("fourth loop")
r = 0;
try:
    while 1:
        result(args[r])
        r += 1
except:
    print("out of arguments array, stop going further")
