import re

with open('test1.txt') as f:
    txt = f.read()

output = re.findall(r'\S+@[a-z.]+', txt)

print('추출된 이메일 개수:', len(output))
print('추출된 이메일 목록:\n', output)