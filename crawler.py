#A Simple Crawler to extract the titles of 
# first n pages (if n==-1, all pages) 
# starting from a given wiki page in wikipedia
# DONOT CHANGE FUNCTION NAME AND PARAMETERS
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin,urlparse


#assign domain name of input url here
domain=""
def main(url,n=-1):
    global domain
    #traversal algorithm in here
    # should return list of titles
    pass

#check if the link provided is an html file or not
def checkmedia(url):
	#check content type of url
    pass

#extract of urls from all a tags in soup
def get_all_links(soup,i):
    #find all <a> tag
	#extract list of links
	#filter based on domain, using filter()
	#avoid fragments, using filter()
    pass

#get title of page
def get_title(soup):
    pass

#check if domain is same
def checkdomain(link):
	pass

#check if any fragments (www.google.co.in/#a, #a is a fragment)
def checkfragment(link):
	pass

#run the main function if executed as main
if __name__=="__main__":
	print("\n".join(main(input().strip(),10)))