import numpy as np
import pandas as pd

"""Series"""
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2,3],[2,3,4],[5,4,3]])

labels = ['a', 'b', 'c', 'd']
series1 = pd.Series(data = arr1, index=labels)
print(series1)

