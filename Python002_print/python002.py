import glob
import os
import time

print( "into the python002.py" )

if __name__ == '__main__':
	print( "main()" )
	# print with parameter
	print( "{0} doing...".format(time.ctime()) ) #use'.' here to make parameter work
	# method 1
	print("Total score for %s is %s" % ("param1","param2"))
	# method 2 , as a dictionary
	print("Total score for %(n)s is %(s)s" % {'n': "name", 's': "score"})
	# method 3 , new style strin format
	print( "{0} {1} doing...".format("param1","param2") )
	# method 4
	name = "john"
	score = 80
	print("Total score for", name, "is", score)
	# If you don't want spaces to be inserted automatically by print in the above example, change the sep parameter:
	print("Total score for ", name, " is ", score, sep='')
	