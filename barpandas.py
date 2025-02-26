import pandas as pd
#rainfall data
isiolo=[20,40,60,90,80]
meru=[60,80,120,100,135]
months=("january","february","march","april","may")
df=pd.DataFrame({'isiolo': isiolo,'meru':meru},index=months)
df.plot.bar()