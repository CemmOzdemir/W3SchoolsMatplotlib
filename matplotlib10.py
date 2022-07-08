# -*- coding: utf-8 -*-
"""
matplotlib Histogram :
    Sıklık grafikleri yapmamızı sağlar fonksiyonu hist() dir

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(90, 15, 120)

plt.hist(x,color ="red")
plt.show()
