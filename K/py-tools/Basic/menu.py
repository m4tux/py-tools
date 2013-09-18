
# This is the menu!!!
print '...welcome...'
print 
print '1. Chapter 1'
print '2. Chapter 2'
print '3. Chapter 3'
print '4. Chapter 4'
print '5. Quit '
print

a = raw_input ('Choose a number from the menu and please press return on your keyboard to continue: ')

def my_menu(a):
        
    print 
    a=input ('please enter the figure that represents what you want to do: ')
    print
    if a == 1:
        #chap1 funciton here 
        a1 = raw_input('Do you want to enter another module, y or n: ')
        print
        while a1 == 'y':
            print raw_input('Please enter your module name: ')
            a1 = raw_input('Do you want to enter another module, y or n: ')
            print                            
    elif a == 2:
        print 'You have choosen to enter your module marks'
        print
        print input('Please enter your module mark: ')
        
    elif a == 3:
        print 'You have choosen find the mean of ur module marks'
        print
        
    elif a == 4:
        print 'You have choosen find the mean of ur module marks'
        print
        
    elif a == 5:
        print 'You have choosen to quit '
        print
        print '......GOODBYE......'
        return
    else:
        print 'That is not part of the menu!!!'
        print
    x = raw_input ('Do you want to perform another task from the menu? y or n: ')
    if x == 'y':
        my_menu(a)
    else: 
        print '......GOODBYE......'
        return

my_menu(a)


