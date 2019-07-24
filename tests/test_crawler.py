from .. import crawler
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
class Test_check_media(object):
    def test_1(self):
        url="https://pytest.org/en/latest/getting-started.html"
        assert crawler.checkmedia(url)==True
    
    def test_2(self):
        url="https://en.wikipedia.org/wiki/Occult"
        assert crawler.checkmedia(url)==True
    
    def test_3(self):
        url="https://upload.wikimedia.org/wikipedia/commons/1/19/Lt._Gen._Leslie_C._Smith.jpg"
        assert crawler.checkmedia(url)==False

class Test_check_domain(object):
    def test_1(self):
        crawler.domain=urlparse("https://en.wikipedia.org/wiki/Occult").netloc
        url="https://stackoverflow.com/questions"
        assert crawler.checkdomain(url)==False
    
    def test_2(self):
        crawler.domain=urlparse("https://en.wikipedia.org/wiki/Occult").netloc
        url="https://en.wikipedia.org/wiki/Occult"
        assert crawler.checkdomain(url)==True

class Test_get_title(object):
    def test_1(self):
        html="<html><head></head><title>hey</title><body></body></html>"
        soup=BeautifulSoup(html,"html.parser")
        assert crawler.get_title(soup)=="hey"
    
class Test_get_a(object):
    def test_1(self):
        i="https://en.wikipedia.org/wiki/Occult"
        crawler.domain=urlparse("https://en.wikipedia.org/wiki/Occult").netloc
        html="""
        <a href='https://en.wikipedia.org/wiki/Occult/A'></a>
        <div><a href='https://en.wikipedia.org/wiki/Occult#content'>
            </a><a href='https://en.wikibook.org/Occult'>
            </a><a></a>
        </div>
        <a href='./B'></a>"""
        soup=BeautifulSoup(html,"html.parser")
        re=["https://en.wikipedia.org/wiki/Occult/A","https://en.wikipedia.org/wiki/B"]
        assert crawler.get_all_links(soup,i)==re

class Test_main(object):
    def test_1(self):
        url="https://en.wikipedia.org/wiki/Occult"
        re=['Occult - Wikipedia', 'Occult (disambiguation) - Wikipedia', 
        'The Occult: A History - Wikipedia', 'Latin - Wikipedia', 
        'Paranormal - Wikipedia', 'Fact - Wikipedia', 'Measure (mathematics) - Wikipedia', 
        'Science - Wikipedia', 'Speculative reason - Wikipedia', 'Western esotericism - Wikipedia', 
        'Astrology - Wikipedia']
        assert crawler.main(url,10)==re
