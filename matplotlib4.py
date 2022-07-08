# -*- coding: utf-8 -*-
"""
matplotlib Line

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
"""
ypoints = np.array([3, 8, 1, 10])
# çizgi tipi için linestyle kullanılır ls kısası
plt.plot(ypoints, linestyle = 'dashed',color="r")
plt.show()
"""
"""
ypoints = np.array([3, 8, 1, 10])
#kalın bir şekilde yazılmasını sağlıyor ve kısası lw
plt.plot(ypoints, linewidth = '20.5')
plt.show()
"""
"""
# iki tane eğrinin yapısı
y1 = np.array([3, 7, 2, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
"""


x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 4])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()










