import cv2
import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread('/home/vivek/Desktop/img.jpg', cv2.IMREAD_GRAYSCALE)

# IMREAD_COLOR=1
# IMREAD_UNCHANGED=-1

# cv2.imshow('/home/vivek/Desktop/img.jpg',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


plt.imshow(img, cmap = "Blues", interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth=10)
plt.show()

