import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
import re
r=[]
f =open("athichudi.txt","w",encoding="utf-8")
reqd="https://www.projectmadurai.org/pm_etexts/utf8/pmuni0002.html"
page=urllib2.urlopen(reqd)
soup=BeautifulSoup(page)
word=soup.find_all("p")
for i in word:
	a=str(i)
	b=re.sub(r"<p>","",a)
	b=re.sub(r"[a-z]","",b)
	b=re.sub(r"</>","",b)
	b=re.sub(r"[A-Z]","",b)
	b=re.sub(r"\(","",b)
	b=re.sub(r" . ","",b)
	b=re.sub(r"[0-9]","",b)
	b=re.sub(r":","",b)
	b=re.sub(r"<>"," ",b)
	r.append(b)

r=r[2:5]
for i in r:
	f.write(i)
