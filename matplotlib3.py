# -*- coding: utf-8 -*-
"""
W3schools markers (belirteçler)
Her noktayı belirli bir işaretleyiciyle vurgulamak için anahtar kelime argüman 
marker kullanabilirsiniz:

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np 
"""
ypoints = np.array([3,8,1,10])
plt.plot(ypoints,marker ="o") # istersek plt.plot(ypoints, marker = '*') yapabiliriz(ops)
plt.show() 
"""
"""
Dizeleri Biçimlendir fmt
İşaretçiyi belirtmek için kısayol dizesi notasyonu parametresini de kullanabilirsiniz.

Bu parametre aynı zamanda fmt olarak da adlandırılır ve şu söz dizimi ile yazılır:

işaret|çizgi|renk
"""
"""
ypoint =np.array([2,7,3,9])
plt.plot(ypoint,"*--b")
plt.show()
"""
#markersize - markerredgecolor-markerfacecolor 
# ms                mec         mfc  
#işaretlemesi yapıyoruz
ypoint =np.array([2,7,3,9])
plt.plot(ypoint, marker = ".", markersize =15, mfc="r", mec ="r")
plt.show()





