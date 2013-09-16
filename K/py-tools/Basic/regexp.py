import re

print "*****************************            REGULAR EXPRESSION            ***************************"


def reghelp():
    f = open("regexp.help","r")
    contents = f.read()
    print contents
    
  
reghelp()

print "****************************************************************************************************"

print "****************************************example 1*********************************************"

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
  print match.group()   ## 'alice-b@google.com' (the whole match)
  print match.group(1)  ## 'alice-b' (the username, group 1)
  print match.group(2)  ## 'google.com' (the host, group 2)
  
  
  
print "****************************************example 2*********************************************"

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"
   
print "****************************************example 3 sub function (replace)*********************************************"

phone = "2004-959-559 # This is Phone Number"
print "string is : ",phone
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num

