# import pandas as pd
import numpy as np

def current(dob):
    return 2021 - dob
# d=pd.DataFrame({"name":['Amaan','Nolan','Nolan'],"age":[12,34,1],"music":['y','n','n']})
# print(d.fillna(value=0))
# print(d.sample(1))
# print(d.nunique())
# print(d.columns)
# print(d.nlargest(1,"age"))

import pandas as pd

data={"ages":[1231,1232,1234,1235]}
# Create a DataFrame
# data = {'Team': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B'],
#         'Player': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10'],
#         'Score': [1012, 2031, 1315, 2115, 3118, 3310, 2312, 1031, 2112,
#                   31 32]}
df = pd.DataFrame(data)
df['bin']=pd.qcut(df['ages'],q=2,labels=['low','high'])
print(df)
# cat=df.select_dtypes(include='object')
# num=df.select_dtypes(include=[np.number])
# con=pd.concat([cat,num],axis=0)
# print(con)
# Group by the 'Team' column
# grouped = df.groupby('Player').describe()
# print(grouped)

# # Iterate over groups and print them
# for name, group in grouped:
#     print(f"Team: {name}")
#     print(group)
#     print("\n")
