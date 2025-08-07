"""Install
pip install matplotlib
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([2,6,8,4,3])
plt.plot(x,y)
plt.show()


plt.scatter(x, y)
plt.show()


"""بررسی توضیع داده"""

plt.hist(x)
plt.show()



"""خوندن عکس"""
pic1 = plt.imread('F:/Work/Python/AI 1404/Bioneers/Python/PythonPractice/Matplotlib/images.png')
#Return Array from pixel

plt.imshow(pic1)
plt.show()


pic2 = mpimg.imread('F:/Work/Python/AI 1404/Bioneers/Python/PythonPractice/Matplotlib/images.png')
#Return Array from pixel

plt.imshow(pic2)
plt.show()

print(pic2.shape)
"""(168, 300, 4)
اون 4 عمق عکس هستش
یا همان کانال های رنگ هستش


سیاه و سفید  => 0-255

: 3کاناله
Red / gray / Blue (RGB)

256 * 256 * 256 = 16581375

این عکس چون ترنس پرنت است 4 تا کانال داره

"""

"""دریافت کانال سوم"""
plt.imshow(pic1[:, :, 2])
plt.show()