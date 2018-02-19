'''
Created on 19 lut 2018

@author: Daniel
'''
import codecs

if __name__ == '__main__':
    
    f = open('pantadeusz.txt')
    data = f.read()
    f.close()
    slowa = data.split()
     
    
    
    zliczak = {}
    for each in slowa:
        if each in zliczak:
            zliczak[each] = zliczak[each] + 1
        else:
            zliczak[each] = 1
      
    # Reversle zliczak jest do bani  bo usuwa podwójne wpisy, trzeba odczytac max a potem znaleœæ petla 20 mniejsztcg 
    reverse_zliczak = () 
    for  k, v in zliczak.iteritems():
        reverse_zliczak[v[k]]
           
    counter = sorted(reverse_zliczak, reverse=True)
    
    for each in counter:
        print reverse_zliczak[each]
     
    print len(reverse_zliczak)   
    #print data
    
    pass