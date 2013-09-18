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
def Tvar():
    print "***********************   Chapter 2 : STRINGS !   ***************************"

    output = 0;
    print output
    # re-declaring the variable works
    output = "abc"
    print output
    # ERROR: different types cannot be combined
    #print "string type " + 123 
    #so we use str function to convert it to a strings variable
    print "string type " #+ str(123)
    # Global vs. local variables in functions
    
    #string methods
    # get some code from here  ! http://www.tutorialspoint.com/python/python_strings.htm -> browse methods below xD 
    #http://docs.python.org/2/library/string.html
    #
    
   
    
    #Accessing Values in Strings: 
    
    var1 = 'Hello World!'
    var2 = "Python Programming"
    
    print "var1[0]: ", var1[0]
    print "var2[1:5]: ", var2[1:5]
    
    #Updating Strings:
    
    var1 = 'Hello World!'
    print var1
    print "Updated String :- ", var1[:6] + 'Python'
    
    
    #String Formatting Operator:
    
    
    print "My name is %s and weight is %d kg!" % ('Zara', 21) 
    
    
    #Python String capitalize() Method
    str = "this is string example....wow!!!";
    print str
    print "str.capitalize() : ", str.capitalize()
    #Python String center() Method
    str = "this is string example....wow!!!";
    print "str.center(40, 'a') : ", str.center(40, 'a')
    #Python String count() Method
    str = "this is string example....wow!!!";
    sub = "i";
    print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
    sub = "wow";
    print "str.count(sub) : ", str.count(sub)
    #Python String isalnum() Method
    print r"This method returns true if all characters in the string are alphanumeric and there is at least one character, false otherwise."
    str = "this2009";  # No space in this string
    print str.isalnum();
    str = "this is string example....wow!!!";
    print str.isalnum();
    #Python String isAlpha() method 
    print r"This method returns true if all characters in the string are alphabetic and there is at least one character, false otherwise."
    str = "this";  # No space & digit in this string
    print str.isalpha();
    str = "this is string example....wow!!!";
    print str.isalpha();
    #Python String join() Method
    print r"The method join() returns a string in which the string elements of sequence have been joined by str separator."
    str = "-";
    seq = ("a", "b", "c"); # This is sequence of strings.
    print str.join( seq );
    #Python String len() Method
    print r"The method len() returns the length of the string."
    str = "this is string example....wow!!!";
    print "Length of the string: ", len(str);
    #Python String lstrip() Method
    print r"The method lstrip() returns a copy of the string in which all chars have been stripped from the beginning of the string (default whitespace characters)."
    str = "     this is string example....wow!!!     ";
    print str.lstrip();
    str = "88888888this is string example....wow!!!8888888";
    print str.lstrip('8');
    
    
    
    #str.find(str, beg=0 end=len(string))
    print r"str.find"
    str1 = "this is string example....wow!!!";
    str2 = "exam";
    
    print str1.find(str2);
    print str1.find(str2, 10);
    print str1.find(str2, 40);
    
    # Split function
    a = "ok test aka you motherfucker!"
    print a.split()
    
    # you can find other strings methods in http://www.tutorialspoint.com/python/python_strings.htm
    def someFunction():
      #global output
      output = "def"
      print output
    
    someFunction()
    print output 
    del output 
    output = 'ok'
    print output
    
    print "***********************   Chapter 2 : LIST !   ***************************"
    #http://docs.python.org/2/tutorial/datastructures.html
    #get some code from here : http://www.tutorialspoint.com/python/python_lists.htm
    
    #Accessing Values in Lists:
    
    list1 = ['physics', 'chemistry', 1997, 2000];
    list2 = [1, 2, 3, 4, 5, 6, 7 ];
    print "list1[0]: ", list1[0]
    print "list2[1:5]: ", list2[1:5]
    
    
    #Updating Lists:
    list = ['physics', 'chemistry', 1997, 2000];
    print "Value available at index 2 : "
    print list[2];
    list[2] = 2001;
    print "New value available at index 2 : "
    print list[2];
    
    #Delete List Elements:
    list1 = ['physics', 'chemistry', 1997, 2000];
    
    print list1;
    del list1[2];
    print "After deleting value at index 2 : "
    print list1;
    
    #Python includes the following list functions:
    
    #Python List cmp() Method
    print r"The method cmp() compares elements of two lists."
    
    list1, list2 = [123, 'xyz'], [456, 'abc']

    print cmp(list1, list2);
    print cmp(list2, list1);
    list3 = list2 + [786];
    print cmp(list2, list3)
        
    
    #Python List len() Method
    print r"The method len() returns the number of elements in the list."
    list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']
    
    print "First list length : ", len(list1);
    print "Second list length : ", len(list2);

    #Python List max() Method
    print r"The method max returns the elements from the list with maximum value."
    
    list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]
    
    print "Max value element : ", max(list1);
    print "Max value element : ", max(list2);
    
    #Python List min() Method
    print r"The method min() returns the elements from the list with minimum value."
    
    list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]

    print "min value element : ", min(list1);
    print "min value element : ", min(list2);
    
    
    #Python List list() Method
    print r"The method list() takes sequence types and converts them to lists. This is used to convert a given tuple into list."
    
    aTuple = (123, 'xyz', 'zara', 'abc');
    #aList = list(aTuple)
    
    print "List elements : ", aTuple   #aList
    
    
    
    #Python includes following list methods
    
    
    #Python List append() Method
    print r"The method append() appends a passed obj into the existing list."
    
    
    aList = [123, 'xyz', 'zara', 'abc'];
    aList.append( 2009 );
    print "Updated List : ", aList;
    
    
    #Python List count() Method
    print r"The method count() returns count of how many times obj occurs in list."
    
    
    aList = [123, 'xyz', 'zara', 'abc', 123];
    
    print "Count for 123 : ", aList.count(123);
    print "Count for zara : ", aList.count('zara');
        
    #Python List extend() Method
    print r"The method extend() appends the contents of seq to list."
    
    
    
    aList = [123, 'xyz', 'zara', 'abc', 123];
    bList = [2009, 'manni'];
    aList.extend(bList)
    
    print "Extended List : ", aList ;
    
    
    
    #Python List index() Method
    print r"The method index() returns the lowest index in list that obj appears."
    
    aList = [123, 'xyz', 'zara', 'abc'];
    
    print "Index for xyz : ", aList.index( 'xyz' ) ;
    print "Index for zara : ", aList.index( 'zara' ) ;
    
    
    
    
    
    #Python List insert() Method
    print r"The method insert() inserts object obj into list at offset index."
    aList = [123, 'xyz', 'zara', 'abc']
    aList.insert( 3, 2009)
    print "Final List : ", aList
    
    
    
    #stack operations 
    #Python List pop() Method
    
    print r"The method pop() removes and returns last object or obj from the list."
    
    aList = [123, 'xyz', 'zara', 'abc'];

    print "A List : ", aList.pop();
    print "B List : ", aList.pop(2);
    
    
    #Python List remove() Method
    print r"The method remove() removes first obj from the list."    
    
    aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

    aList.remove('xyz');
    print "List : ", aList;
    aList.remove('abc');
    print "List : ", aList;
    
    
    #Python List reverse() Method
    print r"The method reverse() reverses objects of list in place."
    
    aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
    aList.reverse();
    print "List : ", aList;
    
    #Python List sort() Method
    #for review to get a look about the func parameter
    print r"The method sort() sorts objects of list, use compare func if given."
    
    aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

    aList.sort();
    print "List : ", aList;
    
    
# ---Functions---
def Tfunction():
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
def TCond():
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
def Tloops():
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
def Tclass():
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
    
    
def TDates():
            
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
    d = str(datetime.now())
    # print today's date
    print "today is: " + d
    
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
    
    

# here we must write a menu for our applications !!!

# This is the menu!!!
print '...welcome...'
print '1. Chapter 1'
print '2. Chapter 2'
print '3. Chapter 3'
print '4. Chapter 4'
print '5. Quit '
print

def my_menu():
    a=input ('please enter the chapter number that you want to learn: ')
    if a == 1:
        Tvar()
    elif a == 2:
        Tfunction()
    elif a == 3:
        TCond()
    elif a == 4:
        Tloops()
    elif a == 5:
        Tclass()
    elif a == 6:
        print 'You have choosen to quit '
        print '......GOODBYE......'
        return
    else:
        print 'That is not part of the menu!!!'
    x = raw_input ('Another task from the menu? y or n: ')
    if x == 'y':
        my_menu()
    else: 
        print '......GOODBYE......'
        return

my_menu()

# TDates()   str used before & must be replaced o0 ? wtf
# end here 