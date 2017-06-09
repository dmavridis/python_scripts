# Pay attention to the pattern

import re
import matplotlib.pyplot as plt

file = open('mpc_data.txt','r')

x = []
y = []
pattern = re.compile('[0-9.-]+')

for line in file.readlines():
    if line.startswith('x ='):
        m = pattern.search(line)
        x.append(float(m.group()))
    if line.startswith('y ='):
        m = pattern.search(line)
        y.append(float(m.group()))        
file.close()        
        
        
plt.scatter(x,y)
