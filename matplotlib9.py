# -*- coding: utf-8 -*-
"""
MatplotLib Bar
çubuk grafiklerini anlatıyor

@author: user
"""
#buradaki bar dikey yani verticaldı.
import matplotlib.pyplot as plt
import numpy as np 
"""
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)
plt.show()
"""

"""
x = np.array(["Apple", "Banana", "berry", "Orange"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
"""

#Horizantal 

x = np.array(["etherscan", "bnb", "avaScan", "Chainlink"])
y = np.array([3, 8, 1, 10])
#yatay bir bar vermemizi sağlıyor
plt.barh(x, y ,color="g" ,height=0.3) 
plt.show()



