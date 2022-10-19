import pandas as pd

from model import SCAMDD

data = pd.read_csv('data/iris.csv', index_col=0)

model = SCAMDD(data)