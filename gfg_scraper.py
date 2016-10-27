from bs4 import BeautifulSoup as bs
import urllib, requests

r=requests.get('http://www.geeksforgeeks.org/fundamentals-of-algorithms/')
soup=bs(r.text,'lxml')
data=soup.find_all('div',{ 'class' : 'entry-content' } )
li = data[0].find_all('li')
arr=[]
for i in li:
	link = i.find('a').get('href')
	t=i.text
	arr.append([link,t])

l=[]
find = raw_input('Give a topic name : ')
for link, t in arr:
	if find.lower() in t.lower():
		l.append([link, t])
		
j=1
for link, t in l:
	print '%d. \n%s\n%s'%(j,t,link)
	j+=1

ch=int(raw_input('\nChoose the index from above : '))
# print l[ch-1][0]
# r=requests.get(l[ch-1][0])
# soup=bs(r.text,'lxml')
# print soup
# data=soup.find_all('div', { 'class' : 'entry-content'})[0].find_all('p')
# print data