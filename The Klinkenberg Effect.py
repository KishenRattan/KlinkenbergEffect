# Generated from: The Klinkenberg Effect.ipynb
# Converted at: 2026-03-23T15:11:51.246Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import numpy as np
import matplotlib.pyplot as plt
k = float(input("Enter the initial guess of absolute permeability(md):"))
pmean = float(input("Enter The mean pressure(psi):"))
kgas = float(input("Enter the gas perm.(md):"))


while abs(6.9*(k**0.64)+pmean*k-pmean*kgas) > 0.0001:
    k = k - (6.9*(k**0.64)+pmean*k - pmean*kgas)/(4.416*(k**(-0.36))+pmean)
    
print("The value of absolute permeability after iteration or gas permeability at infinite pmean is ",k)

x = [0,1/pmean]
y = [k,kgas]

coefficients = np.polyfit(x,y,1)
polynomial = np.poly1d(coefficients)
x_axis = np.linspace(0,0.2,0.01)
y_axis = polynomial(x_axis)
plt.plot(x_axis, y_axis)
plt.plot(x,y)
plt.xlabel("1/Mean_pressure (psi^-1)")
plt.ylabel("Measured Gas Permeability(md)")
plt.title("The Klinkenberg Effect")
plt.grid(True)
plt.show()


##JC