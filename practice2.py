import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com"
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify())
title=soup.title
#print(title)
#print(type(title))
#print(type(title.string))
#print(type(soup))
paras=soup.find_all('p')
#print(paras)
anchors =soup.find_all('a')
#print(anchors )
#print(soup.find('p')) get first element of paragraph
#print(soup.find_all('p')) get all paragraphs
#print(soup.find('p')['class']) get the class of 1st element
#print(soup.find('p')['id']) get id of the 1st element
#print(soup.find_all('p',class_='lead')) will get all the elements whose class is lead
#print(soup.find('p').get_text())    text of the 1st paragraph
#print(soup.get_text())
anchors =soup.find_all('a')
#for link in anchors:  to get all the links inside the website
    ##if(link.get("href") != '#'):
        #linktext="https://www.codewithharry.com"+ link.get("href")
       # all_link.add(link)
       # print(linktext)

#markup = "<p><!-- this is a comment--></p>"
#soup2 = BeautifulSoup(markup)
#print(soup2.p.string)

navbarSupportedContent=soup.find(id='navbarSupportedContent')
#print(navbarSupportedContent.children)  for finding the children

#print(navbarSupportedContent.contents) make availabe all the elements

#for item in navbarSupportedContent.strings:
   # print(item)       this is used to find strings in an id named xyz

#print(navbarSupportedContent.parent)  prints the parent of an element
