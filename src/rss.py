#!/usr/bin/python
import sys
import urllib
import json
import uuid
sys.path.append("./")

from bs4 import BeautifulSoup
html = urllib.urlopen("http://tertuliarium.org/?page_id=19")
bsObj = BeautifulSoup(html.read(), 'html.parser')
LI=bsObj.find_all('li')

list1 = ' '.join(sys.argv[1:])

#=======================================
def numero(file):
	x = file.find(unichr(8211))
	return file[5:x-1].strip()

def parentesis(file):
	return (file.find('%28') , file.find('%29')) 
	
def titulo(file):
	x = parentesis(file)
	y = file.find(unichr(8211))
	if x[0]>0 and x[1] >0:
		return file[y+1:x[0]-1].strip()
	else:
		return file[y+1:].strip()

def especialidade(file):
	x = parentesis(file)
	if x[0]>0 and x[1] >0:
		return file[x[0]+3:x[1]].strip()
	else:
		return ''
#=======================================
def main():
  data = {}
  for x in range(0,len(LI)):
    A = LI[x].a
    if A != None:
    	link = A.get('href')
    	if link.find("youtu") == -1:
            if link.find("dropbox") >= 0:
                z = LI[x].text
		if numero(z).isdigit():
			data[numero(z)]= [titulo(z) , especialidade(link) , link, "31/12/2018", str(uuid.uuid5(uuid.NAMESPACE_DNS, titulo(z).encode('utf-8')))]
  print json.dumps(data)
#=======================================
if __name__ == '__main__':
    main()
