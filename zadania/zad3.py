# coding=utf-8     
'''''
Created on 21 lut 2018  
  
@author: Daniel  
'''    
    
if __name__ == '__main__':  
      
    def isArmstrong (n):    #Definiujemy funkcj�, kt�ra sprawdzi nam czy dana liczba jest liczb� Armstronga  
      
        noOfNumbers = len(str(n)) #liczymy ile podana liczba ma cyfr  
        listOfDigits =[]  
        for char in str(n):   #ka�d� z cyfr  umieszczamy  w tablicy (liscie) jako string
            listOfDigits.append(char)   
        for i in range(0,noOfNumbers):  # ka�d� z cyfr, zamieniamy ze stringa na int, podnosimy do pot�gi r�wnej ilo�ci cyfr i umieszczamy w tym samym miejscu na li�cie   
            listOfDigits[i] = pow(int(listOfDigits[i]), noOfNumbers)  
            i = i + 1  
        if n == sum(listOfDigits):  #sprawdzamy czy podana liczba (n) r�wna si� sumie element�w (cyfr) listy  
            print ("{0} is Armstrong".format(n))  
            return  
        
    i = 0  
    while True:  #Uruchamiamy program w nieko�cz�cej si� p�tli   
        isArmstrong(i)  
        i = i + 1  
