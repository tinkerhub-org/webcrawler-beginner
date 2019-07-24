# Tutorial

## Prerequisite Information

1. Requests
    - importing requests

        ```import requests```
        
    - To make a GET request

        ```req=requests.get(url)```

    - To make a HEAD request

        ```req=requests.head(url)```

    - To get Content-Type header

        ```req.headers["Content-Type"]```

    - To get content(html page)

        ```req.content```

2. BeautifulSoup
    - importing BeautifulSoup

        ```from bs4 import BeautifulSoup```

    - To parse html content (variable ```html``` contains html page as string)

        ```soup=BeautifulSoup(html,"html.parser")```

    - To find an element

        ```soup.find('tagname')```

    - To find an element with tagname and class

        ```soup.find('tagname',{'class':'classname'})```

    - To find all elements with tagname

        ```soup.find_all('tagname')```

    - To get attribute value of a tag
        ```tag=soup.find("tagname")```
        ```tag.attrs['attributename']```

    - The above commands can be used on results of find() and each element in result of find_all(). example:

        ```soup=BeautifulSoup("<a>outside</a><div><a>inside</a></div>","html.parser")```

        ```soup2=soup.find("div")```

        ```print(soup2.find("a").text)```

        should print "inside", since you are searching for a tag inside div tag

3. Try BeautifulSoup by making sample html text and parsing it
4. Try these commands in python console before use
5. The content of wikipedia pages are in a ```<div class='mw-parser-output'>``` tag.
6. The URLs found in the href attribute of a tags are likely to be relative tags, hence for it to be used for extracting html page. You should convert to absolute url. use urljoin. example

    ```from urllib.parse import urljoin```
    ```urljoin("http://www.google.co.in/b/","/a")```

    The output should be http://www.google.co.in/a

7. To extract url details like domain, path, fragment. use urlparse. Example

    ```from urllib.parse import urlparse```
    ```urlparse("http://www.google.co.in/b/a?q#a")```

    Output should be

    ```ParseResult(scheme='http', netloc='www.google.co.in', path='/b/a', params='', query='q', fragment='a')```

## HOW IT WORKS

The crawler has a list of urls,a list of visited urls and list of titles

It loops through the list of urls doing the following

    check if the url leads to an HTML page and if its not already visited.

    if yes, parses the page and extracts the title and all relevant urls.

    - Add all relevant links into the list of urls
    -appends the visited url into the list of visited urls
    -Append title to list of titles

The above loop should terminate if number of titles extracted reaches ```n```(```n``` is an argument in main()) or run till all pages have been visited(if ```n=-1```).

The traversal algorithm described above should be written in main()

The other functions are to be filled and used according to the purpose described in comments.

The relevance of a url is based on

- If the url contains fragments, it maybe ignored since its a url to self

- If the url doesnt have same domain as wikipedia, it wont have the information(related titles of articles) we seek.

## Advanced Improvements (Not to be done here)
- You can attempt to convert the crawler into a multithreaded application to increase the speed

- [Use scrapy framework](https://scrapy.org/) 