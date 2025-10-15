
"""
Created on Wed Feb 14 09:50:43 2024
@author: jokane
"""

print('-----------------------------------------')
print()
print('Eksamen høst 2023, del 2 oppgave 7:')
print('En bedrift vil redusere utslippet av et\nforurenset stoff med 5% hvert år framover. \n'
      'I år er utslippet på 40 tonn')
print('a) Vis at det samlede utslippet i år og de to neste årene vil bli på 114,1 tonn:')
print('b) Lag et program du kan bruke for å bestemme det samlede utslippet for \n'
      'denne bedriften over svært lang tid.')
# sett inn programmet ditt her :) 
print('c) Undersøk sammenhengen mellom utslippet i år og \n'
      'det samlede utslippet over svært lang tid. ')
print()
print('Ole påstår at T = 100* u/p er en formel for å regne ut det samlede utslippet T \n'
      'når utslippet i år er u og utslippet reduseres med p% hvert år framover. \n'
      'd) Undersøk om denne sammenhengen kan gjelde.')
 
print()  
''' Løsning:
    reduksjon = 0.95 # årlig reduksjon 5%
    utslipp = 40
    totalUtslipp=utslipp
    print('Utslipp år 1:',utslipp)
    for i in range (10):
        utslipp *= reduksjon
        totalUtslipp += utslipp
        print('Utslipp år',i+2,':',utslipp)
        print('Totalt:',totalUtslipp)
'''
print('-----------------------------------------')
print()

print('Eksamen vår 2023, del 2 oppgave 6:')   
print('I august 2022 satte elevene i 3PBB seg som mål å samle inn tomflasker for 25 000 kroner før 1. juni 2023.')
print('De brukte funksjonen gitt ved: P(x)=1600*1,045**x, 0<=x<=9\n'
      'som en modell for hvor stort beløp i kroner de måtte samle inn hver måned\n'
      'for å nå målet. ')
print('a) Gjør rede for hva modellen forteller om elevenes plan for å nå målet.')
print('b) Hvor stort beløp regnet elevene med å samle inn i mai 2023 ifølge modellen?\n'
      'Elevene laget programmet nedenfor (se i koden, ikke i outputen her).')

def P(x):
    return 1600*1.045**x
sum_pant=0
x=0
while x <= 9:
    sum_pant+=P(x)
    x+=1

print('Pantesummen til slutt:',sum_pant)
print()
print('c) Bruk programmet til å vise at elevene ikke vil nå målet med den planen de har\n'
      'lagt. Foreslå justeringer av modellen som vil gjøre at de kan nå målet.')
print()
print('-----------------------------------------')



