
print "******************************************************************************************"
print "************************         Chapter 5 Internet Data  *********************************"
print "******************************************************************************************"

import urllib2

def kkkk():
  # open a connection to a URL using urllib2
  webUrl = urllib2.urlopen("http://joemarini.com")
  
  # get the result code and print it
  print "result code: " + str(webUrl.getcode())
  
  # read the data from the URL and print it
  data = webUrl.read()
  print data

kkkk()

print "*****            --- JSON data ---           *****"


import urllib2
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
    print theJSON["metadata"]["title"]
  
  # output the number of events, plus the magnitude and each event name  
  count = theJSON["metadata"]["count"];
  print str(count) + " events recorded"
  
  # for each event, print the place where it occurred
  for i in theJSON["features"]:
    print i["properties"]["place"]

  # print the events that only have a magnitude greater than 4
  for i in theJSON["features"]:
    if i["properties"]["mag"] >= 4.0:
      print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]

  # print only the events where at least 1 person reported feeling something
  print "Events that were felt:"
  for i in theJSON["features"]:
    feltReports = i["properties"]["felt"]
    if (feltReports != None) & (feltReports > 0):
      print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times"



  # Open the URL and read the data
  webUrl = urllib2.urlopen(urlData)
  print webUrl.getcode()
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out our customized results
    printResults(data)
  else:
    print "Received an error from server, cannot retrieve results " + str(webUrl.getcode())



print "*****           --- HTML ---           *****"


# import the HTMLParser module
from HTMLParser import HTMLParser

metacount = 0;

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
  # function to handle an opening tag in the doc
  # this will be called when the closing ">" of the tag is reached
  def handle_starttag(self, tag, attrs):
    global metacount
    print "Encountered a start tag:", tag
    if tag == "meta":
      metacount += 1
      
    pos = self.getpos() # returns a tuple indication line and character
    print "At line: ", pos[0], " position ", pos[1]
    if attrs.__len__ > 0:
      print "\tAttributes:"
      for a in attrs:
        print "\t", a[0],"=",a[1]
      
  # function to handle the ending tag
  def handle_endtag(self, tag):
    print "Encountered an end tag:", tag
    pos = self.getpos()
    print "At line: ", pos[0], " position ", pos[1]
    
  # function to handle character and text data (tag contents)
  def handle_data(self, data):
    print "Encountered some data:", data
    pos = self.getpos()
    print "At line: ", pos[0], " position ", pos[1]
  
  # function to handle the processing of HTML comments
  def handle_comment(self, data):
    print "Encountered comment:", data
    pos = self.getpos()
    print "At line: ", pos[0], " position ", pos[1]



  # open the sample HTML file and read it
  f = open("samplehtml.html")
  if f.mode == "r":
    contents = f.read() # read the entire file
    parser.feed(contents)
  
  print "%d meta tags encountered" % metacount


print "*****           --- XML ---          *****"


import xml.dom.minidom

def main():
  # use the parse() function to load and parse an XML file
  doc = xml.dom.minidom.parse("samplexml.xml");
  
  # print out the document node and the name of the first child tag
  print doc.nodeName
  print doc.firstChild.tagName
  
  # get a list of XML tags from the document and print each one
  skills = doc.getElementsByTagName("skill")
  print "%d skills:" % skills.length
  for skill in skills:
    print skill.getAttribute("name")
    
  # create a new XML tag and add it into the document
  newSkill = doc.createElement("skill")
  newSkill.setAttribute("name", "jQuery")
  doc.firstChild.appendChild(newSkill)

  skills = doc.getElementsByTagName("skill")
  print "%d skills:" % skills.length
  for skill in skills:
    print skill.getAttribute("name")

