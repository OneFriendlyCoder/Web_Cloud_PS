"""program uses requests package to download a set of URLS
   prints the output of the getSequential() function.
   getSequential()-->getUrlTitle()-->this retrives the url title using the request.get method.
   uses BeautifulSoup to parse the html response to create a searchable data structure from it (soup).
   find()with 'title' returns the HTML <title> tags and returns its string representation.
"""
import requests
import multiprocessing  						#spawning multi python interpreters and have each one retrieve a subset of the URLs, a sequential approach makes the program execution slow.
from bs4 import BeautifulSoup

def getMulti(list_urls, num_processes):
	p = multiprocessing.Pool(num_processes)
	titles = p.map(getUrlTitle, list_urls) #execute each getUrlTitle() on each of the URLs in the list of URLs in parallel.
	p.close()
	return(titles) 

def getUrlTitle(url):
	"""this function returns the title of an html document given in its URL
		:param URL : the url to retrieve
		:type url : str
		:return : title of the URL
		:rtype : str
	"""
	resp=requests.get(url)                       
	soup=BeautifulSoup(resp.text,'html.parser')
	title=str(soup.find('title'))
	return(title)

"""
#Sequential approach towards getting the URLs.

def getSequential(urls):
	titles=[]
	for u in urls:
		titles.append(getUrlTitle(u))
	return(titles)
"""
list_urls=['https://pdx.edu','https://oregonctf.org','https://erp.iitkgp.ac.in/','https://facebook.com']
print(getMulti(list_urls,300))
