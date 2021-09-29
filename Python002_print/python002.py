import glob
import os
import time

TAG =\
"""X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains"""

print( "into the python002.py" )

if __name__ == '__main__':
        print( "main()" )
        # print with parameter
        print( "{0} doing...".format(time.ctime()) ) #use'.' here to make parameter work
        criteria = 'http server: has security header section:\r\n{0} \r\nhttps server: has security header section \r\n{0} '.format(TAG)
        print( "{0}".format(criteria) )
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
	
