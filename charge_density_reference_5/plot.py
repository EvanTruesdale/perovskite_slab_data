import numpy as np
import matplotlib.pyplot as plt

# for size in np.arange(0, 44, 5):
#     data = np.loadtxt('avg_{_size}.dat'.format(_size=int(size)))
#     plt.plot(data[:,0], data[:,1] + data[:,2])
# plt.savefig('avg_ex_45.png', dpi=300)

# data = np.loadtxt('energy_data')
# plt.plot(data[:,0], data[:,1])
# plt.savefig('energy_data.png', dpi=300)

for size in np.arange(0, 61, 5):
    data = np.loadtxt('avg_{_size}.dat'.format(_size=int(size)))
    data_reference = np.loadtxt('avg_{_size}_reference.dat'.format(_size=int(size)))
    plt.plot(data[:,0], data[:,1] - data_reference[:,1])
    plt.savefig('diff_{_size}.png'.format(_size=int(size)), dpi=200)
    plt.clf()
