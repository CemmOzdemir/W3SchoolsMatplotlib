# -*- coding: utf-8 -*-
"""
Matplotlib Scatter()
 ... .... .. gibi grafiklri saçılmış şekilde görememize yarar
 ihtiyacı olan şeyler: aynı uzunluktaki 2 tane veri kümesine, birisi x,diğeri
  y değerlerine ihtiyaç duyar.
  Dikkat Color ksımına Burada değinmedin çünkü çok uzun :) 
  Bu yüzden color kısmına w3schools matplotlib Scatter bölümünden bakınız.
@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
"""
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
"""
"""
#iki farklı grafiği kıyaslamak için ise:

#birinci gün 13 adet arabanın hızı ve yaşlarına göre verisi:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#ikinci gün 15 adet arabanın hızları ve yaşlarına göre verisi:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x, y)

plt.show()

"""
