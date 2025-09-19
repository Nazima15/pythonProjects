import re

txt1="Hello World, Hi python"
txt2="Nice to meet you"
txt3="YJU-1"
txt4="YJU-4"
pattern="^YJU-[123]"
print(re.search(pattern, txt3)) #성공
print(re.search(pattern, txt4)) #실패

print(re.search('^Hi',txt1 ))
print(re.search('^Nice', txt2))
print(re.search('python$', txt1))
print(re.search('to$', txt2))