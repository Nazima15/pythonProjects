import re

txt1="Hello World, Hi python"
txt2="Nice to meet you"

print(re.search('^Hi', txt1))
print(re.search('^Nice', txt2))
print(re.search('python$', txt1))
print(re.search('to$', txt2))