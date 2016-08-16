#!/usr/bin/python 

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def f_one ():
    print "You have selected option one."

def f_two ():
    print "You have selected option two."

def f_three ():
    print "You have selected option three."


# create option menu from which to pick from
def menu ():
    print "1.) Test 1"
    print "2.) Test 2"
    print "3.) Test 3"
    print
    v = raw_input("Which option? (1,2,3): ")

    for case in switch(v):
        if case('1'):
            f_one()
            break
        if case('2'):
            f_two()
            break
        if case('3'):
            f_three()
            break
        if case(): # default, could also just omit condition or 'if True'
            print "You didn't select a valid option!"
            menu()

menu()
