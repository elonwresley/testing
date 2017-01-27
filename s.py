import sys
import time
if len(sys.argv) != 4:
    print("Need three arguments after script name")
    sys.exit(1)
script, first, second, third = sys.argv
print "the script is:", script
print "the first variable is:", first
print "the second variable is:", second
print "the third variable is:", third
time.sleep(10)
