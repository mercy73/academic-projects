# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:50:44 2023

@author: masiyon
"""
import matplotlib.pyplot as p
#rainfall data
isiolo=[20,40,60,90,80]
meru=[60,80,120,100,135]
months=("january","february","march","april","may")
p.plot (months,meru)
p.plot(months,isiolo)
p.title("rainfall from two towns")
p.legend(["meru","isiolo"])
