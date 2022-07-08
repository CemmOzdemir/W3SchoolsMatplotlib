"""
Grid  ızgara şeklinde grafiklerimizi kareli kareli şekle sokar

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
"""
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Spotcu değerlendirme verilenmesi")
plt.xlabel("ortalma çalışma süresi")
plt.ylabel("cal yanması")
plt.plot(x,y)
plt.grid()
plt.show()
"""
"""
#Burada yapılan şey grid rengini stilini ve kalınlığını ayarlamak
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Spotcu değerlendirme verilenmesi")
plt.xlabel("ortalma çalışma süresi")
plt.ylabel("cal yanması")
plt.plot(x,y)

plt.grid(color="g", linestyle ="--",linewidth=1)
plt.show()
"""




