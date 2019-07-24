from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin,urlparse
#assign domain name of input url here
domain=""
#A Simple Crawler to extract the titles of 
# first n pages (if n==-1, all pages) 
# starting from a given wiki page in wikipedia

def main(url,n=-1):
    global domain
    #set start url
    #avoid revisiting
    #set title list
    #only extract links in a tags inside main content
    #exclude the navigation links
    pass

#check if the link provided is an html file or not
def checkmedia(url):
	#check content type of url
    pass

#extract of urls from all a tags in soup
def get_all_links(soup,i):
    #find all <a> tag
	#extract list of links
	#filter based on domain
	#avoid fragments
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

#run the main function if executed as main than module
if __name__=="__main__":
	print("\n".join(main(input().strip(),10)))