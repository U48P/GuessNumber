from random import Random
import unittest

import testclass





random = Random()

#kollar om det ingår mellan
def getnumber(o, p):
    # generate integer between 15 and 99
    # return random.randint(15, 17)
    return random.randint(o, p)


# kollar hur många tal som finns 5
def length(a,b):
    c = abs(a-b)
    return c

# vilka tal som finns som kan skrivas ut
def potentialnumbers(s,n):
    d =[*range(s,n)]
    return d


# kollar om det om ett nummber finns med
def numbers(a):

    r = [1,2,3,4,5]
    if a in r:
        return True

def initialize():
    print("Testable functions are being initialized")

def cleanUp():
    print("Cleaning up ...")