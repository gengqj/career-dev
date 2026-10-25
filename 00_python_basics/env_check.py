import sys, pandas as pd, numpy as np, sklearn, matplotlib, seaborn, sqlalchemy
print("Python :", sys.version.split()[0])
print("pandas :", pd.__version__)
print("numpy  :", np.__version__)
print("sklearn:", sklearn.__version__)
df = pd.DataFrame({"a": [1,2,3], "b": [4,5,6]})
print("pandas OK, a+b sum =", int((df.a+df.b).sum()))
