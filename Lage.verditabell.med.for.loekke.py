# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:20:09 2021, @author: jokane
"""
import os
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('Hvis vi kaster en ball opp i lufta fra 1,5 meters høyde\n'
      'og en startfart på 12 m/s - hvor befinner den seg etter\n'
      '0, 0.5, 1, 1.5, 2, 2.5 sekunder?')
print('Vi skal lage en verditabell for verdier av t\n'
      'med formelen s = s0 + v0t + 1/2at^2')

s0 = 1.5
v0 = 1
a = -9.81
print()
print('Tid      strekning')

for t in [0, 0.5, 1, 1.5, 2, 2.5]:
    s = s0 + v0*t + (1/2)*a*t**2
    print (f'{t:.1f}      {s:.1f} ')

print('-------------------------------------------')
print('Vi kan også bruke en for-løkke til å lage en liste med\n'
      'x-verdier og så bruke dem i formelen for å lage en\n'
      'verditabell.')
# et annet eksempel der vi kan bruke en for-løkke til å legge inn
# mange x-verdier. 
penger = 15000
rente = 1.025

for aar in [1,2,3,4,5,6,20]:
    penger *= rente
    print(f'Etter {aar} år er saldo {penger:.0f} kroner.')