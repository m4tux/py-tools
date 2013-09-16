import __main__

print "***********************   chapter 1 Hello World!   ****************************"

def main():
    print "hello world !"

#calling main function
print __name__ 
if __name__ == "__main__": 
    main()
#                                        --- Variables ---    
# Declaring variables and using Them ,Declare a variable and initialize it

print "***********************   Chapter 2 : Variables !   ***************************"

output = 0;
print output
# re-declaring the variable works
output = "abc"
print output

# ERROR: different types cannot be combined
#print "string type " + 123 
#so we use str function to convert it to a strings variable
print "string type " + str(123)

# Global vs. local variables in functions
def someFunction():
  #global output
  output = "def"
  print output

someFunction()
print output 


del output 
output = 'ok'
print output
# ---Functions---

print "***********************   Chapter 2 : Functions !   ***************************"

print "----  define a function    ---"
def func1():
  print "I am a function"
func1()
print func1()
print func1


print "---- function that takes arguments ---"
def func2(arg1, arg2):
  print arg1, " ", arg2


func2(10,20)
print func2(10,20)
print "--------- function that returns a value   ---------"
def cube(x):
    print x 
    return x*x*x

print cube(3)


print "----- function with default value for an argument ----- "
def power(num, x=1):
  result = 1;
  for i in range(x):
    result = result * num  
  return result


print power(2)
print power(2,3)
print power(x=3, num=2)


print "----- function with variable number of arguments ------"
def multi_add(*args):
  result = 0;
  for x in args:
    result = result + x
  return result

print multi_add(4,5,10,4)


#--- Conditionals ---
print "*******************************            Chapter 2 : Conditionnals            *****************************"

print "--------- conditional flow uses if, elif, else  -----------------"  
def condflow(x,y):
    if(x < y):
      st= "x is less than y"
    elif (x == y):
      st= "x is same as y"
    else:
      st= "x is greater than y"
    print st

condflow(10, 100)
def condone(x,y):
    print "---------- conditional statements let you use \"a if C else b --------------------"
    st = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print st
condone(100, 10)


# switch .... case here + menu  // do not exist o0 wtf ?

print "*******************************            Chapter 2 : Loops            *****************************"
x=0
print "---    define a while loop    ---"
while (x < 5):
   print x
   x = x + 1

print "---    define a for loop    ---"
for x in range(5,10):
  print x

  
print "---    use a for loop over a collection    ---"
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for d in days:
  print d

print "---    use the break and continue statements    ---"
for x in range(5,10):
  #if (x == 7): break
  #if (x % 2 == 0): continue
  print x

print "---    using the enumerate() function to get index    ---"
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for i, d in enumerate(days):
  print i, d

#--- Classes ---
print "*********************************        Chapter 2 : CLasses            *****************************"

class myClass():
  def method1(self):
    print "myClass method1"
    
  def method2(self, someString):
    print "myClass method2: " + someString
    
class anotherClass(myClass):
  def method2(self):
    print "anotherClass method2"
    
  def method1(self):
    myClass.method1(self);
    print "anotherClass method1"

    # exercise the class methods
c = myClass()
c.method1()
c.method2("This is a string")
c2 = anotherClass()
c2.method1()



print "******************************************************************************************"
print "************************            Chapter 3            *********************************"
print "******************************************************************************************"



print "************************            Dates            **************************************"



from datetime import date
from datetime import time
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
print "Today's date is ", today

# print out the date's individual components
print "Date Components: ", today.day, today.month, today.year

# retrieve today's weekday (0=Monday, 6=Sunday)
print "Today's Weekday #: ", today.weekday()

## DATETIME OBJECTS
# Get today's date from the datetime class
today = datetime.now()
print  "The current date and time is ", today;

# Get the current time
t = datetime.time(datetime.now())
print "The current time is ", t

# weekday returns 0 (monday) through 6 (sunday)
wd = date.weekday(today)  
# Days start at 0 for Monday 
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print "Today is day number %d" % wd
print "Which is a " + days[wd]


print "***********************            Formatting            ****************************"

# Times and dates can be formatted using a set of predefined string
# control codes 
now = datetime.now() # get the current date and time

#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print now.strftime("%Y") # full year with century
print now.strftime("%a, %d %B, %y") # abbreviated day, num, full month, abbreviated year

# %c - locale's date and time, %x - locale's date, %X - locale's time
print now.strftime("%c")
print now.strftime("%x")
print now.strftime("%X")

#### Time Formatting ####

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print now.strftime("%I:%M:%S %p") # 12-Hour:Minute:Second:AM
print now.strftime("%H:%M") # 24-Hour:Minute

print "**************************            Timedeltas            **************************************"

from datetime import timedelta

# construct a basic timedelta and print it
print timedelta(days=365, hours=5, minutes=1)

# print today's date
print "today is: " + str(datetime.now())

# print today's date one year from now
print "one year from now it will be: " + str(datetime.now() + timedelta(days=365))

# create a timedelta that uses more than one argument
print "in two weeks and 3 days it will be: " + str(datetime.now() + timedelta(weeks=2, days=3))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print "one week ago it was " + s

### How many days until April Fools' Day?

today = date.today()  # get today's date
afd = date(today.year, 4, 1)  # get April Fool's for the same year
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
  print "April Fool's day already went by %d days ago" % ((today-afd).days)
  afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# Now calculate the amount of time until April Fool's Day  
time_to_afd = abs(afd - today)
print time_to_afd.days, "days until next April Fools' Day!"


print "*******************************            Calendars            ********************************"

import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2013, 1, 0, 0)
print str

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2013, 1)
print str

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2013, 8):
  print i
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
  print name

for day in calendar.day_name:
  print day

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
for m in range(1,13):
  # returns an array of weeks that represent the month
  cal = calendar.monthcalendar(2013, m)
  # The first Friday has to be within the first two weeks
  weekone = cal[0]
  weektwo = cal[1]
   
  if weekone[calendar.FRIDAY] != 0:
    meetday = weekone[calendar.FRIDAY]
  else:
    # if the first friday isn't in the first week, it must be in the second
    meetday = weektwo[calendar.FRIDAY]
      
  print "%10s %2d" % (calendar.month_name[m], meetday)


