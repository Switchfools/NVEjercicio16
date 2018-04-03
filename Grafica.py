import numpy as np
import matplotlib.pylab as plt
Laminas= np.loadtxt('Laminas.txt')
NCompras=range(len(Laminas[:,0]))
plt.plot(NCompras,Laminas[:,0], color='teal')
plt.plot(NCompras,Laminas[:,1], color='gold')
plt.savefig('laminas.png')
