'''
Created on 19 lut 2018

@author: Daniel
'''
import codecs

if __name__ == '__main__':
    
    f = codecs.open('pantadeusz.txt', 'r', 'UTF-8')
    data = f.read()
    f.close()
    znaki = ['!' , '(' , ')' , ';' , ':' , '"' , "'" , ',' , '.', '-']
    for each in znaki:
        data = data.replace(each, "").lower()
     
    
    slowa = data.split()
    #print (slowa)
     
    
    
    zliczak = {}
    for each in slowa:
        if each in zliczak:
            zliczak[each] = zliczak[each] + 1
        else:
            zliczak[each] = 1
      
    
    lista =  (sorted(zliczak.values(), reverse=True)[0:19])
    print (type(lista)) 
    print (lista)
       
    
    for each in lista:
        for  k, v in zliczak.items():
            if zliczak[k] == each:
                print (k,v)

    pass