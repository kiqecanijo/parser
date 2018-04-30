import re
final = re.findall('([\s\S]*?)(I|[.]\d\d)',open('string.txt','r').read().replace('\n',''))
for match in final:
    for i in match:
        if (len(i) >= 3):
             print i
