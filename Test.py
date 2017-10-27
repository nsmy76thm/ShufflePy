import sys

print("Test2")
print(sys.argv)

for i in range(len(sys.argv)):
    if i == 0:
        print ("Funktionsname: %s" % sys.argv[0])
    else:
        print ("%d. Argument: %s" % (i,sys.argv[i]))