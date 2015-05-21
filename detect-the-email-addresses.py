
#Solution to https://www.hackerrank.com/challenges/detect-the-email-addresses

# by: Strobes27

import re

N = int(raw_input())
lines = " ".join([raw_input() for i in range(N)])

regex = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b")
mails = re.findall(regex, lines)

print ";".join(sorted(set(mails)))