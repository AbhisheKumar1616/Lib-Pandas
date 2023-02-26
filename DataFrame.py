import numpy as np
import pandas as pd

dic1={"Names":["Abhishek","Aman","Kumar"],
      "Age":[20,21,22]}
df=pd.DataFrame(dic1)
df.to_csv("test1.csv")
df.to_csv("test2.csv", index=False)
print(df)