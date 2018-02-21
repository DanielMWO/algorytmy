# coding=utf-8     
'''''
Created on 21 lut 2018  
  
@author: Daniel  
'''    
    
if __name__ == '__main__':  
      
    def isArmstrong (n):    #Definiujemy funkcjê, która sprawdzi nam czy dana liczba jest liczb¹ Armstronga  
      
        noOfNumbers = len(str(n)) #liczymy ile podana liczba ma cyfr  
        listOfDigits =[]  
        for char in str(n):   #ka¿d¹ z cyfr  umieszczamy  w tablicy (liscie) jako string
            listOfDigits.append(char)   
        for i in range(0,noOfNumbers):  # ka¿d¹ z cyfr, zamieniamy ze stringa na int, podnosimy do potêgi równej iloœci cyfr i umieszczamy w tym samym miejscu na liœcie   
            listOfDigits[i] = pow(int(listOfDigits[i]), noOfNumbers)  
            i = i + 1  
        if n == sum(listOfDigits):  #sprawdzamy czy podana liczba (n) równa siê sumie elementów (cyfr) listy  
            print ("{0} is Armstrong".format(n))  
            return  
        
    i = 0  
    while True:  #Uruchamiamy program w niekoñcz¹cej siê pêtli   
        isArmstrong(i)  
        i = i + 1  
