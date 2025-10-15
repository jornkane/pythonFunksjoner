# -*- coding: utf-8 -*-
"""Created on Tue Dec  8 11:00:32 2020. @author: jornkane
"""
print('Dette er et program der du kan lage egen verditabell\n'
      'for funksjonen f(x)= x**2 + 3*x − 1, du legger inn x-verdier\n'
      'programmet finner f(x) og skriver ut tabellen :)') 
x=[]
y=[]
fortsett = int(input('Hvor mange x-verdier vil du legge inn? '))
slutt = 0
while slutt < fortsett:
    x.append(float(input('Skriv inn ny x-verdi: ')))
    slutt +=1

for i in x:
    y.append(i**2 + 3*i - 1)

print('----------------------------------------')
print('Da ser verditabellen slik ut:')
print('X-verdier',x,'Y-verdier',y)

print('----------------------------------------')
print()
for a in range(len(x)):
    print (f'x-verdi',x[a],'gir y-verdi',y[a])
 













