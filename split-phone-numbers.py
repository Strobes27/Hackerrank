#Solution to https://www.hackerrank.com/challenges/detect-the-email-addresses

# by: Strobes27

import re

N = int(raw_input())

for _ in range(N):
    case = raw_input()
    countrycode = re.search(r'[0-9]{1,3}', case)
    
    if countrycode:
        ccode = countrycode.group()
    areacode = re.search(r'([- ])([0-9]{1,3})', case)
   
    if areacode:
        acode = areacode.group(2)
    num = re.search(r'[0-9]{4,10}', case)
    
    if num:
        ncode = num.group()
    
    print "CountryCode=%s,LocalAreaCode=%s,Number=%s" % (ccode, acode, ncode)