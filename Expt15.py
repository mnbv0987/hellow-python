#Data visualization and manipulation in Python
import matplotlib.pyplot as plt
import numpy as np

yield_apples = [0.895,0.91,0.919,0.929,0.931]
plt.plot(yield_apples)
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()


import matplotlib.pyplot as plt
import numpy as np


#plot 1:	
x = np.array([0, 1, 2,	3])
y = np.array([3, 8, 1,	10])
plt.subplot(2, 1, 1)	
plt.plot(x,y)	
#plot 2:	
x = np.array([0, 1, 2,	3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "#4CAF50")
plt.show()
