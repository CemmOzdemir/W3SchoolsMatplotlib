# -*- coding: utf-8 -*-
"""
Matplotlib pasta grafiği kullanımı pie() şeklinde kullanılır.
@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
"""
y = np.array([35, 25, 25, 15])
mylabels =["BTC","ETH","AVA","LINK"]
plt.pie(y,labels = mylabels)
plt.show() 

"""
#explode parametresi değer almadan arraydeki ilk idex[0] olanın pasta payını böler

"""
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 
"""
#shadow parametresi burada pastanın payının ayrılan yerini 2 boyut yapıyor
"""
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()
"""
"""
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()
"""
# legend parametresinde ise lsite oluşmasını saağlıyor üstte


y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()








