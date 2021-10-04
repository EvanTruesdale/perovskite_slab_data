import numpy as np
import matplotlib.pyplot as plt

# Section III.B plotting
data_reference = np.loadtxt('avg_rho_0.dat')
for size in np.arange(5, 85, 5):
    data = np.loadtxt('avg_rho_{_size}.dat'.format(_size=int(size)))
    plt.plot(data[:,0], data[:,1] - data_reference[:,1])
    plt.savefig('screening_rho_{_size}.png'.format(_size=int(size)), dpi=300)
    plt.clf()
