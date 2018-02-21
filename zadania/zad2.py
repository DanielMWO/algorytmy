# coding=utf-8   
''''' 
Created on 21 lut 2018 
 
@author: Daniel 
'''  
import sys  
sys.setrecursionlimit(1000)  # To pozwala nam zwiększyć liczbę możliwych wywołań rekurencyjnych (do momentu aż skończy się pamięć)  
  
  
if __name__ == '__main__':  
   
  
    #Definiujemy funkcje do sprawdzania czy coś jest Palindromem,  Funkcja operuje na stringach (zamiast np na listach) bo python pozwala na takie cuda  
    def isPalindrom (n):  
        assert type(n) == int  
        a = str(n)   # zmieniamy integer na string    
        b = a[::-1]  # odwracamy string   
        n2 = int(b)  # zamieniamy odwrócony string na integer   
        if a == b:     
            return b  # zwracamy string jeżeli jest Palindromem  
        else:  
            return isPalindrom(n+n2) # jeśli nie jest powtarzamy operację dla sumy  dwóch liczb jako parametru      
       
    for i in range(1,201):  # wykonujemy funkcję w pętli dla zadanego przedziału i drukujemy wyniki   
        try:  
            print ("for {0} the palindorm is {1}".format(i, isPalindrom(i)))  
              
        except (RecursionError):  
            print ("Sorry not enough memory to calculate palindrom for {0} - skipping ".format(i))  ## obsługujemy wyjątek w przypadku gdy przekroczymy dopuszczalną przez system liczbę rekurencji  
            continue  