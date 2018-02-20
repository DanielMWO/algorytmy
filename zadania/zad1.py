# coding=utf-8  
''''' 
Created on 19 lut 2018 
 
@author: Daniel 
'''  
import codecs  
  
if __name__ == '__main__':  
      
    #Otwieramy plik, do odczytu, z odpowiednim kodowaniem, wczytujemy cały plik jako String.   
    f = codecs.open('pantadeusz.txt', 'r', 'UTF-8')                      
    text = f.read()  
    f.close()  
      
    # Ze stringa usuwamy znaki interpunkcyjne i zamieniamy wszystkie litery na małe. Po to by  "Dobranoc!" było tym samym co "dobranoc"  
    znaki = ['!' , '(' , ')' , ';' , ':' , '"' , "'" , ',' , '.', '-']   
    for each in znaki:  
        text = text.replace(each, "").lower()  
    slowa = text.split()  
    
    
    #Usuwamy  z listy pojedyncze  litery (Pojedycze litery też są słowami ale tak jest ciekawiej)
    spojniki = 'iwzao'
    for char in spojniki:
        n = slowa.count(char)
        for i in range (0,n):
            slowa.remove(char)
      
    #Korzystając ze słownika (dict), Dodajemy do niego kolejne słowa jako klucze z wartością 1, jeżeli słowo już w nim jest zwiększamy wartość o 1   
    zliczak = {}  
    for each in slowa:  
        if each in zliczak:  
            zliczak[each] = zliczak[each] + 1  
        else:  
            zliczak[each] = 1  
          
    #Sortujemy  słownik po wartościach (od największej do najmniejszej), Otrzymaną listę przycinamy do 20 pierwszych elementów = daje nam to liczbę  wystąpień każdego z 20 najczęstszych słów  
    top20lista =  (sorted(zliczak.values(), reverse=True)[0:19])  
         
    #Sprawdzamy słownik dla każdej wartości z listy top 20, i wypisujemy parę klucz wartość.  
    for each in top20lista:  
        for  k, v in zliczak.items():  
            if zliczak[k] == each:  
                print (k,v)  