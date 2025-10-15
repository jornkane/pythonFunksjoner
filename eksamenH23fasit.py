
print('Eksamen høst 2023, del 2 oppgave 7:')
print('En bedrift vil redusere utslippet av et\nforurenset stoff med 5% hvert år framover.\nI år er utslippet på 40 tonn')
print('a) Vis at det samlede utslippet i år og de to neste årene vil bli på 114,1 tonn:')

import os
os.system('cls' if os.name == 'nt' else 'clear')

reduksjon = 0.95  # årlig reduksjon 5%
utslipp = 40
totalUtslipp = utslipp
print('Utslipp år 1:', round(utslipp, 1))  # Avrunder til én desimal
for i in range(10):
    utslipp *= reduksjon
    totalUtslipp += utslipp
    print('Utslipp år', i + 2, ':', round(utslipp, 1))  # Avrunder til én desimal
    print('Totalt:', round(totalUtslipp, 1))  # Avrunder til én desimal
print('-----------------------------------------')


print('Eksamen vår 2023, del 2 oppgave 6:')
print('I august 2022 satte elevene i 3PBB seg som mål å samle inn \n'
      'tomflasker for 25 000 kroner før 1. juni 2023.')
print('Funksjonen: P(x)=1600*1,045**x, 0<=x<=9')
def P(x):
    return 1600 * 1.045**x
sum_pant = 0
x = 0
while x <= 9:
    sum_pant += P(x)
    x += 1
print('Pantesummen til slutt:', round(sum_pant),'kr')  # Avrunder til én desimal
print('-----------------------------------------')

