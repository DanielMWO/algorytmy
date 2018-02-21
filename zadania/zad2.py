# coding=utf-8 
'''
Created on 21 lut 2018

@author: Daniel
'''

import sys
sys.setrecursionlimit(10000000)

if __name__ == '__main__':
    #defninujemy funkcje do zamiany miejscami  cyfr w lciznie
    #def reverseOrder (int):
        
    print (9//10)
        
    # Denfiniujemy funkcje do sprawdzania czy czy coś jest palindormem
    def isPalindrom (n):
        assert type(n) == int
        if (1):
            a = str(n)
            b = a[::-1]
            n2 = int(b)
            if a == b:
                print (" the palindrom is " + b) 
            else:
                isPalindrom(n+n2)
    isPalindrom(200) 
    
    
     
    for i in range(1,200):
        print ("for" + str(i))
        isPalindrom(i)
        