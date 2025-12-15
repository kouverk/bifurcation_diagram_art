#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
%matplotlib inline

title = "r*np.cos(x)"
def chaos(r, x):
    return eval(title)

n = 100000
maxr = 25
minr = 1.3

r = np.linspace(0, maxr, n)
iterations = 10000
last = 1000
x = 1e-5 * np.ones(n)

fig, ax1 = plt.subplots(1, 1, figsize=(25, 20), dpi=400)

for i in tqdm(range(iterations)):
    x = chaos(r, x)
    if i >= (iterations - last):
        ax1.plot(r, x, ',k', alpha=.25)
ax1.set_xlim(minr, maxr)
ax1.set_title(title)

plt.tight_layout()

# In[ ]:



