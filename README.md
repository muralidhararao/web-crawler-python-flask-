# web-crawler-python-flask-
Web Crawler sample with Python Flask using Beautiful Soup

Web crasler/Spider using Beautiful Soup as a Python Flask Web application<br>

<h4>Flask installation:</h4> (http://flask.pocoo.org/docs/0.12/installation/)

$pip install Flask

<h4>Beautiful Soup installation:</h4>

$pip install BeautifulSoup4

<h4>Imports:</h4>

from flask import Flask<br>
import urllib2<br>
from bs4 import BeautifulSoup  <br>

<h4> Do best Practice with Try... blocks</h4>

try:<br>
       ...... <br>
    except urllib2.HTTPError, err:<br>
	
<h4>Open a URL with urllib2:</h4>

page = urllib2.urlopen("https://.....")<br>

<h4>Make a soup with html.parser</h4>

soup = BeautifulSoup(page,'html.parser')

<h4>Filter with tags or class names</h4>

for links in soup.findAll("a"):
	aray.append(links.href)

 <a href="https://github.com/muralidhararao/web-crawler-python-flask-/blob/master/web-crawler.py">Get code from</a>
