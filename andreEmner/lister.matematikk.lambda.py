# -*- coding: utf-8 -*-
"""Author Jørn Kanestrøm"""

import math
import statistics
print()

ds = [1, 2, 3, 3, 4, 6, 9]
snitt1 = statistics.mean(ds)
print('Om vi har ei liste med tallene:',ds)
print('Er gjennomsnittet: ', snitt1)

print('______________________________________________')
print()

numbers = [1, 2, 3, 4, 5]
for index in range(len(numbers)):
    numbers[index] = numbers[index]**2
print('De 5 første kvadrattallene er:',numbers)
snitt2 = statistics.mean(numbers)
print('Gjennomsnittet av de 5 første kvardattallene er:',snitt2)

print('______________________________________________')
print()

tall = [12,13,14,15,16]
for i in range (len(tall)):
    tall[i]=tall[i]/3
rund2desi = [round(num, 2) for num in tall] #ny liste avrundet
print('Tallene er 12 t.o.m 16')
print('Alle de tallene delt på 3 og avrundet til 2 desimaler er:')
print(rund2desi)

print('______________________________________________')
print()








