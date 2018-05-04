import re,json,argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p", help="input relative file path, default string.txt")
args = parser.parse_args()
path = (args.p if args.p else 'string.txt')
final = re.findall('([\s\S]*?)(I|[.]\d\d)',open(path,'r').read().replace('\n',''))
concat = ''
jsonString = {}
curentTicket = 0
currentItem = 0
for column in final:
  for item in column:
    if item != 'H' or item != 'T' or item != 'I':
      concat += item
  if len(concat) >= 3:
    if concat.find(".") == -1:
      curentTicket += 1
      jsonString['ticket '+ str(curentTicket)] = {'head':{'ticket':concat[0:8],'customer':concat[8:15],'date':concat[15:21],'denomination':concat[21:24]}}
    elif concat.find("T") != -1 and len(concat) == 14:
      jsonString['ticket '+ str(curentTicket)]['total'] = {'#items':concat[2],'price':concat[-11:].replace('_','')}
    else:
      currentItem += 1
      jsonString['ticket '+ str(curentTicket)]['product '+str(currentItem)] = {'id':concat[0:5],'lifetime':concat[5:9],'cuantity':concat[9:15].replace('_',''),'price':concat[-9:].replace('_','')}
  concat = ''
print(json.dumps(jsonString, indent=2))
