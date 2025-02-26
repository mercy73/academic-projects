import matplotlib.pyplot as p
#rainfall data
isiolo=[20,40,60,90,80]
meru=[60,80,120,100,135]
months=("january","february","march","april","may")
p.bar(months,meru)
p.title("histogram of meru")