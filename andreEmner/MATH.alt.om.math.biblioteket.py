"""
Created on Sun Oct  4 16:59:30 2020
@author: Jørn Kanestrøm
Alt hentet fra: https://realpython.com/python-math-module/#getting-to-know-the-python-math-module 
"""
import math

pi = math.pi
tau = math.tau # det dobbelte av pi
e = math.e 
inf = math.inf 
nan = math.nan # not a number. Dett skal kunne brukes for å
    # sikre at input feks har riktig verdi
r = 3.5
z = 1e308 # 10 opphøyd i 308 - høyeste floating point number

print()
print('Funksjoner av typen potens, eksponential og kvadratrot: ')
print('Potensfunksjoner: ')
print('2 opphøyd i 5:',(math.pow(2, 5)))
print('5 opphøyd i 2,4:',(math.pow(5, 2.4)))
print('0 i nullte:',(math.pow(0.0, 0.0)))
# du kan også bruke pow(a, b, evt c) uten math. Mer om det nederst i dokumentet
print()
print('Eksponentialfunksjoner (f(x) = a**x')
print('Den naturlige eksponentialfunksjonen e**x, med x = 3:',(math.exp(3))) 
print('---') 
print('Praktisk eksempel på bruk av exp:')
print('Radioaktiv halverintstid')
print('Om du har 100 milligram Strontium-90 med halveringstid på 38,1 år,\n'
      'Har du etter 100 år så mye: ')
half_life = 38.1
initial = 100
time = 100
remaining = initial * math.exp(-0.693 * time / half_life)
print(f'Gjenstående mengde av Sr-90: ca. {round (remaining,2)} milligram') 
    # Formel N(t) =  N(0) * e**(-693t / T) 
    # N(0) er utgangsmengde og N(t) er det som gjenstår. T er halveringstid og e er Eulers tall
print()
print('Logaritmefunksjoner:')
print('f(x) = log.a (x). a er basen som kan være hvilket som helst tall,\n'
      'men som oftest 10 eller e. Kan ses på som invers eksponentialfunksjon')
print('den naturlige logaritmen med e som base uttrykkes slik f(x) = ln(x)')
# mer info: You can use the natural log in the same way that you use the exponential function. 
# It’s used to calculate values such as the rate of population growth or 
# the rate of radioactive decay in elements.
print('Om du bare gir ett tall som input får du den naturlige logaritmen')
print('math.log(4) gir',(math.log(4)),'.') # her er basen e
print('math.log(4 ,2) gir',(math.log(4, 2)),' med base 2.')
print('math.log(4, 5) gir',(math.log(4, 5)),' med base 5.')
print('math.log2(4) gir',(math.log2(4)),' med base 2.') # math.log2 og 10 er mer nøyaktige
print('math.log10(4) gir',(math.log10(4)),' med base 10.')
print('math.log10(100) gir',(math.log10(100)),' med base 10.')
print('---')
print('Praktisk eksempel - finn radioaktiv halveringstid')
print('Formel: T = -693t / ln(N(t)/N(0) ')
initial = 100
remaining = 16.22
time = 100
half_life = (-0.693 * time) / math.log(remaining / initial)
print(f"Halveringstiden til stoffet: {half_life} år")
print('Dermed vet vi at stoffet er Strontium-90')
print()
print()

print('---')
print ('Pi fra math gjengis med 15 desimaler: \n', # husk komma før tall her
       '   ',(pi))
print(f'Arealet av en sirkel med radius {r} er:\n'
      f'    {pi*r*r}')
print(f'Omkrets av en sirkel med radius {r} er:\n'
      f'    {tau*r}')
print()
print(f'Uendelig kan også uttrykkes i math: {inf}')
print('Maksstørrelse på desimaltall i Python er 10**308,\n'
      'og når det deles på uendelig blir svaret: ',(z/inf),)
print(f'Om det deles på minus uendelig blir svaret: {z/-inf}')
print()
print ('Eulers tall fra math gjengis med 15 desimaler: \n', # husk komma før tall her
       '   ',(e))
print()
print('Fakultet kan gjøres med loop og med rekursiv fuksjon, \n'
      'men math.factorial er raskest.')
fakultet = math.factorial(7)
print(f' 7 fakultet er: {fakultet}')
print('---')

print()
print('Andre funksjoner i math:')
print('math.gcd() finner største felles divisor')
print('For eksempel har 120 og 80:',math.gcd(120,80),'som størte f.d.') 
print('---')
print('Kalkuler summen av "iterables", feks. [12, 15, 6, 89]')
tall1 = [12, 15, 6, 89]
print('Summen av [12, 15, 6, 89] er:',math.fsum(tall1))
print('---')
print('math.sqrt() gir kvadratrota av 49:',math.sqrt(49))
print('---')
print('Konvertere fra grader til radianer og omvendt:')
print(f'30 grader er:{round(math.radians(30),2)} radianer, og 5 radianer er:{round(math.degrees(5),2)} grader.')
print('---')
print('Trigonometri: ')
print('Sinus, cosinus og tangens av 0,786  radianer er: ')
print(math.sin(0.786), math.cos(0.786), math.tan(0.786))
print('0,786 radianer er',math.degrees(0.786),'grader.')
print('---')
print('Vi kan også konvertere 45 grader til radianer og så finne sin cos tan:')
print('Med samme metode som lenger opp: gtr= math.radians(45)')
gtr= math.radians(45)
print(math.sin(gtr), math.cos(gtr), math.tan(gtr))
print('---')
print('Til slutt - finn hypotenus i rettvinklet trekant enkelt!')
print('Vi har en trekant med katet 3 og 4, og bruker math.hypot(3, 4)')
print(math.hypot(3, 4))



