#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
%matplotlib inline

def logistic(r, x):
    return r * x * (1 - x)

n = 1000000
maxr = 4.0
minr = 3.4

r = np.linspace(0, maxr, n)
iterations = 10000
last = 100
x = 1e-5 * np.ones(n)

fig, ax1 = plt.subplots(1, 1, figsize=(15, 9))

for i in tqdm(range(iterations)):
    x = logistic(r, x)
    if i >= (iterations - last):
        ax1.plot(r, x, ',k', alpha=.01)
ax1.set_xlim(minr, maxr)
ax1.set_title("Bifurcation diagram")

plt.tight_layout()

# In[ ]:



