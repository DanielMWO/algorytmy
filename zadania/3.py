# coding=utf-8   
''''' 
Created on 21 lut 2018 
 
@author: Daniel 
'''  
  
if __name__ == '__main__':
    
    def isArmstrong (n):    #Definiujemy funkcje, która sprawdzi nam czy dana liczba jest liczbą Armstronga
    
        noOfNumbers = len(str(n)) #liczymy  podana liczna ma cyfr
        listOfDigits =[]
        for char in str(n):   #kazda z cyfr  umieszczamy  w tablcy (liscie) (jako string)
            listOfDigits.append(char) 
        for i in range(0,noOfNumbers):  # każdą z cyfr, zamieniamy ze stringa na int  podnosimy do potęgi rówej lośći cyfr i umieszzamy w tym samym miejscy na liscie 
            listOfDigits[i] = pow(int(listOfDigits[i]), noOfNumbers)
            i = i + 1
        if n == sum(listOfDigits):  #sprawdzamy czy podana liczna równa się sumie elementów (cyfr) listy
            print ("{0} is Armstrong".format(n))
            return
      
    i = 0
    while True:  #Uruchamiamy program w niekończoncej się pętli 
        isArmstrong(i)
        i = i + 1