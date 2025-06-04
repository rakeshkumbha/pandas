import pandas as pd
import numpy as np

s = pd.Series() 
print("Pandas Series: ", s) 

data = np.array([1,6,8,4,9]) 
  
s = pd.Series(data) 
print("Pandas Series:\n", s)

