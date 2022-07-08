"""
matplotlib Labels

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
"""
#grafikin yanlarında etiketlerinin çıkmasını sağladı.Aynı Zamanda başlıkta
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

#Burada başlık ve etiket renklerini değiştiriyoruz

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fondict=font1)
plt.xlabel("Average Pulse" , fondict=font2)
plt.ylabel("Calorie Burnage", fondict=font2)

plt.show()

"""

