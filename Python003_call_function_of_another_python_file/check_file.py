import os
import re

TAG =\
"""X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains"""

def Check():
    criteria = 'http server: has security header section:\r\n{0} \r\nhttps server: has security header section:\r\n{0} '.format(TAG)
    print( '{0}'.format(criteria) )
