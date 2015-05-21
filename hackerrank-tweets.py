#Solution to https://www.hackerrank.com/challenges/detect-the-email-addresses

# by: Strobes27

import re

N = int(raw_input())
count = 0

for _ in range(N):
    tweet = raw_input()
    match = re.search(r'hackerrank', tweet, re.IGNORECASE)
    if match:
        count += 1
        
print count
