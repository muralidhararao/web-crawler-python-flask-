from flask import Flask
import urllib2
from bs4 import BeautifulSoup  

app = Flask(__name__)

@app.route("/ndtv")
def hello():
    try:
        page = urllib2.urlopen("https://www.ndtv.com/india?pfrom=home-topnavigation")
        soup = BeautifulSoup(page,'html.parser')
        aray=[]
        if soup:
          for divdata in soup.findAll("div", { "class" : "new_storylising" }):
              for liinfo in divdata.findAll("li"):
                aray.append(liinfo)
        return str(aray)
    except urllib2.HTTPError, err:
         if err.code == 404:
           return "Page not found!"
         elif err.code == 403:
           return "Access denied!"+str(err.fp.read())
         else:
           print "Something happened! Error code", err.code
    except urllib2.URLError, err:
       return "Some other error happened:", err.reason


if __name__ == "__main__":
    app.run()


