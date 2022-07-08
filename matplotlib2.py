# -*- coding: utf-8 -*-
"""
Created on Wed Jul  

x ve y noktalarının çizilmesi
plot() işlevi, bir diyagramda noktalar (işaretler) çizmek için kullanılır.

Varsayılan olarak, plot() işlevi noktadan noktaya bir çizgi çizer.

İşlev, diyagramdaki noktaları belirtmek için parametreler alır.

Parametre 1, x eksenindeki noktaları içeren bir dizidir.

Parametre 2, y eksenindeki noktaları içeren bir dizidir.

(1, 3)'den (8, 10)'a bir çizgi çizmemiz gerekirse, 
çizim işlevine [1, 8] ve [3, 10] olmak üzere iki dizi iletmemiz gerekir.


@author: User
"""
"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([4, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

"""

"""
import matplotlib.pyplot as plt
import numpy as np
xpont = np.array([1, 2, 5, 8])
ypont = np.array([3, 1, 8, 5])

plt.plot(xpont,ypont)
plt.show()

"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()




