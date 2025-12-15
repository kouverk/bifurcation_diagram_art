#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
%matplotlib inline

title = "r*np.exp(-.5*(1-x)**2)*np.cos(.37*np.exp(x)**2)"
def choas(r, x):
    return eval(title)

n = 250000
maxr = 5
minr = 1.85

r = np.linspace(0, maxr, n)
iterations = 10000
last = 1000
x = 1e-5 * np.ones(n)

fig, ax1 = plt.subplots(1, 1, figsize=(25, 20), dpi=400)

for i in tqdm(range(iterations)):
    x = choas(r, x)
    if i >= (iterations - last):
        ax1.plot(r, x, ',k', alpha=.1)
ax1.set_xlim(minr, maxr)
ax1.set_title(title)

plt.tight_layout()

# In[ ]:



