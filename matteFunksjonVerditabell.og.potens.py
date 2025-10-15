# import math
import matplotlib.pyplot as plt
import numpy as np
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Enkel måte å lage verditabell til funksjonen: f(x) = 3x**2 + 1: \n'
      'Verdiene vi bruker for x er 0 til 8, men steglende på 2.')
print()
# xverdier = [0,2,4,6,8] # vanlig liste med 5 verdier
xverdier = np.linspace(-4,10,15) # array med start, stopp, antall punkter (pass på å få heltall helst)
print(xverdier)
yverdier = [] # tom liste
print()
print ('x | f(x)')
print('__________')

# for x in range(len(xverdier)): 

for a in xverdier:  
    print(f'{a:.1f} | {3*a**2+1:.1f}') # den midlertidige variabelen heter a
    yverdier.append(3*a**2+1)

yverdier = np.array(yverdier) # yverdier var fortsatt liste så den måtte bli til array
print('Verditabell:',xverdier, yverdier)
print(type(xverdier), type(yverdier)) # sjekker at det er array
print()
print('----')
plt.plot(yverdier)
plt.grid(True)
plt.show()



'''
#potensfunksjon med input
print('Potensfunksjon med input:')
print('Finn ut hvilket grunntall vi skal undersøke+n'
      'og så velg hvor høyt vi skal gå i eksponent, altså fra 1 til ditt valg')
a = int(input('Tast inn grunntallet: '))
b = int(input('Tast inn eksponenten: '))

def raise_to_power():
    result=1
    for index in range(b):
        result = result  * a
        print(result)

raise_to_power()
print('----')
print('Bruk math.pow(a,b) for å finne tallet direkte: ')           
print('a opphøyd i b:',(math.pow(a, b)))
'''