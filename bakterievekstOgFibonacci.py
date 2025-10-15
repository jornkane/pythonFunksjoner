# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:35:08 2024, @author: jokane
"""
import os
os.system('cls' if os.name == 'nt' else 'clear')  

import numpy as np
import matplotlib.pyplot as plt

print()
print('----------------------------------------')
print('Bakterievekst: Bn = Bn-1 * 2')
antall_dager = 12
bakterier = np.zeros(antall_dager)
bakterier[0] = 3  # vi starter med 3 bakterier

print('Bakterier dag 1:', bakterier[0])  # 1 3.0. Antall bakterier dag 1

for i in range(1, antall_dager):
    bakterier[i] = 2 * bakterier[i - 1]
    print('Dag', i + 1, 'Bakt.', bakterier[i])

print()
print('Antall bakterier dag 3:',bakterier[2])  # 1 3.0. Antall bakterier dag 3

dag = np.arange(antall_dager)
plt.plot(dag + 1, bakterier)
plt.title('Bakterievekst')
plt.xlabel('Dag')
plt.ylabel('Antall bakterier')
plt.grid(True)
plt.show()

print()
print('----------------------------------------')
print('Fibonacci: Fn = Fn-1 + Fn-2')
print('Hvert tall er lik summen av de to forrige.')
antall_dager = 9
bakterier = np.zeros(antall_dager)
bakterier[1] = 1  # neste er 1
bakterier[2] = 1  # neste er 1
print('Fibonacci nr 0 =', bakterier[0])
print('Fibonacci nr 1 =', bakterier[1])
for i in range(2, antall_dager):
    bakterier[i] = bakterier[i - 1] + bakterier[i - 2]
    print('Fibonacci nr', i, '=', bakterier[i])
print()
print('F6=', bakterier[6])  # 1 3.0
print()

dag = np.arange(antall_dager)
plt.plot(dag, bakterier)
plt.title('Fibonacci-sekvens')
plt.xlabel('Indeks')
plt.ylabel('Verdi')
plt.grid(True)
plt.show()
