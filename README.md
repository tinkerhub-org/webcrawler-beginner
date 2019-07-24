# Simple Web Crawler

A basic web crawler to go through wikipedia and extract titles of related pages from a starting page.

This is just a practice sample to get started with crawlers.
## How it Works ?

It uses requests to check if the given starting link is html file or not

Then process the html file using BeautifulSoup, to extract the required title and

Extract urls to follow from href attribute of ```<a>``` tags

## Prerequisites

- Python3 - Most code written in python
- Html - To understand how to parse html
- Http - To understand how to communicate with wikipedia to get html file

## Libraries used

- BeautifulSoup4 - For parsing html
- requests - For requesting url provided
- pytest - For testing

## How to configure

- Clone this repository
    - ```git clone <github repo url>```
- install dependencies
    - ```pip3 install -r requirements.txt```

## How to Run

- execute ```crawler.py```
    - ```python3 crawler.py```

## How to Test 

- Run pytest
    - ```pytest```
## Contributors list

1. John Abraham - dravog7
2. (Add your name and Github Id)
