import re

f = open('test1.txt')

for line in f:
    line = line.rstrip()
    if re.search(r'^\([0-9]+\)', line):
        print(line)

f.close()
