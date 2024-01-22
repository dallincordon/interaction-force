#!/usr/bin/env python

import numpy as np
import itertools
import pandas as pd
from interaction_eqs import *

# Loop over possible conditions
l = [3,5,7,-3,-5,-7,0]
# l = [3,-5,7]
r = 3
table  = []
row = [99,99,99,99,99,99,99,99,99]
for p in itertools.product(l, repeat=r):
    Fa = p[0]
    Fg = p[1]
    Fb = p[2]
    row[0] = literature_def(Fa,Fb,Fg)
    row[1] = spencers(Fa,Fb,Fg)
    row[2] = inv_spencers(Fa,Fb,Fg)
    row[3] = leader_follower(Fa,Fb,Fg)
    row[4] = leader_leader(Fa,Fb,Fg)
    row[5] = isolation(Fa,Fb,Fg)
    row[6] = vis_F(Fa)
    row[7] = vis_F(Fg)
    row[8] = vis_F(Fb)
    row 
    table.append(row)
    row = [99,99,99,99,99,99,99,99,99]

# Print the table
headers=[]
df = pd.DataFrame(table, columns=['Lit', 'Spen','inv', 'LF', 'LL', 'Iso','Fa','Fg','Fb'])
df.style.format("- {:.4f} -")
# print(df)
df.to_csv('compare_interactions.csv', index=False)
